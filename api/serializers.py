from dataclasses import field
from rest_framework import serializers
from .models import Family, Child

class FamilyChildSerializers(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True)
    class Meta:
        model = Family
        fields = ('_id', 'surname', 'parent1', 'parent2', 'children')

class FamilySerializers(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class ChildSerializers(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'