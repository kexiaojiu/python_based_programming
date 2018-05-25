#!/usr/bin/env pythin3
#~ ### part 1
#~ import printing_functions

#~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#~ completed_models = []

#~ printing_functions.print_models(unprinted_designs, completed_models)
#~ printing_functions.show_completed_models(completed_models)


#~ ### part 2
#~ from printing_functions import print_models,show_completed_models

#~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#~ completed_models = []

#~ print_models(unprinted_designs, completed_models)
#~ show_completed_models(completed_models)


#~ ### part 3
#~ from printing_functions import print_models as pm, show_completed_models as sm

#~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#~ completed_models = []

#~ pm(unprinted_designs, completed_models)
#~ sm(completed_models)


#~ ### part 4
#~ import printing_functions as pf

#~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#~ completed_models = []

#~ pf.print_models(unprinted_designs, completed_models)
#~ pf.show_completed_models(completed_models)

### part 5
from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
