#!/usr/bin/env python
# File    : led.py 
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.2  02/17/2016
# Copyright (C) 2016 Joe McManus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import mraa
import time
import argparse

parser = argparse.ArgumentParser(description='Simple LED Blinker for Galileo')
parser.add_argument('pinNumber', help="Specify the pin number, i.e. 0-13", type=int)
parser.add_argument('--count', help="Number of times to execute, default infinity", default=0, type=int, action="store")
parser.add_argument('--delay', help="Number of seconds to wait between blinkings, default 10", default=10, type=int, action="store")
parser.add_argument('--version', action='version',version='%(prog)s 0.2')
args=parser.parse_args()


#Initialize the MRAA pin
pin = mraa.Gpio(int(args.pinNumber))
pin.dir(mraa.DIR_OUT)
pin.write(0)
print("Blinking LED {:d}". format(args.pinNumber))
print("Using delay {:d} and for {:d} attempts".format(args.delay, args.count))

i = 0 
while True: 
	try:
		print("Turning LED {:d} on, for {:d} seconds, count {:d}.".format(args.pinNumber, args.delay, i))
		pin.write(1)
		i = i+1
		if args.count != 0:
			if args.count == i:
				pin.write(args.pinNumber)
				break
		time.sleep(args.delay)

		print("Turning LED {:d} off, for {:d} seconds.".format(args.pinNumber, args.delay))
		pin.write(0)
		time.sleep(args.delay)
	
	except KeyboardInterrupt:
		quit()

	except Exception,e: 
		print("Error: {:s}". format(e))
		quit()
	
