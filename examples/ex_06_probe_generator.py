"""
Probe generator
--------------------------

probeinterface have also basic function to generate simple electrode layout like:

  * tetrode
  * linear probe
  * multi column probe

"""

##############################################################################
# Import

import numpy as np
import matplotlib.pyplot as plt

from probeinterface import Probe, ProbeBunch
from probeinterface.plotting import plot_probe, plot_probe_bunch


##############################################################################
# Generate 4 tetrode
# 

from probeinterface import generate_tetrode

probebunch = ProbeBunch()
for i in range(4):
    tetrode = generate_tetrode()
    tetrode.move([i*50, 0])
    probebunch.add_probe(tetrode)
probebunch.set_global_device_channel_indices(np.arange(16))
plot_probe_bunch(probebunch, with_channel_index=True, same_axe=True)


##############################################################################
# Generate a linear probe
# 

from probeinterface import generate_linear_probe

linear_probe = generate_linear_probe(num_elec=16,  ypitch=20)
plot_probe(linear_probe, with_channel_index=True)



##############################################################################
# Generate a multicolumn probe
# 

from probeinterface import generate_multi_columns_probe

multi_columns = generate_multi_columns_probe(num_columns=3,
            num_elec_per_column=[10, 12, 10],
            xpitch=22, ypitch=20,
            y_shift_per_column=[0, -10, 0],
            electrode_shapes='square', electrode_shape_params={'width': 12})
plot_probe(multi_columns, with_channel_index=True,)

##############################################################################
# Generate a square probe
# 

square_probe = generate_multi_columns_probe(num_columns=12,
            num_elec_per_column=12,
            xpitch=10, ypitch=10,
            electrode_shapes='square', electrode_shape_params={'width': 8})
square_probe.create_auto_shape('rect')
plot_probe(square_probe)



plt.show()




