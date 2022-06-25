from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django_countries.fields import CountryField
from smart_selects.db_fields import ChainedForeignKey



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_email_verified', True)
        other_fields.setdefault('is_premium', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')


        return self.create_user(email, username, first_name, last_name, password, **other_fields)

    def create_user(self, email, username, first_name, last_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



class CompanyRole(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=2, null=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Office(models.Model):
    company_role = models.ForeignKey(CompanyRole, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name




class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    comments = models.TextField(_(
        'comments'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    company_role = models.ForeignKey(CompanyRole, on_delete=models.SET_NULL, null=True, blank=True)



    # office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True)
    office = ChainedForeignKey(
        Office,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        chained_field="company_role",
        chained_model_field="company_role",
        show_all=False,
        auto_choose=True,
        sort=True,
        )

    #location = CountryField(null=True)
    location = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    # location = ChainedForeignKey(
    #     Office,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="location",
    #     chained_field="country",
    #     chained_model_field="country",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True)



    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username


