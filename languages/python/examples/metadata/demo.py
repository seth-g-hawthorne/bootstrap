# Simple demo of metadata_parser

import metadata_parser 
import sys
import pprint

if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    url = 'https://www.imdb.com/list/ls053501318/'
    
page = metadata_parser.MetadataParser(url, search_head_only=False)
pprint.pprint(page.metadata)

