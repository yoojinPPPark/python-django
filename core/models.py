from django.db import models
from django.contrib.postgres.fields import ArrayField 
from jsonfield import JSONField
#pip3 install jsonfield

#create models here
class Cocktailbar_cocktail(models.Model):
    cocktailbar_id = models.CharField(max_length=15)
    cocktail_id = models.IntegerField()
    popularity_coctail = models.BooleanField
    cocktail_korname = models.CharField
    cocktail_engname = models.CharField
    cocktail_img_for_order = models.ImageField(blank=True, null=True, upload_to='cocktail')
    coctail_alchol_degree = models.IntegerField()
    cocktail_description = models.TextField
    cocktail_ingredients = ArrayField(models.CharField(max_length=20), blank=True) 
    cocktail_price = models.CharField
    
    def __str__(self):
        return self.cocktail_id
    
    
    
class Order(models.Model):
    order_num = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    client_id = models.CharField(max_length=15)
    client_cocktail = models.CharField(max_length=15)
    client_detail_customizing = models.JSONField()
    order_check = models.BooleanField
    def __str__(self):
        return self.order_check
    
    
class Community(models.Model):
    community_id = models.IntegerField()
    community_title = models.CharField(max_length=100)
    community_client_name = models.CharField(max_length=20)
    community_date = models.DateTimeField(auto_now_add=True)
    community_contents  = models.TextField
    def __str__(self):
        return self.community_id
    
    
class Cocktionary(models.Model):
    cocktail_id = models.IntegerField()
    cocktail_korname = models.CharField(max_length=100)
    cocktail_engname = models.CharField(max_length=100)
    cocktail_img = models.ImageField(blank=True, null=True, upload_to='cocktail')
    def __str__(self):
        return self.cocktail_id
