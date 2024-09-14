from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Alumni, DisasterAlert

@admin.register(Alumni)
class AlumniAdmin(OSMGeoAdmin):
    list_display = ('name', 'email', 'city', 'country', 'graduation_year', 'latitude', 'longitude')
    readonly_fields = ('latitude', 'longitude')


@admin.register(DisasterAlert)
class DisasterAlertAdmin(OSMGeoAdmin):
    list_display = ('title', 'severity', 'created_at', 'latitude', 'longitude')
    readonly_fields = ('latitude', 'longitude')