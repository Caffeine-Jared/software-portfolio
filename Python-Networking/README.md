# Overview
The purpose of this project was to learn more about how Python can work with networking modules like socket.
[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

For this project, I decided to go with a client/server model that allows multiple clients to connect to a server that allows intercommunication between clients. I am using a TCP communications, and utilizing user-defined ports to carry out client communications. My program encodes the messages that are sent to and from the server in UTF-8. 

# Development Environment

For this program I decided to use Linux as my main OS, and many of the traditional tools that I've used before like vscode, python3, etc. Using linux for this project has been fun and allowed me to experience a better dev experience. 

I also used socket for network communication and connections, colorama to allow for the clients to be distinct colors, and threading to allow for multiple client connections. Threading was the most difficult part of this program. 

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python Docs - Socket](https://docs.python.org/3/library/socket.html)
* [colorama](https://pypi.org/project/colorama/)

# Future Work

I want to make this program peer to peer next, and see how that ends up. 

- fix the way that messages input
- change the way the network connections are established