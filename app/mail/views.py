from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render

# Create your views here.

@login_required
def mail_me(request):
    if request.method == 'POST':
        name = request.user.username
        email = request.user.email
        subject = request.POST['mail-object']
        message = request.POST['mail-text']
        try:
            send_mail(
                subject + ' from ' + name + ' (' + email + ')',
                message,
                'blog@slb-fullweb.tech',
                ['contact@slb-fullweb.tech'])
            return render(request, 'mail/mail_sent.html')
        except:
            return render(request, 'mail/mail_error.html')
    return render(request, 'mail/mail_me.html')

def mail_error(request):
    return render(request, 'mail/mail_error.html')

def mail_sent(request):
    return render(request, 'mail/mail_sent.html')
