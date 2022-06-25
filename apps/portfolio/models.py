from django.db import models
from apps.account.models import User
from django.utils import timezone
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from model_utils import Choices

class IdentifierType(models.Model):
    name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class PriorityType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(TimeStampMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, unique=True)
    # identifier_type = models.ForeignKey(IdentifierType, on_delete=models.CASCADE, null=True)
    actflag = models.CharField(max_length=1, blank=True)
    comments = models.TextField(_(
        'comments'), max_length=30, blank=True)
    priority = models.ForeignKey(PriorityType, on_delete=models.CASCADE, null=True)
    deadline = models.DateField(blank=True, null=True)
    initial = models.IntegerField(blank=True, null=True)
    update = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    invalid = models.IntegerField(blank=True, null=True)
    isin_count = models.IntegerField(blank=True, null=True)
    uscode_count = models.IntegerField(blank=True, null=True)
    sedol_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


# class ISIN(TimeStampMixin, models.Model):
#     code = models.CharField(max_length=12)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
#     actflag = models.CharField(max_length=1, blank=True)
#     valid = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.code
#
# class USCODE(TimeStampMixin, models.Model):
#     code = models.CharField(max_length=9)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
#     actflag = models.CharField(max_length=1, blank=True)
#     valid = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.code



ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'code'),
    ('2', 'code_type'),
    ('3', 'created'),
    ('4', 'updated'),
    ('5', 'valid'),
)





class Identifier(TimeStampMixin, models.Model):
    # code_id = models.IntegerField(null=True)
    code_type = models.CharField(max_length=10, null=True)
    code = models.CharField(max_length=12)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    actflag = models.CharField(max_length=1, blank=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    class Meta:
        db_table = "portfolio_identifier"

    #JSON
    def get_data(self):
        return{
            'id': self.id,
            'code': self.code,
            'code_type': self.code_type,
            'created': self.created,
            'updated': self.updated,
            'valid': self.valid,
        }


# def query_identifier_by_args(**kwargs):
#     draw = int(kwargs.get('draw', None)[0])
#     length = int(kwargs.get('length', None)[0])
#     start = int(kwargs.get('start', None)[0])
#     search_value = kwargs.get('search[value]', None)[0]
#     order_column = kwargs.get('order[0][column]', None)[0]
#     order = kwargs.get('order[0][dir]', None)[0]
#
#     order_column = ORDER_COLUMN_CHOICES[order_column]
#     # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column
#
#     queryset = Identifier.objects.all()
#
#
#     total = queryset.count()
#
#     if search_value:
#         queryset = queryset.filter(Q(id__icontains=search_value) |
#                                         Q(code__icontains=search_value) |
#                                         Q(code_type__icontains=search_value) |
#                                         Q(created__icontains=search_value) |
#                                         Q(updated__icontains=search_value) |
#                                         Q(valid__icontains=search_value))
#
#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }
