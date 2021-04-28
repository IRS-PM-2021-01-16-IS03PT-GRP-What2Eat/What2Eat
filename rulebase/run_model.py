import rules
import pandas as pd
from scipy.spatial.distance import cosine
from recommender import filter_recipe,ingredient_recommender

df = pd.read_csv('category_rules.csv')
raw_df = pd.read_csv('raw-data_recipe.csv')

rating = 3


healthy = []

carnivorous = []

extravagant = []

scorching = []

rainy = []


def recipe_rule():
        
    x = input('Please Select Category\ne.g.Healthy: 1\nCarnivours: 2\nScorching: 3\nRainy: 4\nSurprise Me: 5\n')
    x = int(x)
    if (x == 1):
        
        selection = rules.is_healthy(df)
        
    elif (x == 2):
       
        selection =  rules.is_carnivorous(df)
        
    elif (x == 3):
        
        selection = rules.is_scorching(df)
        
    elif (x == 4):
        
        selection = rules.is_rainy(df)
        
    elif (x == 5):
        selection = rules.is_surprise(df)
        
    else:
        print('Please select again ! ')
        
    return selection


def main():
    recipe = recipe_rule()
    df_normalize = filter_recipe(raw_df, rating, recipe)
    recommended_recipes = ingredient_recommender(df_normalize,cosine, '10001', 3)
    return print(recommended_recipes)
    
main()