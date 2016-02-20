states = {
	'Oregon':'OR',
	'Florida':'FL',
	'New York':'NY',
	'California':'CA',
	'Michigan':'MI',
	'Miami':'MI'	
}

cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville',
#	'MI':'Miami'
}

state = states.get('Texas')

if not state:
	print "Sorry, no Texas"

city = cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is %s"%city
print " Key MI is for %r "%cities.get('MI')

