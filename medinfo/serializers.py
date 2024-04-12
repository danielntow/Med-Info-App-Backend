from rest_framework import serializers
from .models import Drug, Dosage, AdverseEffect, Indication, Warning, Administration, PregnancyLactation, Contraindication


class DosageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosage
        fields = '__all__'


class AdverseEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdverseEffect
        fields = '__all__'


class IndicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indication
        fields = '__all__'


class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = '__all__'


class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = '__all__'


class PregnancyLactationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PregnancyLactation
        fields = '__all__'


class ContraindicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contraindication
        fields = '__all__'


# class DrugSerializer(serializers.ModelSerializer):
#     dosage = DosageSerializer(many=True, read_only=True)
#     adverse_effects = AdverseEffectSerializer(many=True, read_only=True)
#     indications = IndicationSerializer(many=True, read_only=True)
#     warnings = WarningSerializer(many=True, read_only=True)
#     administrations = AdministrationSerializer(many=True, read_only=True)
#     pregnancy_lactations = PregnancyLactationSerializer(
#         many=True, read_only=True)
#     contraindications = ContraindicationSerializer(many=True, read_only=True)

#     class Meta:
#         model = Drug
#         fields = '__all__'

# serializers.py

class DrugSerializer(serializers.ModelSerializer):
    dosages = serializers.SerializerMethodField()
    adverse_effects = serializers.SerializerMethodField()
    indications = serializers.SerializerMethodField()
    warnings = serializers.SerializerMethodField()
    administrations = serializers.SerializerMethodField()
    pregnancy_lactations = serializers.SerializerMethodField()
    contraindications = serializers.SerializerMethodField()

    class Meta:
        model = Drug
        fields = ['id', 'name', 'dosages', 'adverse_effects', 'indications',
                  'warnings', 'administrations', 'pregnancy_lactations', 'contraindications']

    def get_dosages(self, obj):
        return [dosage.description for dosage in obj.dosage_set.all()]

    def get_adverse_effects(self, obj):
        return [adverse_effect.description for adverse_effect in obj.adverseeffect_set.all()]

    def get_indications(self, obj):
        return [indication.description for indication in obj.indication_set.all()]

    def get_warnings(self, obj):
        return [warning.description for warning in obj.warning_set.all()]

    def get_administrations(self, obj):
        return [administration.description for administration in obj.administration_set.all()]

    def get_pregnancy_lactations(self, obj):
        return [pregnancy_lactation.description for pregnancy_lactation in obj.pregnancylactation_set.all()]

    def get_contraindications(self, obj):
        return [contraindication.description for contraindication in obj.contraindication_set.all()]
