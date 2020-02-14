'''
simple python script to turn Raspberry Pi into
hardware digital source trigger

change TRIG_FREQ constant to define frequency of generated
triggers every second

Tchange RIG_PULSE constant to define active pulse width

Copyright 2019 (c) Innopolis University
'''

import time
from gpiozero import LED

TRIG_FREQ = 20 # triggers every second
TRIG_PULSE = 0.001 # 1ms active pulse width
trigger_channel = LED("GPIO24") # trigger channel

fstep =1/TRIG_FREQ

while True:
	# calculate next wake time
	fcur_time = time.time()
	tquot_rem =divmod(fcur_time,fstep)
	fwake_time = tquot_rem[0]*fstep+fstep
	
	fsleep_time = fwake_time - fcur_time
	# sleep until next period
	time.sleep(fsleep_time)
	
	#fnew_cur_time = time.time()
	
	# turn on
	trigger_channel.on()
	time.sleep(TRIG_PULSE)
	trigger_channel.off()
	#print('waked at ',fnew_cur_time)
