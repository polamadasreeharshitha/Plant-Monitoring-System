# -*- coding: utf-8 -*-

# Register your models here.
from django.contrib import admin
from .models import Weather_Station,Plant,Actuator,Water_body,Soil_Moisture_Sensor

# Register your models here.
admin.site.register(Weather_Station)
admin.site.register(Plant)
admin.site.register(Water_body)
admin.site.register(Soil_Moisture_Sensor)
admin.site.register(Actuator)
