from django.db import models


# class Food(models.Model):
#     title = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200,blank=False, default='')
#     ingredients = models.CharField(max_length=500, blank=False, default='')
#     link = models.CharField(max_length=100, blank=False, default='')
#     methods = models.CharField(max_length=500, blank=False, default='')
#     thumbnail = models.CharField(max_length=100,blank=False, default='')

class Food (models.Model):
    recipe_id = models.IntegerField(blank=False, default=0, primary_key=True)
    recipe_name = models.TextField(blank=False, default='')
    image_url = models.TextField(blank=False, default='')
    ingredients = models.TextField(blank=False, default='')
    methods = models.TextField(blank=False, default='')

    def __str__(self):
        return self.recipe_id

class FoodRatings(models.Model):
    username = models.CharField(blank=False, max_length=150, default='')
    ratings = models.IntegerField(blank=False, default=0)
    fooditem_id = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.username

class Registration(models.Model):
    userid = models.IntegerField(blank=False, default=0)
    fooditem = models.ForeignKey(Food, on_delete=models.CASCADE)
    ratings = models.IntegerField(blank=False, default=0)


