# emailing/admin.py
from django.contrib import admin
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import EmailInfo
from django.conf import settings
from django.utils import timezone

@admin.register(EmailInfo)
class EmailInfoAdmin(admin.ModelAdmin):
    list_display = ('get_to_users_emails', 'company_name', 'purpose', 'sent_datetime')

    actions = ['send_email_action']

    def send_email_action(self, request, queryset):
        from_email = settings.EMAIL_HOST_USER
        email_template = 'email/email1.html'

        for email_info in queryset:
            to_emails = [user.email for user in email_info.to_users.all()]

            html_message = render_to_string(email_template, {
                'company_name': email_info.company_name,
                'purpose': email_info.purpose,
                'message_content': email_info.message_content,
            })

            send_mail(
                f"Subject: {email_info.purpose}",
                '',
                from_email,
                to_emails,
                html_message=html_message,
                fail_silently=False,
            )

            email_info.sent_datetime = timezone.now()
            email_info.sent = True
            email_info.save()

        self.message_user(request, f"Emails have been sent to {queryset.count()} recipients.")

    send_email_action.short_description = "Send selected emails"

    def get_to_users_emails(self, obj):
        return ', '.join(user.email for user in obj.to_users.all())

    get_to_users_emails.short_description = "To Users"
