from django.contrib import admin
from .models import IdentifierType, PriorityType, Account, Identifier


class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    # search_fields = ('name', 'code')
    ordering = ('id',)
    list_display = ('name', 'user', 'created', 'updated', 'priority', 'deadline', 'initial', 'update', 'total',)

# class ISINAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', 'updated',)
#     # search_fields = ('name', 'code')
#     # ordering = ('name',)
#     list_display = ('code', 'valid')
#
#
#
# class USCODEAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', 'updated',)
#     # search_fields = ('name', 'code')
#     # ordering = ('name',)
#     list_display = ('code', 'valid')


class IdentifierAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    # search_fields = ('name', 'code')
    ordering = ('id',)
    list_display = ('code_type', 'code', 'valid', 'account')


# Register your models here.
admin.site.register(IdentifierType)
admin.site.register(PriorityType)
admin.site.register(Account, AccountAdmin)
# admin.site.register(ISIN, ISINAdmin)
# admin.site.register(USCODE, USCODEAdmin)
admin.site.register(Identifier, IdentifierAdmin)