from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import(
    MinLengthValidator,
    MaxValueValidator,
    MinValueValidator
)
from . import (
MILEAGE_CHOICES,
CURRENCY_CHOICES,
OWNER_CHOICES,
TRANSMİSSİON_CHOİCES,
NUMBER_OF_SEATS_CHOICES
)
from core.utils.models import TrackingModel

USER = get_user_model()

class Brand(models.Model):
    name = models.CharField(max_length=50)
    
class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=50)
    
class RoofType(models.Model): #Bannovu
    name = models.CharField(max_length=50)
    
class Color(models.Model):
    name = models.CharField(max_length=50)

class FuelType(models.Model): #Yanacaq novu
    name = models.CharField(max_length=50)

class EngineCapacity(models.Model): #Muherrik hecmi
    volume = models.CharField(max_length=10)

class ForCountry(models.Model): #Hansi bazar ucun yigilib
    name = models.CharField(max_length=50)

class CarSupply(models.Model): #Avtomobilin techizati
    name = models.CharField(max_length=50)

class GearBox(models.Model): #Suretler qutusu
    name = models.CharField(max_length=50)

class Announcement(TrackingModel):
    # user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='announcements')#Bezi hallarda circular import xetasi cixir
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='announcements')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='announcements')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='announcements')
    roof_type = models.ForeignKey(RoofType, on_delete=models.CASCADE, related_name='announcements')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='announcements')
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='announcements')
    engine_capacity = models.ForeignKey(EngineCapacity, on_delete=models.CASCADE, related_name='announcements')
    for_country = models.ForeignKey(ForCountry, on_delete=models.CASCADE, related_name='announcements')
    gear_box = models.ForeignKey(GearBox, on_delete=models.CASCADE, related_name='announcements')
    
    car_supply = models.ManyToManyField(CarSupply, related_name='announcement')

    #choices
    mileage_type = models.CharField(max_length=5, choices=MILEAGE_CHOICES)
    currency_type = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    owner_type = models.CharField(max_length=10, choices=OWNER_CHOICES)
    transmission_type = models.CharField(max_length=10, choices=TRANSMİSSİON_CHOİCES)
    seat_count = models.CharField(max_length=3, choices=NUMBER_OF_SEATS_CHOICES)
    
    #boolean fields--VEZIYYETI
    is_crashed = models.BooleanField(default=False) #Vurugu var
    is_damaged = models.BooleanField(default=False) #Qezali ve ya ehtiyat hisseler
    is_colored = models.BooleanField(default=False) #renglenib
    with_credit = models.BooleanField(default=False) #kreditle
    barter = models.BooleanField(default=False) #barter mumkundur
    
    #manual input
    mileage = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000000)])
    price = models.DecimalField(max_digits=8, decimal_places=0) #noqteden sonra reqem ucun limit teyin etmek olur 5.45(limit2)&& if decimal_fiels=2 -->999 999.99 noqteden sagda iki eded solda 6
    
    #DateField
    released_date = models.DateField() #Il
    engine_power = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10000)]) #muherrikin gucu

    vin_code = models.CharField(max_length=17, validators=[MinLengthValidator(17)])
    info = models.TextField(null=True, blank=True)
    
class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='announcements')
    