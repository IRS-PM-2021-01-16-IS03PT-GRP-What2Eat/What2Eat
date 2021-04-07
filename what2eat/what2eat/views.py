from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, FoodSerializer, RegisterSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers  import JSONParser
from .models import Food
from django.views.decorators.csrf import csrf_exempt


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

class FoodViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Food model
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = []
    http_method_names = ['get']

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = RegisterSerializer

@csrf_exempt
def food_list (request):
    if request.method == 'GET':
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request == 'POST':
        data = JSONParser.parse(request)
        serializer = FoodSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def food_detail (request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FoodSerializer(food, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        food.delete()
        return HttpResponse(status=204)


