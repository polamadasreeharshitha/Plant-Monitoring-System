# -*- coding: utf-8 -*-

# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Plant(models.Model):
       plant_id=models.AutoField(primary_key=True)
       def __str__(self):
           return ' '+str(self.plant_id)
class Weather_Station(models.Model):
        id_w=models.AutoField(primary_key=True)
	plant=models.IntegerField(null=True)
	tem_value=models.CharField(max_length=250)
	hum_value=models.CharField(max_length=250)
        rain_value=models.CharField(max_length=250)
        a_value=models.CharField(max_length=250)
        b_value=models.CharField(max_length=250)
        c_value=models.CharField(max_length=250)
        d_value=models.CharField(max_length=250)
        e_value=models.CharField(max_length=250)
        f_value=models.CharField(max_length=250)
        def __str__(self):
           return 'id:'+str(self.id_w)+'plant_id:'+str(self.plant)+'temperature:'+str(self.tem_value)+'humidity:'+str(self.hum_value)+'rain:'+str(self.rain_value)+'date:'+str(self.a_value)+'month:'+str(self.b_value)+'year:'+str(self.c_value)+'Hour:'+str(self.d_value)+'Minute:'+str(self.e_value)+'seconds:'+str(self.f_value)
class Soil_Moisture_Sensor(models.Model):
        id_s=models.AutoField(primary_key=True)
        #plant_id1=models.ForeignKey(Plant,on_delete=models.CASCADE,null=True)
	plant=models.IntegerField(null=True)
        soil_value=models.CharField(max_length=250)
        def __str__(self):
           return 'id:'+str(self.id_s)+'plant_id:'+str(self.plant)+'soil_value:'+str(self.soil_value)  
class Actuator(models.Model):
        id_a=models.AutoField(primary_key=True)
        #plant_id2=models.ForeignKey(Plant,on_delete=models.CASCADE,null=True)
	plant=models.IntegerField(null=True)
        motor_value=models.CharField(max_length=250)
        def __str__(self):
           return 'id:'+str(self.id_a)+'plant id:'+str(self.plant)+'motor:'+str(self.motor_value)
class Water_body(models.Model):
        id_wa=models.AutoField(primary_key=True)
	plant=models.IntegerField(null=True)
        water_value=models.CharField(max_length=250)
        def __str__(self):
           return 'id:'+str(self.id_wa)+'plant_id:'+str(self.plant)+'water_level:'+str(self.water_value)
