import pysvf

pysvf.buildSVFModule(["./BASIC_array_2d_0-0.c.bc"])
pag = pysvf.getPAG()
icfg = pag.getICFG()
print("Module Identifier:", pag.getModuleIdentifier())
print("ICFG Node count:", len(icfg.getICFGNodeList()))
