import pysvf

pysvf.buildSVFModule(["./BASIC_array_2d_0-0.c.bc"])
pag = pysvf.getPAG()
icfg = pag.getICFG()
node_list = icfg.getICFGNodeList()
print("Total ICFG nodes:", len(node_list))
if len(node_list) > 0:
    first_node = node_list[0]
    print("First Node ID:", first_node.getId())
