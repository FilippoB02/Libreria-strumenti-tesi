"""
code for instrument instruction
13 03 2026
arbitrary function generator
"""

import numpy as np
import pyvisa
from TektronixDPO2024B import DPO2024B
import time
import matplotlib.pyplot as plt


"""
rm = pyvisa.ResourceManager()
print(rm.list_resources())
"""

# definisco il mio strumento
osc = DPO2024B('USB0::0x0699::0x03A3::C020036::INSTR', verbose=True)
# forse 'USB0::0x0699::0x03A3::C020036::INSTR'

# altro strumento scope = TBS2204B('USB0::0x0699::0x03A3::C020036::INSTR', verbose=True)

#scope = TBS2204B.TBS2204B('USB0::0x0699::0x03A3::C020036::INSTR', verbose=True)

# parametri
num_ch = 1
probe_ch = 2

# lo ho connesso / inizializzato

osc.idn()
osc.clear()
osc.reset()
osc.autoset()
osc.set_record_length(100000)

# lo ho anche resettato e pulito

#channel settings OUTPUT
#osc.set_channel_display(num_ch, False)
#osc.set_channel_coupling(num_ch, "DC")
#osc.set_channel_position(num_ch, 0)
#osc.set_channel_gain(num_ch, 1)
#osc.set_channel_scale(num_ch, 1)

#channel settings probe
osc.set_channel_display(probe_ch, True)
osc.set_channel_coupling(probe_ch, "DC")
osc.set_channel_position(probe_ch, 0)
osc.set_channel_gain(probe_ch, 0.1)
osc.set_channel_scale(probe_ch, 20)

#timebase settings
osc.set_timebase_scale(40e-09)

osc.set_timebase_position(20)


#trigger settings
osc.set_trigger_mode('AUTO')
osc.set_trigger_source(probe_ch)
osc.set_trigger_level(0)
osc.set_trigger_slope('RISE')


time.sleep(5)
t, v = osc.get_waveform(probe_ch)

#from s to ns
t = t * 1e9

osc.close()

#df = pd.DataFrame({"x": t, "y":v})
#df.to_csv('dati/Rf30k/dati_30k_1MHz_6V_100pF.csv', index=False)

"""
plt.plot(t, v, label='output')
plt.xlabel("Tempo [ns]")
plt.ylabel("Tensione [V]")
plt.grid(True)
plt.legend()
plt.show()
"""