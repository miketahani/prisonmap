# scrape USA prison KML files for all states from Prisoners of the Census
import urllib
import os

RAW_DIR = 'raw/'
# if the raw data directory doesn't exist, create it
if not os.path.exists(RAW_DIR):
    os.mkdir(RAW_DIR)

base = "http://www.prisonersofthecensus.org/locator2010/kml/"
filename = "state_pts_%02d.kml"
for i in xrange(1,57):  # 56 files total, 01-56
    local_filename = filename % i
    if not os.path.exists(RAW_DIR+local_filename):
        urllib.urlretrieve(base+local_filename, filename=RAW_DIR+local_filename)
        print "[*] retrieved %s%s" % (base, local_filename)
    else:
        print "[*] file %s exists, skipping" % local_filename
print "done"