import crop.models as m
from django import forms
from django.forms import widgets

class LandForm(forms.ModelForm):

	water = forms.CharField(widget=forms.TextInput(attrs={'class': 'water', 'placeholder':'Water(Rate 0 to 10)'}))
	avg_temp = forms.CharField(widget=forms.TextInput(attrs={'class': 'avg_temp', 'placeholder':'Average Temperature(Celsius)'}))
	pincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'pincode', 'placeholder':'Pincode'}))
	# water = forms.CharField(widget=forms.TextInput(attrs={'class': 'water', 'placeholder':'Water(Rate 0 to 10)'}))

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

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name', 'placeholder':'Name:'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'description', 'placeholder':'Description:'}))
	duration = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'duration', 'placeholder':'Duration(In days):'}))
	min_temp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'min_temp', 'placeholder':'Minimun temperature(Celcius):'}))
	max_temp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'max_temp', 'placeholder':'Max Temperature(celcius):'}))
	month_plant = forms.CharField(widget=forms.TextInput(attrs={'class': 'month_plant', 'placeholder':'Time to Plant:'}))
	cultivation = forms.CharField(widget=forms.TextInput(attrs={'class': 'cultivation', 'placeholder':'Cultivation:'}))
	harvest = forms.CharField(widget=forms.Textarea(attrs={'class': 'harvest', 'placeholder':'Harvest:'}))
	water = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'water', 'placeholder':'Water(Rate 0 to 10):'}))
	ph_min = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'ph_min', 'placeholder':'Minimum Ph:'}))
	ph_min = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'ph_min', 'placeholder':'Minimum Ph:'}))

	class Meta:
		model = m.Crop
		fields = '__all__'
 
class VarityForm(forms.ModelForm):

	name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    min_temp = models.IntegerField(blank=True, null=True)
    max_temp = models.IntegerField(blank=True, null=True)
    month_plant = models.CharField(max_length=30, blank=True, null=True)
    cultivation = models.TextField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    harvest = models.TextField(blank=True, null=True)

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name', 'placeholder':'Name:'}))
	description = forms.Textarea(widget=forms.Textarea(attrs={'class': 'description', 'placeholder':'Description:'}))
	duration = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'duration', 'placeholder':'Duration(In days):'}))
	min_temp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'min_temp', 'placeholder':'Minimun temperature(Celcius):'}))
	max_temp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'max_temp', 'placeholder':'Max Temperature(celcius):'}))
	month_plant = forms.CharField(widget=forms.TextInput(attrs={'class': 'month_plant', 'placeholder':'Time to Plant:'}))
	cultivation = forms.CharField(widget=forms.TextInput(attrs={'class': 'cultivation', 'placeholder':'Cultivation:'}))
	harvest = forms.Textarea(widget=forms.Textarea(attrs={'class': 'harvest', 'placeholder':'Harvest:'}))
	water = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'water', 'placeholder':'Water(Rate 0 to 10):'}))

	class Meta:
		model = m.Varity
		fields = '__all__'

class DiseaseForm(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name', 'placeholder':'Name:'}))
	Symptoms = forms.Textarea(widget=forms.TextInput(attrs={'class': 'symptoms', 'placeholder':'Symptoms:'}))
	effect = forms.Textarea(widget=forms.TextInput(attrs={'class': 'effect', 'placeholder':'Effect:'}))
	prevention = forms.Textarea(widget=forms.TextInput(attrs={'class': 'prevention', 'placeholder':'Prevention:'}))



	class Meta:
		model = m.Disease
		fields = '__all__'

class SolutionForm(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name', 'placeholder':'Name:'}))
	Procedure = forms.Textarea(widget=forms.TextInput(attrs={'class': 'procedure', 'placeholder':'Procedure:'}))
	quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'quantity', 'placeholder':'Quantity:'}))
	duration = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'duration', 'placeholder':'Duration:'}))
	items = forms.Textarea(widget=forms.TextInput(attrs={'class': 'items', 'placeholder':'Items:'}))


	class Meta:
		model = m.Solution
		fields = '__all__'
 

class ProfileForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name', 'placeholder':'Name:'}))
	area = forms.CharField(widget=forms.TextInput(attrs={'class': 'area', 'placeholder':'Area:'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'class': 'city', 'placeholder':'City:'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone', 'placeholder':'Phone:'}))
	alt_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'alt_phone', 'placeholder':'Alternate Phone:'}))
	pincode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'pincode', 'placeholder':'Pincode:'}))
	address = forms.CharField(widget=forms.Textarea(attrs={'class': 'address', 'placeholder':'Address:'}))

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
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name', 'placeholder':'Name:'}))
	quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'quantity', 'placeholder':'Quantity:'}))
	expected_price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'expected_price', 'placeholder':'Expected price:'}))

	class Meta:
		model = m.Product
		fields = [
			'name',
			'quantity',
			'expected_price',
            
		]

class BuyerForm(forms.ModelForm):
	expected_product = forms.CharField(widget=forms.TextInput(attrs={'class': 'expected_product', 'placeholder':'Expected product:'}))
	quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'quantity', 'placeholder':'Quantity:'}))
	expected_price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'expected_price', 'placeholder':'Expected price:'}))

	class Meta:
		model = m.Buyer
		fields = [
			'expected_product',
			'quantity',
			'expected_price',
            
		]

class EventForm(forms.ModelForm):

	event_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'event_name', 'placeholder':'Event Name:'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'description', 'placeholder':'Description'}))
	location = forms.CharField(widget=forms.Textarea(attrs={'class': 'location', 'placeholder':'Location'}))
	# pincode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'pincode', 'placeholder':'Pincode'}))

	class Meta:
		model = m.Event
		fields = [
			'event_name',
			'description',
			'location',
            'date',
			'time',
            
		]