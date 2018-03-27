import tldevice

csb = tldevice.Device('COM5')
'''Building the communication'''

#csb.coil.x.current(0.0) # mA
csb.coil.y.current(0.0001) # mA
#csb.coil.z.current(0.0) # mA

w=csb.coil.y.current
print(w)