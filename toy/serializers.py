from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('name', 'textfield1', 'datetimefield1')