from django.contrib import admin
from .models import User, CompanyRole, Office, Country
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username', 'email', 'first_name', 'last_name', 'is_email_verified', 'is_active', 'is_staff', 'company_role', 'office', 'location')
    list_filter = ('is_staff', 'is_superuser', 'is_email_verified', 'is_active', 'company_role', 'office', 'location')
    ordering = ('-start_date',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_email_verified',
                    'is_active', 'is_staff', 'company_role', 'office', 'location')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'is_premium')}),
        (('Employee info'), {'fields': ('company_role', 'office', 'location')}),
        (('Permissions'), {'fields': ('is_email_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Other info'), {'fields': ('comments',)}),
        (('Important dates'), {'fields': ('last_login', 'start_date')}),

    )
    formfield_overrides = {
        User.comments: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_email_verified', 'is_active', 'is_staff', 'is_superuser', 'company_role', 'office', 'location')}
         ),
    )

admin.site.register(User, UserAdminConfig)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    ordering = ('name',)
    list_display = ('name', 'code')





#admin.site.register(Country)
admin.site.register(CompanyRole)
admin.site.register(Office)