import subprocess
import random
from getmac import get_mac_address as gma

#random mac address generator
def randMac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )
#wireless interface
wirelessInterface = "en1" #input the interface you wish to use
#original mac address
originalMacAddress = "b0:34:95:ef:16:ea" #input your devices mac address here
#generate random mac address for first use
randomMacAdress = randMac()

while(0<10):
	# find current mac address
	currentMacAddress = gma(wirelessInterface)
	#check to see if the mac address is the same a the default address
	if originalMacAddress == currentMacAddress:
		#Disconnect from current wifi network
		subprocess.call(["sudo","/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", wirelessInterface, "-z"])
		#change mac address of the interface (en1)
		subprocess.call(["sudo","ifconfig",wirelessInterface,"ether",str(randomMacAdress)])
	else:
		print(currentMacAddress)
		continue