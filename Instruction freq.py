"""
# Metodo generale per chiedere dati allo strumento

import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('USB0::0x0957::0x1807::MY63260252::INSTR')
#my_instrument.write o read o query
print(my_instrument.query("*IDN?"))
"""

from Keysight53220A import Keysight53220A

freq = Keysight53220A('USB0::0x0957::0x1807::MY63260252::INSTR')




freq.idn()
freq.reset()
freq.clear()
freq.beep()

freq.set_input_impedance(1,50)
freq.get_input_impedance(1)
freq.set_coupling(1, 'AC')
freq.get_coupling(1)
freq.set_range(1, 5)
freq.get_range(1)
freq.set_autolevel(1, 'ON')
freq.get_autolevel(1)


freq.meas_volt_min(1)
freq.meas_volt_max(1)
freq.meas_volt_p2p(1)

freq.measure_frequency(1, 250e-6, 20, 'NEG')
freq.measure_period(1, 1e-3, 50, 'POS')

freq.measure_risetime(1, 10, 90)
freq.measure_falltime(1, 80, 20)
freq.measure_pwidth(1, 50)
freq.measure_nwidth(1, 50)
freq.measure_pos_dutycycle(1, 50)
freq.measure_neg_dutycycle(1, 50)
freq.measure_single_period(1)

freq.measure_totalize(1, 0.1)

freq.close()