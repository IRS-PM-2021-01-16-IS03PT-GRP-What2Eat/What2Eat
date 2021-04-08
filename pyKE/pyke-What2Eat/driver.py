from pyke import knowledge_engine
import pandas as pd

recipe = pd.read_csv("/home/ai-user/Downloads/Practice Module_RS_materials/pyke-What2Eat/What2Eat_Pivot.csv")


# Compile and load .krb files in same directory (recursively).
engine = knowledge_engine.engine(__file__)

def print_fc_facts():
    '''
        This function runs the forward-chaining (rules.krb).
    '''
    engine.reset()
    engine.activate("fc_rules")  # Runs all applicable forward-chaining rules.

    # Print FC facts
    engine.get_kb("facts").dump_specific_facts()


def is_healthy():
    engine.reset()
    engine.activate("fc_rules")  # Runs all applicable forward-chaining rules.

    try:
        vars, plan = engine.prove_1_goal("facts.is_healthy($recipe)",recipe=recipe)
        return vars[recipe]
    except:
        print("{} is not healthy".format(recipe))


def is_carnivore():
    engine.reset()
    engine.activate("fc_rules")  # Runs all applicable forward-chaining rules.

    try:
        vars, plan = engine.prove_1_goal("facts.is_carnivore($recipe)",recipe=recipe)
        return vars[recipe]
    except:
        print("{} is not carnivore".format(recipe))

def is_vegetarian():
    engine.reset()
    engine.activate("fc_rules")  # Runs all applicable forward-chaining rules.

    try:
        vars, plan = engine.prove_1_goal("facts.is_vegetarian($recipe)",recipe=recipe)
        return vars[recipe]
    except:
        print("{} is not vegetarian".format(recipe))
    

def main():
    x = input("Please Pick Your Preference:\n1. Healthy\n2. Carnivore\n3. Vegetarian\n")
    if x == 1:
        is_healthy()
    elif x == 2:
        is_carnivore()
    else:
        is_vegetarian()
    


main()