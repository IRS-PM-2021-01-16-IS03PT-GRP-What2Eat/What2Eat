#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('/home/ai-user/Downloads/Practice Module_RS_materials/rulebase-What2Eat/What2Eat_Ingredient_count.csv')

healthy = []

carnivorous = []

extravagant = []

scorching = []

rainy = []



def is_healthy(df):
    for i in range(len(df['Title'])):
        if ((df['Vegetable'][i]>1)&(df['Meat'][i]>1)&(df['Fruits'][i]>1)&(df['Carbs'][i]>1)):
            healthy.append(df['Title'][i])
        else:
            continue
    return healthy
        

def is_carnivorous(df):
    for i in range(len(df['Title'])):
        if ((df['Meat'][i]>2)&(df['Carbs'][i]>1)):
            carnivorous.append(df['Title'][i])
        else:
            continue
    return carnivorous

def is_scorching(df):
    for i in range(len(df['Title'])):
        # if ((df['Fruits'][i]>3)or(df['Spicy'][i]>1)):
        #     scorching.append(df['Title'][i])
        # else:
        #     continue
        if ((df['Fruits'][i]>3)):
            scorching.append(df['Title'][i])
        else:
            continue
    return scorching


def is_rainy(df):
    for i in range(len(df['Title'])):
        # if ((df['Carbs'][i]>3)or(df['Soupbase'][i]>1)):
        #     rainy.append(df['Title'][i])
        # else:
        #     continue
        if ((df['Carbs'][i]>3)):
            rainy.append(df['Title'][i])
        else:
            continue
    return rainy


def main():
    is_healthy(df)
    is_carnivorous(df)
    is_scorching(df)
    is_rainy(df)
    print('Healhty Recipes are {}\n'.format(is_healthy(df)))
    print('Carnivorous Recipes are {}\n'.format(is_carnivorous(df)))
    print('Scorching Recipes are {}\n'.format(is_scorching(df)))
    print('Rainy Recipes are {}\n'.format(is_rainy(df)))
    
main()

