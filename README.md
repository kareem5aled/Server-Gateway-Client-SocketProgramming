# Server-Gateway-Client-SocketProgramming

This is a socket programming project that is divided into three main parts:

**P1**: is a multithreaded gateway server that has the capability of handling multiple clients concurrently by using threads. It accepts connections from clients, receives data from them, performs a couple of mathematical operations on the first two arguments of the data and finally, send the resultant four arguments to the server specified by the third and fourth arguments.

**P2**: is a daemon server waiting to be contacted by P1 and prints the four arguments received from P1 on the standard output. There are several instances of P2 (specified by P2_i); all of them do the same role.

**P3**: is a client that reads four arguments from standard input, passes them to P1 and closes the connection afterwards. There are several instances of P1 (specified by P1_i); all of them do the same role.

The IP addresses and port numbers of each of the previous instances are provided in a config file.

The following figure simplifies how the system ![system](C:\Users\Karim\Desktop\Socket\system.PNG)works: