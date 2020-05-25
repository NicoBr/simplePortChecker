# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:54:48 2020

@author: brettnern
"""

import socket
import sys, getopt


def main(argv):
   ipAdress = ''
   port = ''
   try:
      opts, args = getopt.getopt(argv,"hi:p:",["ip=","port="])
   except getopt.GetoptError:
      help()
      sys.exit(2)
   for opt, arg in opts:
      if opt in ('-h' '--help'):
         help
         sys.exit()
      elif opt in ("-i", "--ip"):
         ipAdress = arg
      elif opt in ("-p", "--port"):
         port = arg
   
   if (ipAdress=="" or port=="" or int(port)>65535):
       help()
       sys.exit()
   else:
       print ('Adress or name is ', ipAdress)
       print ('the port is ', port)
       print ("Please be patient... the check could take some seconds...")
       print ("w.e.g. waard e Moment, et kann daueren...")
       print ("")
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       result = sock.connect_ex((ipAdress,int(port)))
       if result == 0:
            print ("Port is open")
       else:
           print ("Port is not open")
           sock.close()
def help():
    print ("Checks if port is open for a given IP or domain-name")
    print ('simplePortChecker -i <destination> -p <port> [-h]')
    print("""
-i --ipAdress     after this parameter  for the destination is indicated
destination       the IP-Adress or the domain-name
-p --Port         after this parameter for the port to check is indicated
port              port-numbre (between 0 and 65535)   

w.e.g. hudd Spaass...
          """)


if __name__ == "__main__":
   main(sys.argv[1:])
   