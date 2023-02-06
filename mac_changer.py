#!/usr/bin/env python

#------------------------------------------------------------------------------------------#
#This is the code written by Arjun Shetty, which is used as a tool to change the MAC address directly from the terminal
#------------------------------------------------------------------------------------------#

#This program is used to change the mac_address of a system,for this to work we hace to input
#the interface and also the value of the new_mac address.
#there are chances of user using other commands to manipulate the code to perform different functions
#in the input section if we type "eth0;ls;"then the ls command will also run which can be replaces with other 
#scripts to affect the program

import subprocess
import optparse
import re

#function-----------------------------------------------------------------------------------#

def get_arguments():
    parser = optparse.OptionParser() 
    parser.add_option("-i", "--interface", dest="interface",
                     help="interface to change mac_address")
    parser.add_option("-m", "--change", dest="new_mac",
                     help="enter the new mac_address")
  # return parser.parse_args() 
  #when the get_arguments gets called, the code inside the function is executed and 
  #the values which is recieves should be returned as 'options' in the main code

    (option, arguments)= parser.parse_args()
    if not option.interface: 
        parser.error("[-] please enter a interface, use '--help' for more info")
    elif not option.new_mac:
        parser.error("[-] please enter a mac_address, use '--help' for more info")
    return option #since argument is not used

def change_mac(interface, new_mac): #to use a funstion in python the remaining scripts should be in  a indent
#or we can say like a tab space
    print("welcome to mac changer !!")
    print("[+] changing the " + interface + " into " + new_mac)
    subprocess.call(["sudo","ifconfig",interface,"down"])
    subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["sudo","ifconfig",interface,"up"])
    # subprocess.call("sudo ifconfig ", shell = True)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8") #since the subprocess.check_output gives output in bytes
#the re.search uses string values, fir this we use 'utf-8' to convert byte into str
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    # print (ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0) #this is used to choose one group if there are more than one match
    else:
        print("[-] could not find mac_address in interface")
#-------------------------------------------------------------------------------------------#

#main code-----------------------------------------------------------------------------------#
#use the tool as how we would normally use a hacking tool
# interface = option.interface
# new_mac = option.new_mac

option = get_arguments() #options and arguements are actually variables

current_mac = get_current_mac (option.interface)
print("current_MAC= " + str(current_mac)) #str is used so that even if the python returns a NoneType, it prints
#it like a string (type casting)

change_mac(option.interface, option.new_mac)

current_mac = get_current_mac(option.interface) #this is the updated mac
if current_mac == option.new_mac:
    print("mac_address was successfully changed to " + option.new_mac)
else:
    print("mac_address did not get changed")

#--------------------------------------------------------------------------------------------#

# interface= input ("enter the interface: ")
# new_mac = input ("enter the new_mac address: ")
# subprocess.call("sudo ifconfig", shell = True) 
# subprocess.call("sudo ifconfig " + interface +" down", shell = True)
# subprocess.call("sudo ifconfig " + interface + " hw ether "+ new_mac , shell = True)
# subprocess.call("sudo ifconfig " +interface +" up", shell = True)
# subprocess.call("sudo ifconfig ", shell = True)

#--------------------------------------------------------------------------------------------#

#the goal was to check if the mac address changed
#the steps were:
#[1] execute and read ifconfig
#[2]read tha mac addresss from the output
#[3]check oif the MAC in the ifconfig is what the user requested
#[4]print the appropriate message

#----------------------------------------------------------------------------------------------#
#if you want to match a specified line like the mac_address, we can use the "regex expression" which is found
#using the 'pythex' program by inlcuding "\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" denoting a alphanumeric line of code
#this can also be done using re- regular expression