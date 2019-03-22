from django import forms
import django_filters
from django_filters.widgets import RangeWidget
import crop.models as m
from django_select2.forms import ModelSelect2TagWidget


class CropFilter(django_filters.FilterSet):
    soil_type__name=django_filters.ModelMultipleChoiceFilter(queryset=m.SoilType.objects.all(), label='Soil Type',  widget=forms.SelectMultiple(attrs={'class':'modelselect'}))
    name = django_filters.ModelMultipleChoiceFilter(queryset=m.Crop.objects.all(), label='Name', widget=forms.SelectMultiple(attrs={'class':'dealerselect'}))
    class Meta:
        model = m.Crop
        fields = [ 'name', 'soil_type__name']