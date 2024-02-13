# emailing/models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import CustomUser
from django.utils import timezone

class EmailInfo(models.Model):
    to_users = models.ManyToManyField(CustomUser, related_name='emails_received')
    company_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=255)
    message_content = RichTextUploadingField()
    sent_datetime = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{', '.join(user.email for user in self.to_users.all())} - {self.purpose}"

    class Meta:
        verbose_name = "Email Message"
        verbose_name_plural = "Email Messages"
