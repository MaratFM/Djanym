from django.conf import settings
from django.forms.widgets import Textarea
from django.db.models import SubfieldBase, TextField
from django.utils import simplejson
from django.db import models  

if getattr(settings, 'USE_CPICKLE', False):
    import cPickle as pickle
else:
    import pickle


class JSONField(TextField):
    __metaclass__ = SubfieldBase

    def contribute_to_class(self, cls, name):
        super(JSONField, self).contribute_to_class(cls, name)

        def get_json(model):
            return self.get_db_prep_value(getattr(model, self.attname))
        setattr(cls, 'get_%s_json' % self.name, get_json)

        def set_json(model, json):
            setattr(model, self.attname, self.to_python(json))
        setattr(cls, 'set_%s_json' % self.name, set_json)

    def formfield(self, **kwargs):
        kwargs['widget'] = JSONWidget(attrs={'class': 'vLargeTextField'})
        return super(JSONField, self).formfield(**kwargs)

    def get_db_prep_value(self, value):
        return simplejson.dumps(value)

    def to_python(self, value):
        if not isinstance(value, basestring):
            return value

        try:
            return simplejson.loads(value, encoding=settings.DEFAULT_CHARSET)
        except ValueError, e:
            # If string could not parse as JSON it's means that it's Python
            # string saved to JSONField.
            return value

class JSONWidget(Textarea):
    """
    Prettify dumps of all non-string JSON data.
    """
    def render(self, name, value, attrs=None):
        if not isinstance(value, basestring) and value is not None:
            value = simplejson.dumps(value, indent=4, sort_keys=True)
        return super(JSONWidget, self).render(name, value, attrs)
    
    
    
    
    
    
    
    
    
    

class PickleField(models.TextField):
    __metaclass__ = models.SubfieldBase

    editable = False
    serialize = False

    def get_db_prep_value(self, value):
        return pickle.dumps(value)

    def to_python(self, value):
        if not isinstance(value, basestring):
            return value

        # Tries to convert unicode objects to string, cause loads pickle from
        # unicode excepts ugly ``KeyError: '\x00'``.
        #
        # If not possible, return this value, cause it's not pickled yet.
        if isinstance(value, unicode):
            try:
                str_value = str(value)
            except UnicodeEncodeError:
                return value
        else:
            str_value = value

        try:
            return pickle.loads(str_value)
        except ValueError:
            # If pickle could not loads from string it's means that it's Python
            # string saved to PickleField.
            return value    
        
        
        
        
        
        
        
        
        
        
        
        
        

# ======================================================================
#
# http://webnewage.org/post/2008/9/26/krasivaya-kompozitsiya/
# http://webnewage.org/post/2008/10/7/kompozitsiya-foreignattributefield/
# http://svn.turbion.org/turbion/trunk/turbion/core/utils/composition.py
# ======================================================================

# -*- coding: utf-8 -*-
from copy import deepcopy

from django.db import models
from django.db.models.related import RelatedObject
from django.utils.itercompat import is_iterable

class Trigger(object):
    def __init__(self, do, on, field_name, sender, sender_model, commit,\
                 field_holder_getter):
        self.freeze = False
        self.field_name = field_name
        self.commit = commit

        if sender_model and not sender:
            if isinstance(sender_model, basestring):
                sender_model = models.get_model(*sender_model.split(".", 1))
            self.sender = self.sender_model = sender_model
        else:
            self.sender = sender
            self.sender_model = sender_model

        if not do:
            raise ValueError("`do` action not defined for trigger")
        self.do = do

        if not is_iterable(on):
            on = [on]
        self.on = on

        self.field_holder_getter = field_holder_getter

    def connect(self):
        """
           Connects trigger's handler to all of its signals
        """
        for signal in self.on:
            signal.connect(self.handler, sender=self.sender)

    def handler(self, signal, instance=None, **kwargs):
        """
            Signal handler
        """
        if self.freeze:
            return

        objects = self.field_holder_getter(instance)
        if not is_iterable(objects):
            objects = [objects]

        for obj in objects:
            setattr(obj, self.field_name, self.do(obj, instance, signal))

            if self.commit:
                obj.save()

class CompositionMeta(object):
    def __init__(self, model, field, name, trigger,\
                  commons, commit, update_method):#TODO: remove commit param
        self.model = model
        self.name = name
        self.trigger = []

        if not commons:
            commons = {}
        self.commons = commons

        if not is_iterable(trigger) or isinstance(trigger, dict):
            trigger = [trigger]

        trigger_defaults = dict(
                sender_model=model,
                sender=None,
                on=[models.signals.post_save],
                field_holder_getter=lambda instance: instance,
                field_name=name,
                commit=True
        )
        trigger_defaults.update(commons)

        if not len(trigger):
            raise ValueError("At least one trigger must be specefied")

        for t in trigger:
            trigger_meta = trigger_defaults.copy()
            trigger_meta.update(t)

            trigger_obj = Trigger(**trigger_meta)
            trigger_obj.connect()

            self.trigger.append(trigger_obj)

        update_method_defaults = dict(
            initial=None,
            name="update_%s" % name,
            do=self.trigger[0],
            queryset=None
        )
        update_method_defaults.update(update_method)

        if isinstance(update_method_defaults["do"], (int, long)):
            n = update_method_defaults["do"]
            if n >= len(self.trigger):
                raise ValueError("Update method trigger must be index of trigger list")
            update_method_defaults["do"] = self.trigger[update_method_defaults["do"]]

        self.update_method = update_method_defaults

        setattr(model, self.update_method["name"], lambda instance: self._update_method(instance))
        setattr(model, "freeze_%s" % name, lambda instance: self._freeze_method(instance))

    def togle_freeze(self):
        for t in self.trigger:
            t.freeze = not t.freeze

    def _update_method(self, instance):
        """
            Generic `update_FOO` method that is connected to model
        """
        qs_getter = self.update_method["queryset"]
        if qs_getter is None:
            qs_getter = [instance]

        trigger = self.update_method["do"]

        setattr(instance, trigger.field_name, self.update_method["initial"])
        if callable(qs_getter):
            qs = qs_getter(instance)
        else:
            qs = qs_getter

        if not is_iterable(qs):
            qs = [qs]

        for obj in qs:
            setattr(
                instance,
                trigger.field_name,
                trigger.do(instance, obj, trigger.on[0])
            )

        instance.save()

    def _freeze_method(self, instance):
        """
            Generic `freeze_FOO` method that is connected to model
        """
        self.toggle_freeze()

class CompositionField(object):
    def __init__(self, native, trigger=None, commons={},\
                     commit=True, update_method={}):
        self.internal_init(native, trigger, commons, commit, update_method)

    def internal_init(self, native=None, trigger=None, commons={},\
                     commit=True, update_method={}):
        """
            CompositionField class that patches native field
            with custom `contribute_to_class` method

            Params:
                 * native - Django field instance for current compostion field
                 * trigger - one or some numberr of triggers that handle composition.
                    Trigger is a dict with allowed keys:
                      * on - signal or list of signals that this field handles
                      * do - signals handler, with 3 params:
                               * related instance
                               * instance (that comes with signal send)
                               * concrete signal (one from `on` value)
                      * field_holder_getter - function that gets instance(that comes with signal send)\
                                              as parameter and returns field holder
                                              object (related instance)
                      * sender - signal sender
                      * sender_model - model instance or model name that send signal
                      * commit - flag that indicates save instance after trigger appliance or not
                 * commons - a trigger like field with common settings
                             for all given triggers
                 * update_method - dict for customization of update_method. Allowed params:
                        * initial - initial value to field before applince of method
                        * do - index of update trigger or trigger itself
                        * queryset - query set or callable(with one param - `instance` of an holder model)
                                that have to retun something iterable
                        * name - custom method name instead of `update_FOO`
        """
        if native is not None:
            import new
            self.__class__ = new.classobj(
                                    self.__class__.__name__,
                                    tuple([self.__class__, native.__class__] + list(self.__class__.__mro__[1:])),
                                    {}
                                )

            self.__dict__.update(native.__dict__)

        self._c_native = native

        self._c_trigger = trigger
        self._c_commons = commons
        self._c_commit = commit
        self._c_update_method = update_method

    def contribute_to_class(self, cls, name):
        self._c_name = name

        if not self._c_native:
            models.signals.class_prepared.connect(
                            self.deferred_contribute_to_class,
                            sender=cls
                        )
        else:
            self._composition_meta = self.create_meta(cls)
            return self._c_native.__class__.contribute_to_class(self, cls, name)

    def create_meta(self, cls):
        return CompositionMeta(
                    cls, self._c_native, self._c_name, self._c_trigger,\
                    self._c_commons, self._c_commit, self._c_update_method
                )

    def deferred_contribute_to_class(self, sender, **kwargs):
        cls = sender

        self.introspect_class(cls)
        self._composition_meta = self.create_meta(cls)
        return self._c_native.__class__.contribute_to_class(self, cls, self._c_name)

    def introspect_class(self, cls):
        pass

class ForeignAttribute(CompositionField):
    """
        Composition field that can track changes of related objects attributes.
    """
    def __init__(self, field, native=None):
        """
            field - path to related field, e.g. 'director.country.name'
            native - field instance to store value
        """
        self.field = field
        self.native = native

        self.internal_init()

    def introspect_class(self, cls):
        bits = self.field.split(".")

        if len(bits) < 2:
            raise ValueError("Illegal path to foreign field")

        foreign_field = None

        related_models_chain = [cls]
        related_names_chain = []

        for bit in bits[:-1]:
            meta = related_models_chain[-1]._meta

            try:
                foreign_field = meta.get_field(bit)
            except models.FieldDoesNotExist:
                raise ValueError("Field '%s' does not exist" % bit)

            if isinstance(foreign_field, models.ForeignKey):
                if isinstance(foreign_field.rel.to, basestring):
                    raise ValueError("Model with name '%s' must be class instance not string" % foreign_field.rel.to)

                related_name = foreign_field.rel.related_name
                if not related_name:
                    related_name = RelatedObject(
                                    foreign_field.rel.to,
                                    related_models_chain[-1],
                                    foreign_field
                                ).get_accessor_name()

                related_models_chain.append(foreign_field.rel.to)
                related_names_chain.append(related_name)
            else:
                raise ValueError("Foreign fields in path must be ForeignField"
                                 "instances except last. Got %s" % foreign_field.__name__)

        native = self.native
        if not native:
            field_name = bits[-1]
            try:
                native = deepcopy(related_models_chain[-1]._meta.get_field(field_name))
                native.creation_counter = models.Field.creation_counter
                models.Field.creation_counter += 1
            except models.FieldDoesNotExist:
                raise ValueError("Leaf field '%s' does not exist" % field_name)

        def get_root_instances(instance, chain):
            attr = getattr(instance, chain.pop()).all()

            if chain:
                for obj in attr:
                    for inst in get_root_instances(
                                        obj,
                                        chain
                                    ):
                        yield inst
            else:
                for obj in attr:
                    yield obj

        def get_leaf_instance(instance, chain):
            for bit in chain:
                instance = getattr(instance, bit)

            return instance

        self.internal_init(
            native=native,
            trigger=[
                dict(
                    on=(models.signals.post_save, models.signals.post_delete),
                    sender_model=related_models_chain[-1],
                    do=lambda holder, foreign, signal: getattr(foreign, bits[-1]),
                    field_holder_getter=lambda foreign: get_root_instances(foreign, related_names_chain[:])
                ),
                dict(
                    on=models.signals.pre_save,
                    sender_model=related_models_chain[0],
                    do=lambda holder, _, signal: get_leaf_instance(holder, bits[:]),
                    commit=False, # to prevent recursion `save` method call
                )
            ],
            update_method=dict(
                queryset=lambda holder: get_leaf_instance(holder, bits[:-1])#FIXME: rename queryset
            )
        )
        # TODO: add support for selective object handling to prevent pre_save unneeded work

ForeignAttributeField = ForeignAttribute

class AttributesAggregation(CompositionField):
    def __init__(self, field, do, native=None):
        self.field = field
        self.do = do
        self.native = native

AttributesAggregationField = AttributesAggregation

class ChildsAggregation(CompositionField):
    def __init__(self, field, do, native=None, signal=None, instance_getter=None):
        self.field = field
        self.do = do
        self.native = native
        self.signal = signal
        self.instance_getter = instance_getter

ChildsAggregationField = ChildsAggregation

        