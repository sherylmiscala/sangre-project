from sys import argv

script, filename = argv

print "We're going to read %r." % filename

print "Opening the file..."
target = open(filename,'r')

#line = target.readlines()
#print "reading all lines %s" %line

for line in target:
	print line,

print "And finally, we close it."
target.close()