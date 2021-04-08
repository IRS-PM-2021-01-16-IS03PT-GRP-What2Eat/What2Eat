# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '/home/ai-user/Downloads/Practice Module_RS_materials', 'pyke-What2Eat/facts.kfb'):
           [1617895934.0036387, 'facts.fbc'],
         ('', '/home/ai-user/Downloads/Practice Module_RS_materials', 'pyke-What2Eat/fc_rules.krb'):
           [1617895934.011261, 'fc_rules_fc.py'],
        },
        compiler_version)

