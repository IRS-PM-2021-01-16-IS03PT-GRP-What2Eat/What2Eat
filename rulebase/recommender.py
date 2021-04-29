import pandas as pd
from scipy.spatial.distance import cosine
from sklearn.preprocessing import normalize





#Insert User Rating as 10001 as recipe_id and input ratings
def filter_recipe(df,user_rating,recipe_list):
    
    df = df[df.index.isin(recipe_list)]
    
    df = df.append(user_rating)
    df = df.apply(pd.to_numeric)
    df_normalized = pd.DataFrame(normalize(df, axis=0))
    df_normalized.columns = df.columns
    df_normalized.index = df.index
    return df_normalized


def ingredient_recommender(df_normalized,distance_method, recipe_id, N):

    allRecipes = pd.DataFrame(df_normalized.index)
    allRecipes = allRecipes[allRecipes.recipe_id != recipe_id]
    allRecipes["distance"] = allRecipes["recipe_id"].apply(lambda x: distance_method(df_normalized.loc[recipe_id], df_normalized.loc[x]))
    TopNRecommendation = allRecipes.sort_values(["distance"]).head(N).sort_values(by=['distance', 'recipe_id'])
    # sort by distance then recipe id, the smaller value of recipe id will be picked. 
    return TopNRecommendation['recipe_id']

# df_normalized = filter_recipe(df, rating, recipe_list)
# print(ingredient_recommender(cosine, '10001', 3))