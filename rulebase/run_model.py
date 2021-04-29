import rules
import pandas as pd
from scipy.spatial.distance import cosine
from recommender import filter_recipe,ingredient_recommender
from update_ratings import update_ratings

#Standard Files
df = pd.read_csv('category_rules.csv')
raw_df = pd.read_csv('recipe_ingredient_availability.csv',index_col=0)



#Parse Rating List
rating = pd.read_csv('ratings.csv',index_col=(0))



def recipe_rule(df):
        
    x = input('Please select Category\n')
    selection = []
    
    if (x == '1'):
        
        selection = rules.is_healthy(df)
        
    elif (x == '2'):
       
        selection =  rules.is_carnivorous(df)
        
    elif (x == '3'):
        
        selection = rules.is_scorching(df)
        
    elif (x == '4'):
        
        selection = rules.is_rainy(df)
        
    elif (x == '5'):
        selection = rules.is_surprise(df)
        
    else:
        print('Please select again ! ')
        
    return selection


def main():
    recipe = recipe_rule(df)
    update_df,user_rating = update_ratings(raw_df,rating)
    df_normalize = filter_recipe(update_df,user_rating,recipe)
    recommended_recipes = ingredient_recommender(df_normalize,cosine, '10001', 6)
    return print(recommended_recipes)
    
main()