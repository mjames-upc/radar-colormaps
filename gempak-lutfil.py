#!/awips2/python/bin/python
#cat nids_vel8.cmap | grep "color r" | sed 's/\s.*color r="//g' | sed 's/" g="/ /g' | sed 's/" b="/ /g' | sed 's/" a=.*0"\/>//g'
#    <color r = "0.0117647058824" g = "0.494117647059" b = "0.501960784314" a = "1.0" />

import re, sys
rgb = 255 
if len(sys.argv) < 2:
	print "must specify input file\nexiting..."
	exit
a2file = sys.argv[1]
a2lut = a2file.split(".")
lutfil = a2lut[0] + '.cmap'

fout = open(lutfil, "wb")
fout.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
fout.write('<colorMap>\n')
with open(a2file, "rb") as f:
	for line in f:
		if "!" not in line:
			fvals = map(float, line.split())
			#print fvals
			lut = ["%0.7f" % (x/rgb) for x in fvals]
			#print lut
			outline = ' <color r="'+ str(lut[0]) +'" g="'+ str(lut[1]) +'" b="'+ str(lut[2]) +'" a="0.0"/>\n'
			fout.write(outline)

fout.write('</colorMap>\n')
f.close()
fout.close()
print "wrote " + lutfil
