from types import SimpleNamespace

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.decorators import api_view

from .serializers import UserSerializer, GroupSerializer, FoodSerializer, RegisterSerializer, FoodRatingSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from rest_framework.parsers  import JSONParser
from .models import Food, FoodRatings
from django.views.decorators.csrf import csrf_exempt
import random
import json
from .service import (what2EatService)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class InitialFoodRatingListView(generics.ListAPIView):
    def get_queryset(self):
        ingredient_row_total = Food.objects.all().count()
        slice = random.random() * (ingredient_row_total - 6)
        return Food.objects.all()[slice: slice + 6]

    queryset = get_queryset
    serializer_class = FoodSerializer
    permission_classes = []

class FoodRatingsView(generics.CreateAPIView):
    queryset = FoodRatings.objects.all()
    serializer_class = FoodRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = RegisterSerializer

class RecommendListView(generics.ListAPIView):
    def get_queryset(self):
        ingredient_row_total = Food.objects.all().count()
        random_list_of_6 = random.sample(range(1,ingredient_row_total+1), 6)
        return Food.objects.all().filter(pk__in=random_list_of_6)

    queryset = get_queryset
    serializer_class = FoodSerializer
    permission_classes = []


@api_view(['POST'])
def recommendList (request):
    if request.method == 'POST':
        print("inside post")
        choice = request.data.get("choice")
        print(choice)
        # TO-DO to call recommendation method
        service = what2EatService()
    #    recommended_recipes = service.getRecommendationList(choice)
        # below just temporary
        ingredient_row_total = Food.objects.all().count()
        slice = random.random() * (ingredient_row_total - 6)
        queryResult = Food.objects.all()[slice: slice + 6]
        print("after query")
        #print(queryResult)
        resultSerializer = FoodSerializer(queryResult, many=True)
        return JsonResponse(resultSerializer.data, safe=False)

@api_view(['POST'])
def saveInitialRating (request):
    if request.method == 'POST':
        print("inside saveInitialRating post")
        #print(request.data)

        uname = request.data.get("username")
        ratingJsonlist = request.data.get("foodRatingList")
        ratingStoreList = []
        print(ratingJsonlist)
        service = what2EatService()
        for i in ratingJsonlist:
            rate = FoodRatings(username = uname, fooditem_id=i.get("id"), ratings=i.get("rating"))
            ratingStoreList.append(rate)
            #service.saveCustomerRating(json.dumps({'recipe_id' : i.get("id"), 'rating': i.get("rating")}))
        print (ratingStoreList)
        #store into db
        FoodRatings.objects.bulk_create(ratingStoreList)
        return JsonResponse(data = "Success", status=200, safe=False)
        # print(x)
       # registrationDataSet = request.data.get("choice")
     #   print(choice)
        # TO-DO to call recommendation method
        # below just temporary
        # ingredient_row_total = Food.objects.all().count()
        # random_list_of_6 = random.sample(range(1, ingredient_row_total + 1), 6)
        # queryResult = Food.objects.all().filter(pk__in=random_list_of_6)
        # print("after query")
        # print(queryResult)
        # resultSerializer = FoodSerializer(queryResult, many=True)
        # return JsonResponse(resultSerializer.data, safe=False)

@api_view(['POST'])
def rateADish (request):
    if request.method == 'POST':
        print("inside rateADish post")
        print(request.data)
        ratingJsonlist = request.data.get("rates")
        rate = FoodRatings(username=ratingJsonlist.get("username"), fooditem_id=ratingJsonlist.get("id"), ratings=ratingJsonlist.get("rating"))
        print(rate)
        FoodRatings.save(rate)
        service = what2EatService()
        #service.saveCutomerRating(json.dumps({'recipe_id': ratingJsonlist.get("id"), 'rating': ratingJsonlist.get("rating")}))
        #to do to call rules


# @csrf_exempt
# def food_list (request):
#     if request.method == 'GET':
#         food = Food.objects.all()
#         serializer = FoodSerializer(food, many=True)
#         return JsonResponse(serializer.data, safe = False)
#
#     elif request == 'POST':
#         data = JSONParser.parse(request)
#         serializer = FoodSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# def food_detail (request, pk):
#     try:
#         food = Food.objects.get(pk=pk)
#     except Food.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = FoodSerializer(food)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = FoodSerializer(food, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         food.delete()
#         return HttpResponse(status=204)


