# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404
from .models import Weather_Station,Plant,Soil_Moisture_Sensor,Actuator,Water_body
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#Function index
def index(request):
    	context={'plant':1,'plant1':2}
	return render(request,'index.html',context)  # returning context values to index.html page 
received_data=[]
temp_data=[]
hum_data=[]
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
#Function detail
def detail(request,plant_id):
    for i in range(1,9):
    	temp_data.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].tem_value) #Storing last 8 values of temperature values in list
    	hum_data.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].hum_value)  #Storing last 8 values of humidity values in list
    	a.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].a_value)
    	b.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].b_value)
    	c.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].c_value)
    	d.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].d_value)
    	e.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].e_value)
    	f.append(Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-i].f_value)
    rain_data=Weather_Station.objects.order_by('id_w')[len(Weather_Station.objects.all())-1].rain_value	#Storing rain_value in rain_data
    water_data=Water_body.objects.filter(plant=plant_id).order_by('id_wa')[len(Water_body.objects.filter(plant=plant_id).order_by('id_wa'))-1].water_value #Storing water_value in water_data
    soil_data=Soil_Moisture_Sensor.objects.filter(plant=plant_id).order_by('id_s')[len(Soil_Moisture_Sensor.objects.filter(plant=plant_id).order_by('id_s'))-1].soil_value #Storing soil_value in soil_data
    motor_data=Actuator.objects.filter(plant=plant_id).order_by('id_a')[len(Actuator.objects.filter(plant=plant_id).order_by('id_a'))-1].motor_value #Storing motor_value in motor_data
    plantid=get_object_or_404(Plant,pk=plant_id)	#retriving plant_id from the argument
    context={'tem':temp_data[0],'hum':hum_data[0],'tem1':temp_data[1],'hum1':hum_data[1],'tem2':temp_data[2],'hum2':hum_data[2],'tem3':temp_data[3],'hum3':hum_data[3],'tem4':temp_data[4],'hum4':hum_data[4],'tem5':temp_data[5],'hum5':hum_data[5],'tem6':temp_data[6],'hum6':hum_data[6],'tem7':temp_data[7],'hum7':hum_data[7],'mois':soil_data,'rain':rain_data,'water':water_data,'motor':motor_data,'a1':a[0],'a2':a[1],'a3':a[2],'a4':a[3],'a5':a[4],'a6':a[5],'a7':a[6],'a8':a[7],'b1':b[0],'b2':b[1],'b3':b[2],'b4':b[3],'b5':b[4],'b6':b[5],'b7':b[6],'b8':b[7],'c1':c[0],'c2':c[1],'c3':c[2],'c4':c[3],'c5':c[4],'c6':c[5],'c7':c[6],'c8':c[7],'d1':d[0],'d2':d[1],'d3':d[2],'d4':d[3],'d5':d[4],'d6':d[5],'d7':d[6],'d8':d[7],'e1':e[0],'e2':e[1],'e3':e[2],'e4':e[3],'e5':e[4],'e6':e[5],'e7':e[6],'e8':e[7]} # Assigning sensor values to respective word 
    return render(request,'temp.html',context)   # returning context values to detail.html page 
#Function getdata
def getdata(request):
 if request.method=='GET' :          # If request metod is get method following values are retrived
  plant_id=request.GET['id']
  tem_value=request.GET['temperature']  # retriving temperature value from get method
  hum_value=request.GET['humidity']     # retriving humidity value from get method
  rain_value=request.GET['rain_info_1']     #retriving rain status from get method
  a_value=request.GET['a']
  b_value=request.GET['b']
  c_value=request.GET['c']
  d_value=request.GET['d']
  e_value=request.GET['e']
  f_value=request.GET['f']
  t_obj=Weather_Station()           # Weather object is assigned to t_obj
  t_obj.tem_value=tem_value         # tem_value obtained above is assigned to t_obj.tem_value
  t_obj.hum_value=hum_value         # hum_value obtained above is assigned to t_obj.hum_value
  t_obj.rain_value=rain_value       # rain status obtained above is assigned to t_obj.rain_value
  t_obj.a_value=a_value
  t_obj.b_value=b_value
  t_obj.c_value=c_value
  t_obj.d_value=d_value
  t_obj.e_value=e_value
  t_obj.f_value=f_value
  t_obj.plant=1
  t_obj.save()
  water_value=request.GET['water_lev']      #retriving water_level value from get method
  w_obj=Water_body()
  w_obj.water_value=water_value     # water_value obtained above is assigned to t_obj.water_value 
  w_obj.save()
  soil_value=request.GET['soil_moisture']   # retriving soil moisture value from get method
  motor_value=request.GET['motor']
  s_obj=Soil_Moisture_Sensor()
  s_obj.soil_value=soil_value       # soil_value obtained above is assigned to t_obj.soil_value
  s_obj.plant=1
  s_obj.save()
  a_obj=Actuator()
  a_obj.motor_value=motor_value
  a_obj.plant=1
  a_obj.save()
  t_obj1=Weather_Station()                # Weather object is assigned to t_obj
  t_obj1.tem_value=tem_value         # tem_value obtained above is assigned to t_obj.tem_value
  t_obj1.hum_value=hum_value         # hum_value obtained above is assigned to t_obj.hum_value
  t_obj1.rain_value=rain_value       # rain status obtained above is assigned to t_obj.rain_value
  t_obj1.a_value=a_value
  t_obj1.b_value=b_value
  t_obj1.c_value=c_value
  t_obj1.d_value=d_value
  t_obj1.e_value=e_value
  t_obj1.f_value=f_value
  t_obj1.plant=2
  t_obj1.save()
  w_obj1=Water_body()
  w_obj1.water_value=water_value     # water_value obtained above is assigned to t_obj.water_value 
  w_obj1.save()
  soil_value=request.GET['soil_moisture1']   # retriving soil moisture value from get method
  motor_value=request.GET['motor1']
  s_obj1=Soil_Moisture_Sensor()
  s_obj1.soil_value=soil_value       # soil_value obtained above is assigned to t_obj.soil_value
  s_obj1.plant=2
  s_obj1.save()
  a_obj1=Actuator()
  a_obj1.motor_value=motor_value
  a_obj1.plant=2
  a_obj1.save()

  return HttpResponse("data saved in db")
 else:
  return HttpResponse("error")
