# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:03:07 2022

@author: Karim
"""

import socket
import configparser
import sys

#P2 is a server continuously listening and awaits to be connected by P1 and 
#prints the four arguments that P1 has sent

def Main():
    #Reading the main variables from config file
    config = configparser.ConfigParser()
    config.read('config.cfg')
    HOST = config['P2_2']['HOST']
    PORT = int(config['P2_2']['PORT'])  
    #creation of TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #try binding server host address and port number together and exit if failed 
        try:
            s.bind((HOST, PORT))
        except socket.error  :
            print("Error creating server socket")
            sys.exit() 
        while True:
            #prepare the server for incoming requests
            print("=========================================")
            print('Waiting for connection..')
            s.listen()
            #Establish connection with gateway server
            try:
                conn, addr = s.accept()
            except:
                print("Error accepting connection")
                continue
            with conn:
                print('Connected by', addr)
                #Receive data from gateway server, decode it to strings and print it
                data = conn.recv(1024)
                data = data.decode("utf-8") 
                print('The four arguemnts are:'+data)
                
if __name__ == "__main__":
    Main()