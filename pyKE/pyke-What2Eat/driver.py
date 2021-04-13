from pyke import knowledge_engine
import pandas as pd

recipe = pd.read_csv("/home/ai-user/Downloads/Practice Module_RS_materials/pyke-What2Eat/What2Eat_Pivot.csv")

engine = None
# Compile and load .krb files in same directory (recursively).


    
def is_healthy(df,option,vegetable,meat,fruit):
    global engine
    engine = knowledge_engine.engine(__file__)
    
    engine.reset()
    engine.activate("fc_rules")  # Runs all applicable forward-chaining rules.
    
    

    try:
        for i in range(len(df['Title'])):
            rowdata= df.iloc[i]
            print(rowdata)
            vegetable = vegetable.iloc[i]
            print(vegetable)
            meat = meat.iloc[i]
            print(meat)
            fruit = fruit.iloc[i]
            print(fruit)
            vals,plan = engine.prove_1_goal('fc_rules.return_recipe($df,$option,$vegetable,$meat,$fruit)',df=rowdata,option=option,vegetable=vegetable,meat=meat,fruit=fruit)
            
            return print(vals['df'])
    except knowledge_engine.CanNotProve:
        print("Error at healthy") 


# def is_carnivore():
#     engine.reset()
#     engine.activate("fc_rules")  # Runs all applicable forward-chaining rules.

#     try:
#         vars = engine.prove_1_goal("facts.is_carnivore($recipe)",recipe=recipe)
#         return vars(recipe)
#     except:
#         print("Error at carnivore")

# def is_vegetarian():
#     engine.reset()
#     engine.activate("fc_rules")  # Runs all applicable forward-chaining rules.

#     try:
#         vars = engine.prove_1_goal("facts.is_vegetarian($recipe)",recipe=recipe)
#         return vars(recipe)
#     except:
#         print("Error at vegetarian")


def main():
    
    
   
    is_healthy(recipe,'healthy',recipe['Vegetable'],recipe['Meat'],recipe['Fruits'])
    
    # is_carnivore()
    # is_vegetarian()
    # x = input("Please Pick Your Preference:\n1. Healthy\n2. Carnivore\n3. Vegetarian\n")
    # if x == 1:
    #     is_healthy()
    # elif x == 2:
    #     is_carnivore()
    # else:
    #     is_vegetarian()
    


main()