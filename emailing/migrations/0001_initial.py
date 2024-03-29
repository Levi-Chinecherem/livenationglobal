# Generated by Django 5.0.2 on 2024-02-13 16:20

import ckeditor_uploader.fields
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=255)),
                ('message_content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('sent_datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('to_users', models.ManyToManyField(related_name='emails_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email Message',
                'verbose_name_plural': 'Email Messages',
            },
        ),
    ]
