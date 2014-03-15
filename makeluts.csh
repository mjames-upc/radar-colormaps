#!/bin/csh
cd ~/radar-colormaps/
set files = `ls *.cmap`
foreach file ($files)
   python awips2-lutfil.py "$file"
end
