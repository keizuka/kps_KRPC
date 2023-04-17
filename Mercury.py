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
