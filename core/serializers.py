from rest_framework import serializers
from models import Cocktailbar_cocktail, Order, Community, Cocktionary


class Cocktailbar_cocktail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktailbar_cocktail
        fields = ('id', 'cocktailbar_id','cocktail_id','popularity_coctail','cocktail_korname','cocktail_engname','cocktail_img_for_order','coctail_alchol_degree','cocktail_description','cocktail_ingredients' ,'cocktail_price')

    
    
class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_num','order_time','client_id','client_cocktail','client_detail_customizing','order_check')

    

class Community_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('community_id','community_title','community_client_name','community_date','community_contents')

    
    
class Cocktionary_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktionary
        fields = ('cocktail_id','cocktail_korname','cocktail_engname','cocktail_img')
