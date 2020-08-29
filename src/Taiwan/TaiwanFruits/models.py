from django.db import models

# Create your models here.
class Fruits(models.Model):
    title = models.CharField(max_length =120)
    description= models.TextField(blank =True,null=True)
    price = models.DecimalField(decimal_places = 2,max_digits =100)
    summary = models.TextField(blank=False, null=True)
    featured = models.BooleanField()
    '''
    Name        = models.CharField(  blank = True,max_length = 120)  # max_length required
    origin      = models.CharField(  blank = True, max_length = 100)
    price_per_pound = models.DecimalField(decimal_places = 2, max_digits = 1000)
    price_each = models.IntegerField(default = 100)
    
    description = models.TextField(blank = True,null = True)
    date = models.DateField(auto_now = True, auto_now_add= False)
    certificate = models.FileField(blank = True, upload_to = 'uploads/')
    image = models.ImageField(blank = True, upload_to = 'uploads/')
    '''