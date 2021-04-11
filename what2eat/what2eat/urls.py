from django.urls import include, path
from django.views.defaults import page_not_found
from rest_framework import routers
from .views import FoodView, UserViewSet, GroupViewSet, RegisterView
from . import views

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/groups', GroupViewSet)

def page_not_found_custom(request):
    return page_not_found(request, None)

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/food/', FoodView.as_view()),
    # path('api/food/',views.food_list),
    # path('api/food/<int:pk>/',views.food_detail()),
    path('', include(router.urls))
]

