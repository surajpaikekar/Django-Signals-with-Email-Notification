# signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .email_helper import send_email
from .models import MyModel

# signals.py
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .email_helper import send_email
from .models import MyModel

@receiver(pre_save, sender=MyModel)
def pre_save_modify_fields(sender, instance, **kwargs):
    print("pre-save signal triggered!")
    # Perform actions or modifications before saving
    instance.name = "vasanth sai"

@receiver(post_save, sender=MyModel)
def post_save_send_notification(sender, instance, created, **kwargs):
    if created:  # Only send email if a new instance is created
        print("Post-save signal triggered!")
        subject = "A new data has been added into your model"
        message = f"Data with instance {instance.id} and {instance.name} has been added."
        to_email = 'example@gmail.com'
        send_email(subject, message, to_email)

