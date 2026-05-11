"""
code for instrument instruction
13 03 2026
arbitrary function generator
"""

import numpy as np
import pyvisa
from TektronixAFG3011C import AFG3011C


"""
rm = pyvisa.ResourceManager()
print(rm.list_resources())
"""

# definisco il mio strumento
afg = AFG3011C('USB0::0x0699::0x034F::C020209::INSTR', verbose=True)

frequencies = np.array([1e3, 10e3, 100e3, 1e6])

# lo ho connesso / inizializzato

afg.idn()
afg.reset()
afg.clear()

# lo ho anche resettato e pulito

afg.beep()

# ora gli do le istruzioni

afg.set_function('SQU')
afg.set_frequency(frequencies[3])
afg.set_amplitude(6)
afg.set_output_impedance('50')
# c'e solo 50 ma lo strumento va da 1 ohm a 10k ohm
afg.set_output_state(True)

afg.close()