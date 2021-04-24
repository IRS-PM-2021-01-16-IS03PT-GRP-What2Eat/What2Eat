import rules
import pandas as pd

df = pd.read_csv('category_rules.csv')



healthy = []

carnivorous = []

extravagant = []

scorching = []

rainy = []


def main():
        
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
        
    return print(selection)


main()