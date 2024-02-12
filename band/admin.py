# band/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Band, PaymentType, MembershipType, Membership, CommonFields

admin.site.site_title = _('LiveNationGlobal Admin')
admin.site.site_header = _('LiveNationGlobal Administration')
admin.site.index_title = _('Site Administration')

class CommonFieldsInline(admin.StackedInline):
    model = CommonFields
    can_delete = False

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    inlines = [CommonFieldsInline]
    list_display = ('user', 'band', 'membership_type', 'payment_type')  # Update to use 'payment_type'
    search_fields = ('user__email', 'band__name', 'membership_type__name')
    
@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name = 'Payment Type'
    verbose_name_plural = 'Payment Types'

@admin.register(CommonFields)
class CommonFieldsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'phone_number', 'country', 'state', 'city')
    search_fields = ('full_name',)
