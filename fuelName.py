import krpc

conn = krpc.connect(name='fuelName')

vessel = conn.space_center.active_vessel

fuel_name = conn.get_call(vessel.resources)

print(fuel_name)
