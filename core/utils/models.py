from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)      #obj yarandigi anin tarixin qeyd edir
    updated_at = models.DateTimeField(auto_now=True)     #objin en sonuncu update olundugu tarixi goturur
    
    class Meta:
        abstract = True  #class-i migrate edende birbasa table kimi bazaya dusmur inheritance aldigimikz childclasslarda gorunecek. yeni meselen Car classiin daxilinde default olaraq created ve updated at gorunecek
    
    
