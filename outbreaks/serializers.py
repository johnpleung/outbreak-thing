from rest_framework import serializers
from . import models

class IncidentSerializer(serializers.ModelSerializer):
    affected_us_states = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Incident
        fields = ('id', 'description', 'date_created', 'date_ended', 'affected_food_description', 'affected_food_type', 'severity', 'details', 'affected_us_states')

class ContaminantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contaminant
        fields = ('description')

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reference
        fields = ('org_name')

class AffectedUSStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AffectedUSState
        fields = ('abbrev')
