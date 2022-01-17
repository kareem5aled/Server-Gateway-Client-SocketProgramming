# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:07:31 2022

@author: Karim
"""

import socket            
import configparser
import ipaddress 
import sys

#P3 is a client that recieves four arguemnts from user input and sends them to P1

def Main():

    #Reading the main variables from config file
    config = configparser.ConfigParser()
    config.read('config.cfg')
    HOST = config['P1']['HOST']
    PORT = int(config['P1']['PORT'])             
    ClientSocket = socket.socket()    #instaniate client socket    

    #connect to the gateway server
    try:
        ClientSocket.connect((HOST, PORT))
    except :
        print("Error connecting to the gateway server")
        sys.exit()
    

    while True:
        #Recieve the 4 arguemnts from user input
        Input = input("Enter the four arguemnts (two numbers followed by ip address and port number):")
        #make sure the user entered two numbers followed by ip address and port number
        try:
            float(Input.split()[0]), float(Input.split()[1])
            ipaddress.ip_address((Input.split()[2]))
            int(Input.split()[3])

        except:
            print("Please enter a valid input")
            continue
        #make sure the two numbers are not too large
        if len(Input.split()[0]) > 15 or len(Input.split()[1]) > 15:
            print("Input numbers are too large")
            continue
        #send input to the gateway server and close the connection
        ClientSocket.send(str.encode(Input))
        ClientSocket.close()  
        break
if __name__ == "__main__":
    Main()