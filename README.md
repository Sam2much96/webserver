# webserver
hosts a secure webserver (https://), that can be connected to from a remote machine

Instructions to check your device's IP address and generate a new web server certificate are in
the python script.

Make sure to add a security exception for the server's certificate in your web browser's settings
when connecting for the first time, browsers don't support self signed webservers and i suggest using
a CA certified certificate when hosting for production
