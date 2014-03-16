
"""
Simple I&F neuron fed with DC current 

""" 



from pyNN.utility import get_script_args
from pyNN.errors import RecordingError

simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)

setup(timestep=0.1,min_delay=0.1,max_delay=4.0)

ifcell = create(IF_cond_exp, {  'i_offset' : 0.1,    'tau_refrac' : 3.0,
                                'v_thresh' : -51.0,  'tau_syn_E'  : 2.0,
                                'tau_syn_I': 5.0,    'v_reset'    : -70.0,
                                'e_rev_E'  : 0.,     'e_rev_I'    : -80.})
pulse = DCSource(amplitude=0.5,start=5.0,stop=10.0)
ifcell.inject(pulse) 
ifcell.record()

run(200.0)

end()
