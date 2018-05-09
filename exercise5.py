name =  'Sheryl Miscala'
age = 37
height = 151.0 #cm
weight = 60.0 #kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "She's %d cm tall." % height
print "Sher's %d inches tall." % (height/2.54)
print "She's %d kg heavy." % weight
print "Sher's %d lbs heavy." % (weight*2.2)
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." %(eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
