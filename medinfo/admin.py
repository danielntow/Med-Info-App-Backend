from django.contrib import admin

from django.db.models import ManyToOneRel, ForeignKey, OneToOneField


# Register your models here.

from .models import *


def MySpecialAdmin(model): return type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
})


class DrugAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Drug._meta.fields]


class DosageAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Dosage._meta.fields]


class AdverseEffectAdmin(admin.ModelAdmin):
    list_display = [x.name for x in AdverseEffect._meta.fields]


class IndicationAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Indication._meta.fields]


admin.site.register(Drug, DrugAdmin)
admin.site.register(Dosage, DosageAdmin)
admin.site.register(Indication, IndicationAdmin)
admin.site.register(AdverseEffect, AdverseEffectAdmin)
