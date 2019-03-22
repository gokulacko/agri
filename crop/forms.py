import crop.models as m
from django import forms
from django.forms import widgets

class LandForm(forms.ModelForm):
	class Meta:
		model = m.Land
		fields = [
			# 'area',
			'water',
			'avg_temp',
            'pincode',
            'soil_type',
			'ph',
            # 'user'
		]

class SoilForm(forms.ModelForm):
	class Meta:
		model = m.SoilTest
		fields = [
			'ph',
			'phosporus',
			'potassium',
            'nitrogen',
            'sulfate',
            'boron',
            'copper',
			'iron',
			'zinc',
            'magnesium',
            'land',
            
		]
 

class CropForm(forms.ModelForm):
	class Meta:
		model = m.Crop
		fields = '__all__'
 
class VarityForm(forms.ModelForm):
	class Meta:
		model = m.Varity
		fields = '__all__'

class DiseaseForm(forms.ModelForm):
	class Meta:
		model = m.Disease
		fields = '__all__'

class SolutionForm(forms.ModelForm):
	class Meta:
		model = m.Solution
		fields = '__all__'
 

class ProfileForm(forms.ModelForm):
	class Meta:
		model = m.Profile
		fields = [
			'name',
			'area',
			'city',
            'pincode',
            'address',
            'phone',
            'alt_phone',
			'is_farmer',
			'is_buyer',
            
		]

class ProductForm(forms.ModelForm):
	class Meta:
		model = m.Product
		fields = [
			'name',
			'quantity',
			'expected_price',
            
		]

class BuyerForm(forms.ModelForm):
	class Meta:
		model = m.Buyer
		fields = [
			'expected_product',
			'quantity',
			'expected_price',
            
		]

class EventForm(forms.ModelForm):
	class Meta:
		model = m.Event
		fields = [
			'event_name',
			'description',
			'location',
            'date',
			'time',
            
		]