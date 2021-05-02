#!/usr/bin/env python3
# -*- coding: utf-8 -*-




#Used to append user_rating
def unique_user(df):
    x=0
    for i in range(len(df)):
        x += df.iloc[i]
    return (x/len(df))

#Insert User Rating as 10001 as recipe_id and input ratings
def update_ratings(df,rating):
    for i in range(len(df)):
        for j in range(len(rating)):
            if(df.index[i]==rating.index[j]):
                df.iloc[i] = df.iloc[i] * int(rating.iloc[j])
            else:
                continue

    user_rating = df.loc[rating.index]
    print("user_rating")
    print(user_rating)
    user = unique_user(user_rating)
    user = user.rename('10001')
    return df, user