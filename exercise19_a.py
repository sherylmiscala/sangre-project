def cake_order(type, flavour):
    print "I like %s cake!" % type
    print "I love it to be a %s cake." % flavour
    print "I can't wait to eat it."
    
print "=====================1==============="    
type = "fondant"
flavour = "chocolate"
cake_order(type, flavour)

print "=====================2==============="
cake_order("buttercream", "strawberry")

print "=====================3==============="
cake_order('sponge', 'ube')

print "=====================4==============="
cake_order(1,3)

print "=====================5==============="
type = raw_input("type: ")
flavour = raw_input("flavour: ")
cake_order(type, flavour)

print "=====================6==============="
cake_order('','')

print "=====================7==============="
type = int(raw_input("type: "))
flavour = int(raw_input("flavour: "))
cake_order(type, flavour)

print "=====================8==============="
print cake_order(type, flavour)

print "=====================9==============="
type = "cheesecake"
flavour = "red bean"
cake_order("{}".format(type), "{}".format(flavour))

print "=====================10==============="
type = "icecream"
flavour = type
cake_order(type , flavour)
