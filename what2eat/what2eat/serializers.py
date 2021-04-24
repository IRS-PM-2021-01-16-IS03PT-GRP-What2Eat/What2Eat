from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Food, FoodRatings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'title', 'description', 'ingredients', 'link', 'methods', 'thumbnail' ]

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[])

    class Meta:
        model = User
        fields = ['username', 'password']

    # https://www.django-rest-framework.org/api-guide/serializers/#saving-instances
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        # create one more object concurrently?
        return user

class FoodRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRatings
        fields = ['ratings','fooditem']

    def create(self, validated_data):
        foodratings = FoodRatings.objects.create(
            userid=self.context['request'].user.id,
            fooditem=validated_data['fooditem'],
            ratings=validated_data['ratings']
        )
        foodratings.save()
        return foodratings
