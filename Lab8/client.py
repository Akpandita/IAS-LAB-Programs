# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12347           
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 

print "Enter the data to be sent:-"
ciphertext=raw_input()
s.send(ciphertext)
# close the connection 
s.close() 