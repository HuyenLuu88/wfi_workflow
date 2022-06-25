from django.conf import settings
from rest_framework import serializers

from apps.portfolio.models import Identifier


class IdentifierSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    created = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    updated = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Identifier
        # fields = '__all__'
        fields = ('id', 'code', 'code_type', 'created', 'updated', 'valid')


