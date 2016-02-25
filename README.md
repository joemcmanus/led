# led
A Simple Intel Galileo LED Control Script in Python

I had a bit of trouble finding information on blinking an LED on the Intel Galileo Gen 2 using python 
and wanted to share a script that blinks an LED. 

This uses MRAA to perform all the real tasks. 

Which does the following:

Initialize the pin 

    pin = mraa.Gpio(X) # where X is the pin number

Set it to output mode

    pin.dir(MRAA.DIR_OUT) 

Turn it on or off (0/1) 

    pin.write(1) # Turn on
    pin.write(0) # Turn off

But it is just wrapped in a script which will do this for you. 

Simple use: 

    root@galileo:~# ./led.py 1 
    Blinking LED 1
    Using delay 10 and for 0 attempts
    Turning LED 1 on, for 10 seconds, count 0.

    root@galileo:~ ./led.py --help
    usage: led.py [-h] [--count COUNT] [--delay DELAY] [--version] pinNumber

    Simple LED Blinker for Galileo

    positional arguments:
      pinNumber      Specify the pin number, i.e. 0-13

    optional arguments:
      -h, --help     show this help message and exit
      --count COUNT  Number of times to execute, default infinity
      --delay DELAY  Number of seconds to wait between readings, default 10
      --version      show program's version number and exit
 
Possible Wiring:
![alt tag](https://raw.githubusercontent.com/joemcmanus/led/master/GalileoGen2-LED_bb.png)
