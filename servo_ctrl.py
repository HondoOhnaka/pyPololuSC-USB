#	Control the pololu USB servo controller 16 on Mac (or Linux, or Win (may require add'l work))
#	http://www.pololu.com/catalog/product/390
#
#	basic code via pyusb site
#   http://sourceforge.net/projects/pyusb/
#	http://pyusb.sourceforge.net/docs/1.0/tutorial.html
#
#   Based on my previous work using pySerial, but updated for pyusb
#   posted original here
#   http://forum.pololu.com/viewtopic.php?f=16&t=535&start=0&st=0&sk=t&sd=a

import usb.core
import usb.util
import sys

START_BYTE = '\xff'
TIMEOUT_VALUE = 100 # not sure what this should be yet

def setup():
	# find our device
	# Vendor = Silicon Laboratories, Inc.
	global DEVICE
	DEVICE = usb.core.find(idVendor=0x10c4, idProduct=0x803b) 

	# was it found?
	if DEVICE is None:
	    raise ValueError('Device not found')

	# set the active configuration. With no arguments, the first
	# configuration will be the active one
	DEVICE.set_configuration()

def set_servo(servo, pos):
	servo_num = servo + 16  # note that the port is always n+16
	s2 = [START_BYTE,  chr(servo_num), chr(pos) ]
	DEVICE.ctrl_transfer(0x21, 0x09, 0, 0, [0xff, 0x10, 0xa0])
	s = '%c%c%c' % (START_BYTE, chr(servo_num), chr(pos))
	#DEVICE.write(s)

         print 'Moved Servo: %s to pos:%d' % (servo, pos)

def main(args):

    # if len(args) < 2:
    #     usage()
    #     sys.exit(1)

    setup()

	# a little servo exercis
    for i in range(0,255):
		set_servo(0,i)  # only testing a single servo

if __name__ == '__main__':
    main(sys.argv)