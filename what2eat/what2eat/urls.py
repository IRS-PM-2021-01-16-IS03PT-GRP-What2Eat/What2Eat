from django.urls import include, path
from django.views.defaults import page_not_found
from rest_framework import routers
from .views import InitialFoodRatingListView, UserViewSet, GroupViewSet, RegisterView, FoodRatingsView, RecommendListView
from . import views

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/groups', GroupViewSet)

def page_not_found_custom(request):
    return page_not_found(request, None)

urlpatterns = [
 #   path('api/register/', RegisterView.as_view()),
    path('api/foodratings/', FoodRatingsView.as_view()),
    path('api/food/', InitialFoodRatingListView.as_view()),
    path('api/register/initialFoodRating/',InitialFoodRatingListView.as_view()),
    path('api/dailyRecommend/',views.recommendList),
    path('api/register/saveInitialRating/',views.saveInitialRating),
    path('', include(router.urls))
]

