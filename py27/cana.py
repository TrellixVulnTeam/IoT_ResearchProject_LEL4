
from __future__ import division
#import numpy as np
#from itertools import product
#from cana.control import fvs, mds, sc
from cana.datasets.bio import THALIANA
from IPython.display import display
from IPython.core.display import HTML

N = THALIANA()

display(HTML('<h3>Control State Transition Graph (CSTG)</h3>'))
# THIS MIGHT TAKE A LONG TIME, it is here for demo purposes.
driver_nodes = N.attractor_driver_nodes(min_dvs=1, max_dvs=6, verbose=True)
print N.get_node_name(driver_nodes)


# The FREQUENCY that two events has a certain temporal relationship