import os

from .rules import is_healthy, is_carnivorous, is_scorching, is_rainy, is_surprise
import pandas as pd
from scipy.spatial.distance import cosine
from .recommender import filter_recipe, ingredient_recommender
from .update_ratings import *

#Standard Files
category_csv_path = os.path.join(os.path.dirname(__file__), 'category_rules.csv')
recipe_ingredient_aval_csv_path = os.path.join(os.path.dirname(__file__), 'recipe_ingredient_availability.csv')

df = pd.read_csv(category_csv_path)
raw_df = pd.read_csv(recipe_ingredient_aval_csv_path,index_col=0)



# Parse Rating List, used for testing
# rating_csv_path = os.path.join(os.path.dirname(__file__), 'ratings.csv')
# rating =  pd.read_csv(rating_csv_path,index_col=(0)) #To be replaced with ratings input




def recipe_rule(df,choice):

    selection = []

    if (choice == 1):
        print("is_healthy")
        selection = is_healthy(df)
        
    elif (choice == 2):
       
        selection =  is_carnivorous(df)
        
    elif (choice == 3):
        
        selection = is_scorching(df)
        
    elif (choice == 4):
        
        selection = is_rainy(df)
        
    elif (choice == 5):
        selection = is_surprise(df)
        
    else:
        print('Please select again ! ')

    return selection

class runModel:
    def getRecommendedRecipes(self, choice, ratings):
        print ("inside getRecommendedRecipes")
        print(choice);
        print(ratings);
        print("rating json")
        ratings = ratings.set_index('recipe_id')
        recipe = recipe_rule(df, choice)
        update_df, user_rating = update_ratings(raw_df, ratings)
        df_normalize = filter_recipe(update_df, user_rating, recipe)
        recommended_recipes = ingredient_recommender(df_normalize, cosine, '10001', 6)
        print("recommended_recipes")
        print(recommended_recipes)
        return recommended_recipes

    def saveCustomerRating(self, rating):
        print ("inside saveCustomerRating")
        update_ratings(df, rating)
        print(rating);
