from django.urls import include, path
from django.views.defaults import page_not_found
from rest_framework import routers
from .views import FoodViewSet,UserViewSet,GroupViewSet

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/groups', GroupViewSet)
router.register(r'api/food',  FoodViewSet)

def page_not_found_custom(request):
    return page_not_found(request, None)

urlpatterns = [
    path('api/food/',page_not_found_custom),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

