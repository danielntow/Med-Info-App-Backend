from django.shortcuts import render
from .serializers import DrugSerializer
from .models import Drug
from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework import viewsets
from .models import Drug, Dosage, AdverseEffect, Indication, Warning, Administration, PregnancyLactation, Contraindication
from .serializers import DrugSerializer, DosageSerializer, AdverseEffectSerializer, IndicationSerializer, WarningSerializer, AdministrationSerializer, PregnancyLactationSerializer, ContraindicationSerializer
from django.shortcuts import get_object_or_404


class DrugsViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class DosagesViewSet(viewsets.ModelViewSet):
    queryset = Dosage.objects.all()
    serializer_class = DosageSerializer


class DosageViewSet(viewsets.ModelViewSet):
    queryset = Dosage.objects.all()
    serializer_class = DosageSerializer


class DrugViewSet(viewsets.ModelViewSet):
    # queryset = Drug.objects.all()
    queryset = Drug.objects.prefetch_related('dosage', 'adverse_effects', 'indications',
                                             'warnings', 'administrations', 'pregnancy_lactations', 'contraindications').all()
    serializer_class = DrugSerializer


class DrugListView(generics.ListAPIView):
    serializer_class = DrugSerializer

    def get_queryset(self):
        queryset = Drug.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))
        return queryset


class DrugDetailView(generics.RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    lookup_field = 'name'

    def get_object(self):
        # value of the 'name' parameter from the URL
        name = self.kwargs[self.lookup_field]

        # case-insensitive lookup
        drug = get_object_or_404(self.get_queryset().model, name__iexact=name)

        # Ensure the object is accessible to the user
        self.check_object_permissions(self.request, drug)
        return drug
