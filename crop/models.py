from django.db import models
from django.contrib.auth.models import User, Permission

# Create your models here.

class SoilType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)

class Sun(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)


class Land(models.Model):
    
    water = models.CharField(max_length=30)
    avg_temp = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    ph = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    soil_type = models.ForeignKey(SoilType,
        on_delete=models.CASCADE,
      
        
    )
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        
        
    )
    
    def __str__(self):
        return str(self.user.username)

class SoilTest(models.Model):
    ph =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    phosporus =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    potassium =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    nitrogen =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    sulfate =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    boron =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    copper =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    iron =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    zinc =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    magnesium =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    land = models.ForeignKey(Land,
        on_delete=models.CASCADE,
       
        
    )

    def __str__(self):
        return str(self.land)

class CropType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)

class Ph(models.Model):
    status = models.CharField(max_length=30)
    
    
    def __str__(self):
        return str(self.status)

class Crop(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    min_temp = models.IntegerField(blank=True, null=True)
    max_temp = models.IntegerField(blank=True, null=True)
    month_plant = models.IntegerField(blank=True, null=True)
    cultivation = models.TextField(blank=True, null=True)
    harvest = models.TextField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)

    
    soil_type = models.ForeignKey(SoilType,
        on_delete=models.CASCADE, blank=True, null=True
        
        
    )

    crop_type = models.ForeignKey(CropType,
        on_delete=models.CASCADE,blank=True, null=True
        
        
    )
    sun = models.ForeignKey(Sun,
        on_delete=models.CASCADE,blank=True, null=True
            
    )
    ph_min = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ph_max = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    ph = models.ForeignKey(Ph,
        on_delete=models.CASCADE,blank=True, null=True
            
    )
    
    def __str__(self):
        return str(self.name)

class Varity(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    min_temp = models.IntegerField(blank=True, null=True)
    max_temp = models.IntegerField(blank=True, null=True)
    month_plant = models.CharField(max_length=30, blank=True, null=True)
    cultivation = models.TextField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    harvest = models.TextField(blank=True, null=True)
    soil_type = models.ForeignKey(SoilType,
        on_delete=models.CASCADE,blank=True, null=True
        
        
    )
    sun = models.ForeignKey(Sun,
        on_delete=models.CASCADE, blank=True, null=True
            
    )
    crop = models.ForeignKey(Crop,
        on_delete=models.CASCADE, blank=True, null=True
        
        
    )
    def __str__(self):
        return str(self.name)


class Disease(models.Model):
    name = models.CharField(max_length=30)
    Symptoms = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    prevention = models.TextField(blank=True, null=True)
    crop = models.ForeignKey(Crop,
        on_delete=models.CASCADE,    
    )
    
    def __str__(self):
        return str(self.name)

class Solution(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    Procedure = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=30, blank=True, null=True)
    duration = models.CharField(max_length=30, blank=True, null=True)
    items = models.TextField(blank=True, null=True)
    disease = models.ForeignKey(Disease,
        on_delete=models.CASCADE,    
    )
    
    def __str__(self):
        return str(self.name)

class Zoning(models.Model):
    area = models.CharField(max_length=30)
    water = models.CharField(max_length=30)
    Subregion   = models.CharField(max_length=10)
    soil_type = models.ForeignKey(SoilType,
        on_delete=models.CASCADE,
      
        
    )
    
    def __str__(self):
        return str(self.area)



class Profile(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        
        
    )
    
    name = models.CharField(max_length=100,blank=True,
        null=True)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    alt_phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True,
        null=True)
    is_farmer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

   
    def __str__(self):
        return str(self.name)



class Product(models.Model):
    name = models.ForeignKey(Crop,
         on_delete=models.CASCADE,
        
    )
    quantity = models.IntegerField(blank=True, null=True)
    expected_price = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        
        
    )
    
    def __str__(self):
        return str(self.name)

class Buyer(models.Model):
    expected_product = models.ForeignKey(Crop,
         on_delete=models.CASCADE,
        
    )
    expected_price   = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(Profile,
        on_delete=models.CASCADE,
        
        
    )
    
    def __str__(self):
        return str(self.name)

class Event(models.Model):

    event_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.TextField()
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    user = models.ForeignKey(Profile,
        on_delete=models.CASCADE,
        
        
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.event_name)







# growing procedure month wise process tracking