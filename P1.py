# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:40:25 2022

@author: Karim
"""

import socket
import configparser
import threading
import sys

#P1 is the gateway server that manages recieving data from different clients 
#simultaneously using threads and send this data to the target server 

def Main():
    #Reading the main variables from config file
    config = configparser.ConfigParser()
    config.read('config.cfg')
    HOST = config['P1']['HOST']
    PORT = int(config['P1']['PORT']) 
    thread_count = 1 #a variable that represents the current running thread and is used to print the current activity per each thread
    #creation of TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #try binding server host address and port number together and exit if failed 
        try:
            s.bind((HOST, PORT))
        except socket.error  :
            print("Error creating server socket")
            sys.exit() 
        while True:
            #prepare the server for incoming client requests
            print(str(thread_count) + ': Waiting for connection..')
            s.listen()
            
            #Establish connection with client.
            try:
                conn, addr = s.accept()
            except:
                print(str(thread_count)+": Error accepting connection")
                continue
            with conn:
                print(str(thread_count)+': Connected by', addr)
                #Receive data from client
                try:
                    data = conn.recv(1024)
                    print(str(thread_count)+ ": Received data from client")
                except:
                    print(str(thread_count)+": Error receiving data")
                    continue
                #Spawn a new thread for sending data to target server and wait to finish.  
                #Threads are used to handle multiple clients concurrently.
                thread = threading.Thread(target=send_data, args=(data,thread_count))
                thread.start()
                thread_count +=1

    
                
def send_data(data,thread_count):
    #decode the data from byte object to string and split it
    data = data.decode("utf-8") 
    data = data.split()
    #make sure division by zero is handled
    try:
        O1 = float(data[0])/float(data[1])
    except:
        print(str(thread_count)+ ": Division by zero")
        return
    #make sure the result from power operation is not too large
    try:
        O2 = float(data[0])**float(data[1])
    except:
        print(str(thread_count)+": Result too large")
        return
    HOST2 = data[2]         #target server ip address
    PORT2 = int(data[3])    #target server port number
    #create another TCP socket to connect to the target server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ServerSocket2:
        #try connecting to the target server
        try:
            ServerSocket2.connect((HOST2, PORT2)) 
        except:
            print(str(thread_count)+": Error establishing connection with target server")
            return
        #format data as space separated strings and send it to target server
        Data = " ".join([str(O1),str(O2),HOST2,str(PORT2)])
        try:
            ServerSocket2.send(str.encode(Data))
            print(str(thread_count)+': Data successfully sent to target server')
            ServerSocket2.close()
        except:
            print(str(thread_count)+": Error sending data to target server")
            return

if __name__ == "__main__":
    Main()