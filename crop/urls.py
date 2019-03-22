from django.conf.urls import  url
from . import views

app_name = "crop"

urlpatterns = [
	url(r'^add-land$', views.addland, name='add_land' ),
	url(r'^add_crop$', views.addCrop, name='add_crop' ),
	url(r'^add_varity$', views.addVarity, name='add_varity' ),
	url(r'^add_disease$', views.addDisease, name='add_disease' ),
	url(r'^add_solution$', views.addSolution, name='add_solution' ),
	url(r'^add-soiltest/$', views.addSoilTest, name='add_soiltest'),
	url(r'^add_profile$', views.addProfile, name='add_profile' ),
	url(r'^product$', views.farmer, name='product' ),
	url(r'^buyer$', views.buyer, name='buyer' ),
	url(r'^event$', views.event, name='event' ),
	url(r'^about$', views.about, name='about' ),
	
	url(r'^crop_list/$', views.cropList, name='crop_list'),
	url(r'^prefered_crop/$', views.preferedCrop, name='prefered_crop'),
	url(r'^(?P<id>\d+)/crop_details/$', views.cropDetails, name='crop_details' ),


]

