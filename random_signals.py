# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:08:27 2018

@author: huyinan
"""
'''    building communication      '''

import numpy as np
import time
import tldevice
import random

'''    choose the port    '''

csb = tldevice.Device('COM5')

'''     signal generator           '''

delay=0.02 # delay time:second

for i in range(100000):

   t = random.randrange(1,1000,1)
   y=0.1/t
   csb.coil.y.current(y) # mA
   print(y)
   time.sleep(delay) #delay time: s


