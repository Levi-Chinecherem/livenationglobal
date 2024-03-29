# Generated by Django 5.0.2 on 2024-02-12 14:18

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='band_covers/')),
            ],
            options={
                'verbose_name': 'Band',
                'verbose_name_plural': 'Bands',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Payment Type',
                'verbose_name_plural': 'Payment Types',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='band.band')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
            },
        ),
        migrations.CreateModel(
            name='CommonFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('membership', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='common_fields', to='band.membership')),
            ],
            options={
                'verbose_name': 'Members Common Fields',
                'verbose_name_plural': 'Members Common Fields',
            },
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duration', models.CharField(max_length=50)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_types', to='band.band')),
            ],
            options={
                'verbose_name': 'Membership Type',
                'verbose_name_plural': 'Membership Types',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='membership_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.membershiptype'),
        ),
        migrations.AddField(
            model_name='membership',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.paymenttype'),
        ),
    ]
