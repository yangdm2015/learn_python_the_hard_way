# coding= utf-8 
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print "%s %r %r %r" % ("���","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had this thing.",
	"But it didn't sing.",
	"That' you could type up right.",
	
	"So I said goodnight."
	

)
