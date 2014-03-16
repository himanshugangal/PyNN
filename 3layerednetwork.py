"""
Simple 3 layered network model where both excitatory and inhibitory time based spike source is fed into 3 neurons , the voltage travels through a mediating layer of 50 neurons and finally goes into a layer of 100 neurons to give the desired output 
""" 



from pyNN.utility import get_script_args
from pyNN.errors import RecordingError

simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)

seed = 764756387

setup(timestep=0.1,min_delay=0.1,max_delay=4.0)

N = 153 
N1 = 3 
N2 = 50 
N3 = 100 
seed = 764756387
rng = NumpyRNG(seed=seed, parallel_safe=True) 

cell_params = {'tau_refrac':2.0,'v_thresh':-50.0,'tau_syn_E':2.0, 'tau_syn_I':2.0}
output_population = Population(N3, IF_curr_alpha, cell_params, label="output")
input_population = Population(N1, IF_curr_alpha, cell_params, label="input")
mediate_population = Population(N2, IF_curr_alpha, cell_params, label="mediate")

spike_sourceE = create(SpikeSourceArray, {'spike_times': [float(i) for i in range(5,105,10)]})
spike_sourceI = create(SpikeSourceArray, {'spike_times': [float(i) for i in range(155,255,10)]})

connE = connect(spike_sourceE, input_population, weight=0.006, synapse_type='excitatory',delay=2.0)
connI = connect(spike_sourceI, input_population, weight=-0.02, synapse_type ='inhibitory',delay=4.0)
    
connector = FixedProbabilityConnector(0.5, weights=1.0)
projection1 = Projection(input_population, mediate_population, connector, rng=rng)
projection2 = Projection(mediate_population, output_population, connector, rng=rng)



run(200.0)

end()
