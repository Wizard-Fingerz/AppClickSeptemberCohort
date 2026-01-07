from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from students.models import Student
from django.contrib.auth.models import User
from django.dispatch import Signal

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

original_student_created = Signal(providing_args=["instance"])
original_student_created.send(sender=None, instance=None)

@receiver(original_student_created)
def handle_original_student_created(sender, instance, **kwargs):
    logger.info(f'Original signal received for student creation: {instance}')
    # print(f'Original signal received for student creation: {instance}')


@receiver(post_save, sender=Student)
def create_user_for_student(sender, instance, created, **kwargs):
    if created:
        # Create a User account for the new Student
        User.objects.create_user(
            username=instance.name.replace(" ", "").lower(),
            password='defaultpassword123',  # In a real app, generate a secure password or prompt for one
        )
        print(f'User account created for student: {instance.name}')


@receiver(post_delete, sender=Student)
def delete_user_for_student(sender, instance, **kwargs):
    # Delete the associated User account when a Student is deleted
    try:
        user = User.objects.get(username=instance.name.replace(" ", "").lower())
        user.delete()
        print(f'User account deleted for student: {instance.name}')
    except User.DoesNotExist:
        print(f'No user account found for student: {instance.name}')