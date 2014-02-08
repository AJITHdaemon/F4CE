#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

# Retrieve form fields
#form   = cgi.FieldStorage()			# Get POST data
#fname  = form.getfirst("fname")			# Pull fname field data
#lname  = form.getfirst("lname")			# Pull lname field data
#secret = form.getfirst("secretsquirrel")	# Pull secretsquirrel field from POST data
print "Content-type: text/html"
print '''
<!DOCTYPE html>
<html>
	<head>
		<title>Sample video check</title>
	</head>
	<body>
		<video src = "http://192.168.1.106/tep.mp4" controls></video>
	</body>
</html>
'''
