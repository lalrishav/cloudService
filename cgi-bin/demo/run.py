#!/usr/bin/python2

import cgi,commands,subprocess

print "Content-type:text/html"
print ""

def php(script_path):
    p = subprocess.Popen(['php', script_path], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result

print php("/var/www/html/demo/run.php")

