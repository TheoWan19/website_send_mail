from django.shortcuts import render
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.

def create_view(request, *args, **kwargs):
	''' This view help to create 
	an account for testing send email'''
	cxt = {}
	if request.method == 'POST':
		email = request.POST.get('email')

		template = 'send_mail/email.html'	

		context = {
			'date': datetime.today().date,
			'email': email,
		}

		subject = 'Test Email'
		message = render_to_string(template, context)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email]
		if send_mail(subject, message, email_from, recipient_list):
			cxt = {'message': 'envoie avec success'}

	return render(request, 'send_mail/home.html', cxt)


