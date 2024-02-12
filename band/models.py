# band/models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import CustomUser

class Band(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextUploadingField()
    cover_image = models.ImageField(upload_to='band_covers/', blank=True, null=True)
    # Add more fields as needed

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Band"
        verbose_name_plural = "Bands"

class MembershipType(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='membership_types')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)  # e.g., 'One Year', 'Three Years', 'Five Years'

    def __str__(self):
        return f"{self.band.name} - {self.name}"

    class Meta:
        verbose_name = "Membership Type"
        verbose_name_plural = "Membership Types"

class CommonFields(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Members Common Fields"
        verbose_name_plural = "Members Common Fields"

class PaymentType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Payment Type"
        verbose_name_plural = "Payment Types"
    
class Membership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='memberships')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='memberships')
    common_fields = models.OneToOneField(CommonFields, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    # Add more fields as needed

    def __str__(self):
        return f"{self.user.email} - {self.band.name} - {self.membership_type.name} - {self.payment_type.name}"

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"
