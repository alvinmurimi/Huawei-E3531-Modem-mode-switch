#!/usr/bin/python
import commands
import os
import subprocess
print """
 _                              _ 
| |__  _   _  __ ___      _____(_)
| '_ \| | | |/ _` \ \ /\ / / _ \ |
| | | | |_| | (_| |\ V  V /  __/ |
|_| |_|\__,_|\__,_| \_/\_/ \___|_|
     E3531 modem mode switcher
"""
def details():
	modem = commands.getstatusoutput("lsusb | grep 'Huawei'")
	modem = str(modem[1])
	if(len(modem) < 1):
		print "Modem not found. Please connect your USB modem and try again\n"
		raw_input("Press any key to exit.")
		exit()
	else:
		print "[OK] Modem found\n"
		print "[*] Print checking dependencies..."
	confirm()
	return
def confirm():
	confirm = commands.getstatusoutput("usb_modeswitch -v")
	confirm = str(confirm[1])
	if(len(confirm) < 100):
		response = raw_input("usb modeswitch is not installed. Do you want to install it? (Y or N)")
		if(response == 'Y' or response == 'y'):
			os.system("apt-get install usb-modeswitch")
		else:
			print "Please install usb modeswitch"
			exit()
	else:
		print "[OK] USB modeswitch installed.."
		print "[*]  Starting swich process"
		make()
	return
def make():
	os.system("v=$(lsusb | grep 'Huawei' | awk '{ print $6 }' | awk -F: '{ print $1 }'); p=$(lsusb | grep 'Huawei' | awk '{ print $6 }' | awk -F: '{ print $2 }'); sudo usb_modeswitch -v $v -p $p -M '55534243123456780000000000000011062000000100000000000000000000'")
	print "[OK] Modem mode switch success"
	reboot = raw_input("The changes have been made to your Huawei E3551 USB modem. Do you wish to reboot for changes to take place?(Y or N)")
	if(reboot == 'Y' or reboot == 'y' or reboot == 'yes' or reboot == 'YES'):
		os.system("reboot")
	else:
		exit()
	print "Rebooting..."
	return

details()