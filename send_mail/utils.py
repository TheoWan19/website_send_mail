from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

import logging

logger = logging.getLogger(__name__)

def send_email_with_html_body(subject: str, receivers: list, template: str, context: dict):
	# This function help to send a customize email to a specific user or to set of users

	try:
		message = render_to_string(template, context)
	except Exception as e:
		logger.error(e) 