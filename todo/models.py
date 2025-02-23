from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    complete_by = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=1)
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.completed and not self.completed_at:
            self.completed_at = now()
        elif not self.completed:
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # Signal to send email after task is completed
@receiver(post_save, sender=Task)
def send_task_completed_email(sender, instance, created, **kwargs):
    if instance.completed:
        send_mail(
            'Task Completed',
            f'Your task "{instance.title}" has been completed.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
