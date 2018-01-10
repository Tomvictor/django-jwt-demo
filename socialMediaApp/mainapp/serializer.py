from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
)
from mainapp.models import College


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = [
            'id',
            'name',
            'city',
        ]