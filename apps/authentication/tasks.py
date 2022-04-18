from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from apps.authentication.models import ActivationToken


@shared_task
def send_invitation_email(token_id):
    activation_token = ActivationToken.objects.get(id=token_id)
    user = activation_token.user
    message_context = {
        "user": user,
        "activation_token": activation_token,
        "site_url": settings.SITE_URL,
    }

    text = render_to_string(
        "email/registration/user_activation.txt", context=message_context
    )
    html = render_to_string(
        "email/registration/user_activation.html", context=message_context
    )

    mail = EmailMultiAlternatives(
        "Activate your account please",
        text,
        to=[user.email],
    )
    mail.attach_alternative(html, "text/html")
    mail.send()
