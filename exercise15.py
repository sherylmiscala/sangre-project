from sys import argv

#assign 2variables
script, filename = argv

# variable txt will open the filename
txt = open(filename)

#read the content of the filename passed in %r
print "Here's your file %r: " % filename
print txt.read()

#key in filename again
#print "Type the filename again: "
#file_again = raw_input("> ")

#open filename again and assign it to txt_again
#txt_again = open(file_again)

#print the content of the filename
#print txt_again.read()