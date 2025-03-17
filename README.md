# Showing performance of local function call vs. http-request
Example is a programm that counts the number of words in test.txt.
# Local function call
```
$ python3 all_local.py 
Anzahl der Wörter: 2614
Ausführungsdauer: 0.000607 Sekunden
```
# HTTP-Request on localhost
The program is splitted in a client (reading file and sending to server) and a server (counting the words in a line and sending back the integer number). It is just running on localhost using HTTP to communicate between client and server.
Open in first terminal 
```
$ python3 server.py
Open in second termin
```
In the second terminal the client:
```
$ python3 client.py 
Anzahl der Wörter: 2614
Ausführungsdauer: 8.087693 Sekunden
```
# Factor

8.087693/0.000607 = about 13.000

Remote function call is about *13.000* slower under this setup!
