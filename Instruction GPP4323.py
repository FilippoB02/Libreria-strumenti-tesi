import pyvisa
from GPP4323 import GPP4323
import time

"""
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
"""

gen = GPP4323("ASRL3::INSTR")



gen.idn()
gen.reset()
gen.clear()


gen.set_voltage(1, 1)
gen.set_current(1, 1)
gen.set_voltage(2, 2)
gen.set_current(2, 5)
gen.set_voltage(3, 3)
gen.set_current(3, 5)
gen.set_voltage(4, 4)
gen.set_current(4, 5)

# resistenza

gen.output_on(1)
gen.output_on(2)
gen.output_on(3)
gen.output_on(4)

time.sleep(0.5)

gen.output_off(1)
gen.output_off(2)
gen.output_off(3)
gen.output_off(4)

gen.output_on_all()

gen.measure_param(1)
gen.measure_param(2)
gen.measure_param(3)
gen.measure_param(4)

gen.output_off_all()

"""
gen.series('ON')
gen.series('OFF')
gen.parallel('ON')
gen.parallel('OFF')

gen.parallel('ON')
gen.series('ON')
gen.series('OFF')
"""

gen.close()

