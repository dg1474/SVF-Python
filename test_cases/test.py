import pysvf

pysvf.buildSVFModule(["./BASIC_array_2d_0-0.c.bc"])
pag = pysvf.getPAG()
icfg = pag.getICFG()
print("Module Identifier:", pag.getModuleIdentifier())
nodes = icfg.getNodes()
print("ICFG Node count:", len(nodes))
for node in nodes[:5]:
    print("Node ID:", node.getId())
