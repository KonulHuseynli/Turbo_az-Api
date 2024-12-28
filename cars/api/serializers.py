from rest_framework import serializers

from cars.models import(
    Announcement,
    AnnouncementImage,
    Brand,
    CarModel,
    RoofType,
    Color,
    FuelType,
    EngineCapacity,
    ForCountry,
    CarSupply,
    GearBox
    
)

class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ('image',)
        
        
class CreateAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('user', 'car_supply','created_at','updated_at')

class ListBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class ListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        
class ListRoofTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoofType
        fields = '__all__'
        
class ListColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        
class ListFuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'
        
class ListEngineCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineCapacity
        fields = '__all__'
              

class ListForCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForCountry
        fields = '__all__'
              
class ListCarSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSupply
        fields = '__all__'
              
class ListGearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearBox
        fields = '__all__'
              
