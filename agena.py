import krpc
import time

conn = krpc.connect()
vessel = conn.space_center.active_vessel
targetAlt = 300000
vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)
print('engine startup')
vessel.control.activate_next_stage()
time.sleep(5)
print('launch')
vessel.control.activate_next_stage()
vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()

fuel = vessel.resources_in_decouple_stage(1, cumulative=False).amount('Kerosene')
# oxy = vessel.resources_in_decouple_stage(3, cumulative=False).amount('Ox')
while fuel > 1.0:
    print(vessel.resources_in_decouple_stage(1, cumulative=False).amount('Kerosene'))
#    print(vessel.resources_in_decouple_stage(3, cumulative=False).amount('Ox'))
    time.sleep(1)
    fuel = vessel.resources_in_decouple_stage(1, cumulative=False).amount('Kerosene')
#    oxy = vessel.resources_in_decouple_stage(3, cumulative=False).amount('Ox')

if fuel < 0.1:
    vessel.control.throttle = 0
    vessel.control.activate_next_stage()

