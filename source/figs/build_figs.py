# Build app/data/figs.json from the diagram modules (all original SVG).
import sys,json,os
sys.path.insert(0,os.path.dirname(__file__))
import phys,chem,maths
F={**phys.F,**chem.F,**maths.F}
assert len(F)==len(phys.F)+len(chem.F)+len(maths.F),'duplicate figure name'
json.dump(F,open(os.path.join(os.path.dirname(__file__),'../../app/data/figs.json'),'w'),ensure_ascii=False,separators=(',',':'))
print('figs',len(F),'bytes',sum(map(len,F.values())))
