# fc_rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def is_healthy(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Vegetable', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'Meat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'Fruit', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'Carbs', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('facts', 'healthy',
                                   (rule.pattern(0).as_data(context),
                                    rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_carnivore(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Meat', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'Meat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'carnivore',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def is_vegetarian(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Vegetable', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'Vegetable', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'vegetarian',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_rules')
  
  fc_rule.fc_rule('is_healthy', This_rule_base, is_healthy,
    (('facts', 'Vegetable',
      (contexts.variable('x'),),
      False),
     ('facts', 'Meat',
      (contexts.variable('y'),),
      False),
     ('facts', 'Fruit',
      (contexts.variable('z'),),
      False),
     ('facts', 'Carbs',
      (contexts.variable('w'),),
      False),),
    (contexts.variable('recipe'),
     pattern.pattern_tuple((contexts.variable('w'), contexts.variable('x'), contexts.variable('y'), contexts.variable('z'),), None),))
  
  fc_rule.fc_rule('is_carnivore', This_rule_base, is_carnivore,
    (('facts', 'Meat',
      (contexts.variable('x'),),
      False),
     ('facts', 'Meat',
      (contexts.variable('y'),),
      False),),
    (contexts.variable('recipe'),
     pattern.pattern_tuple((contexts.variable('x'), contexts.variable('y'),), None),))
  
  fc_rule.fc_rule('is_vegetarian', This_rule_base, is_vegetarian,
    (('facts', 'Vegetable',
      (contexts.variable('x'),),
      False),
     ('facts', 'Vegetable',
      (contexts.variable('y'),),
      False),),
    (contexts.variable('recipe'),
     pattern.pattern_tuple((contexts.variable('x'), contexts.variable('y'),), None),))


Krb_filename = '../fc_rules.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 21), (4, 4)),
    ((22, 26), (5, 5)),
    ((27, 31), (6, 6)),
    ((32, 34), (8, 8)),
    ((43, 47), (12, 12)),
    ((48, 52), (13, 13)),
    ((53, 55), (15, 15)),
    ((64, 68), (20, 20)),
    ((69, 73), (21, 21)),
    ((74, 76), (23, 23)),
)
