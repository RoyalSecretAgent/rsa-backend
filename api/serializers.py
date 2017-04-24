from .models import Account,Achievements,Book,Barbarian,Culture
from rest_framework import serializers, permissions

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Account
        fields = '__all__'

class AchievementsSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
         models = Achievements
         fields = '__all__'

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Book
        fields = '__all__'

class BarbarianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Barbarian
        fields = '__all__'

class CultureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Culture
        fields = '__all__'