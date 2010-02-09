#coding=utf-8
from djanym.libs.shortcuts import render_to
from forms import FeedbackForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives  
from django.template.loader import render_to_string 
import re 

EMAIL_SPLIT_RE = re.compile('\n\-{3,}\n')

@render_to('feedback/result.html')
def feedback(request):
    '''
    '''
    message = u'Форма обратной связи' 
    if request.method == 'POST':    
        form = FeedbackForm(request.POST) 
   
        if form.is_valid():

            email = render_to_string('feedback/email.html', {'object': form.cleaned_data})
            subject, content = EMAIL_SPLIT_RE.split(email, 1)            
            
            from_email = settings.DEFAULT_FROM_EMAIL                                                               
            to_email = getattr(settings, 'FEEDBACK_EMAILS', [e[1] for e in settings.MANAGERS])     

            msg = EmailMultiAlternatives(subject, content, from_email, to_email)                                   
            msg.content_subtype = "html"                                                                       
            msg.send()
            
            message = u'Ваш вопрос успешно отправлен!'
            form = None
    else:            
        form = FeedbackForm()

    return {
            'form': form,
            'message': message,            
            }