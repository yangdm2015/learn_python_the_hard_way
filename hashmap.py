def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap
    
def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to
    an index for the aMap's buckets."""
    return hash(key) % len(aMap)
    
states = new()    
key = hash('Oregon')
num = hash('Oregon')% len(states)
print 'The key of "Oregon" is %r' %key
print 'The number of "Oregon %% 256" is %r' %num
print hash_key(states, 'Oregon')
bucket = [['Oregon','OR'],['Florida','FL']]
print bucket
k,v = bucket[0]
print 'k = ',k
print 'v = ',v