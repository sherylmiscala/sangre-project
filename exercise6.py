x = "There are %d types of people." %10 # assigning value int 10 to %d
binary = "binary" # assigning value to binary string
do_not = "don't" # assigning value to do_not string
y = "Those who know %s and those who %s." %(binary, do_not) #passing 2 value strings in variable y

print x
print y

print "I said: %r." %x # passing value of x in %r
print "I also said: '%s'." %y # passing value of y to %s

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r."

print joke_evaluation % hilarious # passing hilarious to %r in joke_evaluation string

w = "This is the left side of..."
e = "a string with a right side."

print w + e #addition/concatenate 2 strings w and e

