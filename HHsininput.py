
"""
Simple HH cell , fed with AC current source  

""" 


from pyNN.utility import get_script_args
from pyNN.errors import RecordingError

simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)


setup(timestep=0.1,min_delay=0.1,max_delay=4.0)

HHcell = create(HH_cond_exp)
current = ACSource(start = 50,stop = 200 , amplitude = 2,frequency = 200 , phase = 30  )
HHcell.inject(current)


run(200.0)

end()
