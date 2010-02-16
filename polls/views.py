#coding=utf-8
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from models import Choice, Poll, OBJ_STATUS_ARCHIV
from libs.shortcuts import render_to

@render_to('polls/poll_detail.html')
def detail(request, object_id):
    p = get_object_or_404(Poll.active.all(), pk=object_id)
    return {'object': p,
            'show_results': p.is_voted(request) or p.status==OBJ_STATUS_ARCHIV,}

def vote(request, object_id):
    p = get_object_or_404(Poll.active.all(), pk=object_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/poll_detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        request.session['vote_%s' % p.id] = True

#        print request.session._session_key
#        print request.session.keys
            
        if request.POST.get('redirect'):
            return HttpResponseRedirect(request.POST['redirect'])
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
