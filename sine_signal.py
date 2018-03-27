# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:08:27 2018

@author: huyinan
"""

'''    building communication      '''

import numpy as np
import time
import tldevice

'''    choose the port    '''

csb = tldevice.Device('COM5')

'''     Sine type signal generator           '''

current_amplitude=0.01 #mA
frequency=10  #Hz
sampling_rate = 50
#Phase=90
delay=1/frequency/(sampling_rate-1)

for  t in  np.arange(0, 1000.0, 1.0/sampling_rate):
     y = current_amplitude*np.sin(frequency*2*np.pi*t)
     csb.coil.y.current(y) # mA
     print(y)
     time.sleep(delay) #delay time: s



