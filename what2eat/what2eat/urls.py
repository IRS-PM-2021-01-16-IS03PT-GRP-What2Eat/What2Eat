from django.urls import include, path
from django.views.defaults import page_not_found
from rest_framework import routers
from .views import FoodViewSet, UserViewSet, GroupViewSet, RegisterView
from . import views

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/groups', GroupViewSet)
router.register(r'api/food',  FoodViewSet)

def page_not_found_custom(request):
    return page_not_found(request, None)

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    # this just to block the /food list path as it is not necessary
    # path('api/food/',page_not_found_custom),
    path('api/food/',views.food_list),
  #  path('api/food/<int:pk>',views.food_detail()),
    path('', include(router.urls))
]

