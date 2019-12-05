from rest_framework import viewsets
from . import models
from . import serializers

class IncidentViewset(viewsets.ModelViewSet):
    queryset = models.Incident.objects.all()
    serializer_class = serializers.IncidentSerializer
    filterset_fields = {
        'id': ['exact', 'lte', 'gte', 'isnull'],
        'date_created': ['exact', 'lte', 'gte', 'isnull'],
        'date_ended': ['exact', 'lte', 'gte', 'isnull']
    }

class ContaminantViewset(viewsets.ModelViewSet):
    queryset = models.Contaminant.objects.all()
    serializer_class = serializers.ContaminantSerializer

class ReferenceViewset(viewsets.ModelViewSet):
    queryset = models.Reference.objects.all()
    serializer_class = serializers.ReferenceSerializer

class AffectedUSStateViewset(viewsets.ModelViewSet):
    queryset = models.AffectedUSState.objects.all()
    serializer_class = serializers.AffectedUSStateSerializer