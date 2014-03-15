#!/awips2/python/bin/python
#cat nids_vel8.cmap | grep "color r" | sed 's/\s.*color r="//g' | sed 's/" g="/ /g' | sed 's/" b="/ /g' | sed 's/" a=.*0"\/>//g'
#    <color r = "0.0117647058824" g = "0.494117647059" b = "0.501960784314" a = "1.0" />
import re, sys
rgb = 255 
if len(sys.argv) != 2:
	print "must specify input file\nexiting..."
	exit
a2file = sys.argv[1]
a2lut = a2file.split(".")
lutfil = a2lut[0] + '.tbl'
fout = open(lutfil, "wb")
with open(a2file, "rb") as f:
	for line in f:
		line = re.sub(r' = ', r'=', line)
		line = re.sub(r'" />', r'"/>', line)
		line = re.sub(r'^\s+', r'', line)
		line = re.sub(r'\n', r'', line)
		line = re.sub(r'<color r="', r'', line)
		line = re.sub(r'" [b-z]="', r' ', line)
		line = re.sub(r'" a="[0-2].0"/>', r'', line)
		if "colorMap" not in line and "xml" not in line:
			fvals = map(float, line.split())
			lut = [int(round(x*rgb)) for x in fvals]
			outline = '                       '
			if lut[0] < 100:
				outline += ' '
			if lut[0] < 10:
				outline += ' '
			outline += str(lut[0]) + '    '
			if lut[1] < 100:
				outline += ' '
			if lut[1] < 10:
				outline += ' '
			outline += str(lut[1]) + '    '
			if lut[2] < 100:
				outline += ' '
			if lut[2] < 10:
				outline += ' '
			outline += str(lut[2]) + '\n'
			fout.write(outline)

f.close()
fout.close()
print "wrote " + lutfil
#                       119      0    125
