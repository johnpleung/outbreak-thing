from django.contrib import admin
from outbreaks.models import Contaminant, Incident, Reference, AffectedUSState


# Inlines

class ContaminantInline(admin.TabularInline):
    model = Contaminant

class ReferenceInline(admin.TabularInline):
    model = Reference

class AffectedUSStateInline(admin.TabularInline):
    model = AffectedUSState

# Register models

admin.site.register(Contaminant)

admin.site.register(Reference)

admin.site.register(AffectedUSState)

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    inlines = [ContaminantInline, ReferenceInline, AffectedUSStateInline]