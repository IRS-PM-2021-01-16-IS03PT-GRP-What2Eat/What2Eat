#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('category_rules.csv')

healthy = []

carnivorous = []

extravagant = []

scorching = []

rainy = []



def is_healthy(df):
    for i in range(len(df['recipe_id'])):
        if ((df['veg'][i]>1)&(df['meat'][i]>1)&(df['carbs'][i]>1)):
            healthy.append(df['recipe_id'][i])
        else:
            continue
    return healthy
        

def is_carnivorous(df):
    for i in range(len(df['recipe_id'])):
        if ((df['meat'][i]>1)&(df['carbs'][i]>1)):
            carnivorous.append(df['recipe_id'][i])
        else:
            continue
    return carnivorous

def is_scorching(df):
    for i in range(len(df['recipe_id'])):
        if ((df['veg'][i]>3)or(df['dairy'][i]>1)):
            scorching.append(df['recipe_id'][i])
        else:
            continue
        
    return scorching


def is_rainy(df):
    for i in range(len(df['recipe_id'])):
        if ((df['carbs'][i]>2)or(df['veg'][i]>2)):
            rainy.append(df['recipe_id'][i])
        else:
            continue
        
    return rainy

def is_surprise(df):
    return df['recipe_id'].sample(n=10).to_list()






