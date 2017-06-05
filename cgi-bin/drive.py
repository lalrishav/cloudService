#!/usr/bin/python2

import cgi,os
form = cgi.FieldStorage()
print "Content-type: text/html\n"
print ""
print "hello"
print "<pre>"
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
	link=os.path.abspath(root)[13:]
	print "<h3>"
        print("{}{}/".format(indent, os.path.basename(root)))
	print "</h3>"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
	    path=link+"/"+f
            print("{}<a href='{}'>{}</a>".format(subindent,path,f))

user=form.getvalue("user")
secret_key = form.getvalue("secret_key")
if secret_key == "qwerty":
	list_files("/var/www/html/users/"+user)

print "</pre>"
