from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template



from django.dispatch import receiver

from rest_framework.authtoken.models import Token

# Create your models here.
@receiver(post_save, sender=User)
def create_auth_token_for_validation(sender, instance, created, **kwargs):
    token_create = Token.objects.create(user=instance)

    # emailing tokens
    message = get_template("emails/authtoken_verification.html").render({
        'token_key':token_create.key
    })
    mail = EmailMessage(
        subject="DEH Sabaq | Your verification token",
        body=message,
        from_email="fezzey072@gmail.com",
        to=[instance.email]
    )
    mail.content_subtype = "html"
    mail.send()
    