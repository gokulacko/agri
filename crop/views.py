from django.shortcuts import render, redirect
import crop.forms as f
import crop.models as m
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import CropFilter

import crop.helper as h
import numpy as np

from sklearn import svm, preprocessing
import pandas as pd

import warnings

from twilio.rest import Client

# Create your views here.

# @login_required(login_url='/accounts/login/')


ph=0
water = 0
temp = 0
lands = ""


features = [
          
          
          
          'ph_min',
          'ph_max',
          'min_temp',
          'max_temp',
          'water'
          
          
          ]



def index(request):
     # message = " Hi, gokul Notifiacation from Farm smart."
     # data = h.sendSMS("919677844081", message)

     # print(data)
     try:
          profile = m.Profile.objects.get(user__id = request.user.id)
          request.profile = profile
          print(request.profile.id)
     except:
          messages.error(request, ' Please add profile')

     # account = "AC48175e94606d4f4d12acf863c2d250ef"
     # token = "128f9f24762516c01bcbfb5376f5dfb0"
     # client = Client(account, token)

     # message = client.messages.create(to="9677844081", from_="9677844081",
     #                             body="Hello sms test for agri!")
     return render(request, 'crop/indexs.html')

def addland(request):

     if request.method == "POST":
          form =f.LandForm(request.POST)
          
          if form.is_valid():
               data = form.save(commit=False)
               data.user = request.user
               data.save()
               messages.success(request, ' Land details added successfully')
          else:
               messages.error(request, ' Land details not added successfully')  
          return redirect('index')
     else:
          form = f.LandForm(initial={'user': request.user})
          context = {
                    'form': form,
               }
     return render(request, 'crop/add_land.html', context)

def addSoilTest(request):

     if request.method == "POST":
          form =f.SoilForm(request.POST)
          
          if form.is_valid():
               data = form.save(commit=False)
               data.user = request.user
               data.save()
               messages.success(request, ' Land details added successfully')
          else:
               messages.error(request, ' Land details not added successfully')  
          return redirect('index')
     else:
          form = f.SoilForm()
          context = {
                    'form': form,
               }
     return render(request, 'crop/add_soil_test.html', context)

def addCrop(request):

     if request.method == "POST":
          form =f.CropForm(request.POST)
          
          if form.is_valid():
               # data = form.save(commit=False)
               # data.user = request.user
               form.save()
               messages.success(request, ' Crop added successfully')
          else:
               messages.error(request, ' Crop not added successfully')  
          return redirect('index')
     else:
          form = f.CropForm()
          context = {
                    'form': form,
               }
     return render(request, 'crop/add_crop.html', context)


def addVarity(request):

     if request.method == "POST":
          form =f.VarityForm(request.POST)
          
          if form.is_valid():
               # data = form.save(commit=False)
               # data.user = request.user
               form.save()
               messages.success(request, ' Varity added successfully')
          else:
               messages.error(request, ' Varity not added successfully')  
          return redirect('index')
     else:
          form = f.VarityForm()
          context = {
                    'form': form,
               }
     return render(request, 'crop/add_varity.html', context)


def addDisease(request):

     if request.method == "POST":
          form =f.DiseaseForm(request.POST)
          
          if form.is_valid():
               # data = form.save(commit=False)
               # data.user = request.user
               form.save()
               messages.success(request, ' Disease added successfully')
          else:
               messages.error(request, ' Disease not added successfully')  
          return redirect('index')
     else:
          form = f.DiseaseForm()
          context = {
                    'form': form,
               }
     return render(request, 'crop/add_disease.html', context)

def addSolution(request):

     if request.method == "POST":
          form =f.SolutionForm(request.POST)
          
          if form.is_valid():
               # data = form.save(commit=False)
               # data.user = request.user
               form.save()
               messages.success(request, ' Solution added successfully')
          else:
               messages.error(request, ' Solution not added successfully')  
          return redirect('index')
     else:
          form = f.SolutionForm()
          context = {
                    'form': form,
               }
     return render(request, 'crop/add_solution.html', context)


def addProfile(request):

     if request.method == "POST":
          try:
               profile = m.Profile.objects.get(user__id=request.user.id)
               form =f.ProfileForm(request.POST, instance = profile)
          except:
               form =f.ProfileForm(request.POST)
          if form.is_valid():
               data = form.save(commit=False)
               data.user = request.user
               data.save()
               messages.success(request, ' Solution added successfully')
          else:
               messages.error(request, ' Solution not added successfully')  
          return redirect('index')
     else:
          try:
               profile = m.Profile.objects.get(user__id=request.user.id)
               form = f.ProfileForm(instance = profile)
          except:
               form = f.ProfileForm()

          context = {
                    'form': form,
               }
     return render(request, 'crop/add_profile.html', context)


def event(request):

     if request.method == "POST":
          form =f.EventForm(request.POST)
          
          if form.is_valid():
               data = form.save(commit=False)
               user = m.Profile.objects.get(user__id=request.user.id)
               data.user = user
               data.save()
               messages.success(request, ' Event added successfully')
          else:
               messages.error(request, ' Event not added successfully')  
     
     form = f.EventForm()
     event = m.Event.objects.all()
     print(event)

     context = {
               'form': form,
               'event':event,
          }
     return render(request, 'crop/event.html', context)


def farmer(request):

     if request.method == "POST":
          form =f.ProductForm(request.POST)
          
          if form.is_valid():
               data = form.save(commit=False)
               user = m.Profile.objects.get(user__id=request.user.id)
               data.user = user
               data.save()
               messages.success(request, ' Product added successfully')
          else:
               messages.error(request, ' Product not added successfully')  
     
     form = f.ProductForm()
     product = m.Product.objects.all()

     context = {
               'form': form,
               'product':product,
          }
     return render(request, 'crop/farmer.html', context)

def buyer(request):

     if request.method == "POST":
          form =f.BuyerForm(request.POST)
          
          if form.is_valid():
               data = form.save(commit=False)
               user = m.Profile.objects.get(user__id=request.user.id)
               data.user = user
               data.save()
               messages.success(request, ' Buying product added successfully')
          else:
               messages.error(request, ' Buying product not added successfully')  
    
     form = f.BuyerForm()
     buyers = m.Buyer.objects.all()

     context = {
               'form': form,
               'buyer':buyers
          }
     return render(request, 'crop/buyer.html', context) 

def cropList(request):
     crop = m.Crop.objects.all()
     crop_filter = CropFilter(request.GET, queryset=crop)
     crop = crop_filter.qs
     context = {
          'crop':crop,
          'filter': crop_filter
     }
     return render(request, 'crop/crop_list.html', context)


def cropDetails(request, id):

     crop = m.Crop.objects.get(id=id)
     varity = m.Varity.objects.filter(crop__id=id)
     CropFilter
     
     context = {
          "crop":crop,
          'varity':varity
     }
     return render(request, 'crop/crop_details.html', context)

def preferedCrop(request):

     land = m.Land.objects.filter(user_id = request.user.id)
   
          # def Analysis(request):
     land = land[0]

     
     X, y = Build_Data_Set(land)
     print(X)
     crop = m.Crop.objects.filter(ph_min__lte=land.ph, 
          ph_max__gte=land.ph, 
          water__lte=land.water, 
          min_temp__lte=land.avg_temp, 
          max_temp__gte=land.avg_temp)
     clf = svm.SVC(kernel="linear", C= 1.0)
     clf.fit(X,y)
     
     
     data_df = pd.DataFrame.from_csv("crop_data.csv")
     
     
     

     X = np.array(data_df[features].values)
     print("X---", X)
     

     X = preprocessing.scale(X)
     print("Xpre---", X)

     # Z = data_df["id"].values.tolist()
     
     

     invest_list = []

     for i in range(len(X)):
          
          crop = clf.predict(X[i])[0]
          print("crop_prected---", crop)
          
          if crop == 1:
               
               crop.append(Z[i])
          
               

   
     context = {
          'crop':crop
     }
     return render(request, 'crop/pref_crop.html', context)




def Status_Calc(ph_min, ph_max ):

#count=0
    
     print(ph_min)
     print(ph_max)
     
     if ph<= ph_max and ph>= ph_min:        
          return 1
 
     else:
          return 0


def Build_Data_Set(land):

     global ph
     ph = land.ph
     global temp
     temp = land.avg_temp
     global water
     water = land.water




     data_df = pd.DataFrame.from_csv("crop_data.csv")
     print(data_df)


     data_df["Status2"] = list(map(Status_Calc, data_df["ph_min"], data_df["ph_max"]))

     X = np.array(data_df[features].values)
     y = (data_df["Status2"].values)
     print("y-----",y)
     X = preprocessing.scale(X)
          
     return X,y

def about(request):
     return render(request, 'crop/comingsoon.html')