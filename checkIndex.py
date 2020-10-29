# This tool checks the shared files index for corruption
# Run it from your MuWire home directory
# It will print out a list of corrupt index files

import os, os.path, json

for root,_,files in os.walk("files") :
    for f in files:
        if not f.endswith(".json") :
            continue
        path = os.path.join(root,f)
        print("processing %s" % path)
        with open(path) as jsonFile :
            try :
                json.load(jsonFile)
            except :
                print("error in %s" % path)

