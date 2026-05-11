import pyvisa
from GPP4323 import GPP4323
import time

"""
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
"""

gen = GPP4323("ASRL4::INSTR")  # PROVA A TOGLIERE IL PUNTO

print(gen.idn())

gen.set_voltage(1, 4.1)
gen.set_current(1, 0.5)
gen.output_on(1)
time.sleep(0.5)

v = gen.measure_voltage(1)
i = gen.measure_current(1)

print("Misure:", v, "V", i, "A")

gen.output_off(1)
gen.close()