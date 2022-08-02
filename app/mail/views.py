from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render

# Create your views here.

@login_required
def mail_me(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            'Message from ' + name,
            message,
            email)
    return render(request, 'mail/mail_me.html')
        