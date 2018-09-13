from rest_framework import serializers
from .models import customer,c_review,p_review,product,login,category,super_user

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=customer
        fields=('first_name','last_name','email','phone','address','blacklist')

class C_reviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=c_review
        fields=('rating' ,'text' ,'c_id ')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=product
        fields=('p_id','title','quantity','description','c_id','cat_id')
class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=login
        fields=('username','password','email','created','modified','c_id')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=category
        fields=('name')


class P_reviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=p_review
        fields =('rating','text','pro_id')

class Super_UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=super_user
        fields=('username','a_id')
