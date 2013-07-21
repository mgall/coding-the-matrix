#!/usr/bin/python3

import sys
from inverse_index_lab import *
print( 'Loading Documents' )
f = open( "stories_small.txt" )
docs = list(f)
f.close()
print( "--> %i documents loaded" %(len(docs)) )


print( "\nIndexing documents" )
rIndex = makeInverseIndex(docs);
print( "--> %i words indexed over %i documents" % (len(rIndex),len(docs)) )

query = sys.argv[1:] or ["you", "test"]
print( 'Searching by query: "%s"' % " ".join(query) )

print( "--> Or result:" )
print( orSearch(rIndex, query) or "Nothing found" )

print( "--> And result:" )
print( andSearch(rIndex, query) or "Nothing found" )

