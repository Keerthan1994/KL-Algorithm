print('KL -Algorithm\nECE528 Final Project\nBy,\nKeerthan Nayak ')

import copy

NEW_FILE = []
ListofVertices =[]
VertexCount =0
No_of_iter=1

SWAPG = []

File_name = input('\n\nEnter the name of the input file : ')
with open(File_name, 'r') as input_file:

	vertices,edges  = map(int, input_file.readline().split())

	print('\nNumber of Vertices in the given graph : '+ str(vertices))
	print('\nNumber of Edges in the given graph : '+ str(edges))
	for each_line in input_file:
		NEW_FILE.append([int(value) for value in each_line.split()])

if vertices % 2 != 0 :
	NEW_FILE.append([int(0)])
	vertices +=1
for each_line in NEW_FILE:
	VertexCount +=1
	ListofVertices.append(VertexCount)

var=1
print
for everyelement in NEW_FILE:
	print('Node '+str(var)+'  : '+str(everyelement))
	var+=1
var = 0

my_gd = dict(zip(ListofVertices,NEW_FILE))

node1 = ListofVertices[:int(vertices/2)]
node2 = ListofVertices[int(vertices/2):]

Partition1_node = copy.deepcopy(node1)
Partition2_node = copy.deepcopy(node2)

def intcost(nodes_1, nodes_2, gd):
    part_cost = 0

    for each_key in gd.keys():
        for each_node_x in nodes_2:
            if each_node_x == each_key:
                for each_node_y in nodes_1:
                    if each_node_y in gd[each_key]:
                        part_cost +=1

    return part_cost

Vertex1_copy = copy.deepcopy(node1)
Vertex2_copy = copy.deepcopy(node2)



def Kerrlin_algo(part11, part21, part12, part22, my_dict_kl):
	NodeAA = part11
	NodeAB = part21
	NodeBA = part12
	NodeBB = part22
	kl_dict = my_dict_kl

	EXT_CST = INT_EXT_funct(NodeAA, NodeBB, kl_dict)
	EXT_CST2 = INT_EXT_funct(NodeBA, NodeAB, kl_dict)
	INT_CST1 = INT_EXT_funct(NodeAA, NodeAB, kl_dict)
	INT_CST2 = INT_EXT_funct(NodeBA, NodeBB, kl_dict)
	Dval1 = [Ez - Iz for Ez, Iz in zip(EXT_CST, INT_CST1)]
	Dval2 = [Ez - Iz for Ez, Iz in zip(EXT_CST2, INT_CST2)]

	print('external cost of partition 1 ', EXT_CST)
	print('internal cost of partition 1 ', INT_CST1)
	print('external cost of partition 2 ', EXT_CST2)
	print('internal cost of partition 2 ', INT_CST2)
	print('---------------------------------------------------------------')

	G_Val = cal_Gab(Dval1, Dval2, NodeAA, NodeBA, kl_dict)
	Swap_nodes = node_gain_list(NodeAA, NodeBA, G_Val)
	HGS  = high_gain(Swap_nodes)
	NodeAA, NodeBA = new_ListofVerticess(NodeAA, NodeBA, HGS)
	NodeAB, NodeBB = update_partition(HGS, NodeAB, NodeBB )
	return HGS, NodeAA, NodeBA, NodeAB, NodeBB

def INT_EXT_funct(List_of_Vertices1, List_of_Vertices2, Ver_tex):
    List_of_Connection = []
    List_of_Cost = []

    for node in List_of_Vertices2:
        for key in Ver_tex.keys():
            if node == key:
                List_of_Connection.append(Ver_tex[key])

    for node in List_of_Vertices1:
        Sum = 0
        for line in List_of_Connection:
            for x in line:
                if node == x:
                    Sum +=1
        List_of_Cost.append(Sum)
    return List_of_Cost

def cal_Gab(dValA, dValB, new_List_A, new_List_B, gDict):
    List_of_Connection = []
    addDABList = []
    ListCAB = []

    for node in new_List_B:
        for key in gDict.keys():
            if node == key:
                List_of_Connection.append(gDict[key])

    for dA in dValA:
        for dB in dValB:
            dAplusB = dA + dB
            addDABList.append(dAplusB)

    for node in new_List_A:
        for line in List_of_Connection:
            Sum = 0
            for x in line:
                if node == x:
                    Sum += 1
            cAB = 2*Sum
            ListCAB.append(cAB)

    CombX = [x - y for x, y in zip(addDABList, ListCAB)]

    return CombX

def node_gain_list(new_List_A, new_List_B, Log):
    nAnB = []
    nAnBList = []

    for x in new_List_A:
        for y in new_List_B:
            nAnB = [x] + [y]
            nAnBList.append(nAnB)

    CombX = zip(nAnBList, Log)

    return CombX

def high_gain(CombX):
    gain = -10000
    HIGHAIN = -10000
    HIGHAINSet = []

    for line in CombX:
        if line[0] not in Partition2_node:
            New_AB = line[0]
        gain = line[1]

        if gain > HIGHAIN:
            HIGHAIN = gain
            HIAB = New_AB
            HIGHAINSet = [HIAB] + [HIGHAIN]

    return  HIGHAINSet

def new_ListofVerticess(new_List_A, new_List_B, highestS):
    APmn = []
    BPmn = []
    a2bSwap = highestS[0][0]
    b2aSwap = highestS[0][1]

    for node in new_List_A:
        if node != a2bSwap:
            APmn.append(node)
    APmn.sort()

    for node in new_List_B:
        if node != b2aSwap:
            BPmn.append(node)
    BPmn.sort()

    return APmn, BPmn

def update_partition(highestS, GAnodes, GBnodes ):

    for line in GAnodes:
        if line == highestS[0][0]:
            GAnodes.remove(line)

    GAnodes.append(highestS[0][1])
    GAnodes.sort()

    for line in GBnodes:
        if line == highestS[0][1]:
            GBnodes.remove(line)
    GBnodes.append(highestS[0][0])
    GBnodes.sort()
    return GAnodes, GBnodes

def PGAIN(sLog):
    MPGN = -10000
    SumPG = 0
    MPGNSWPIDX = 0
    l=0
    for line in SWAPG:
        SumPG+=sLog[l][1]
        if SumPG> MPGN:
            MPGN=SumPG
            MPGNSWPIDX=l
        l+=1
    return MPGN, MPGNSWPIDX

def iter_part(new_List_A, new_List_B, sLog, sgIndex):
    count = 0
    for n in range(0,sgIndex+1):
        A,B=update_partition(sLog[count], new_List_A, new_List_B)
        new_List_A=copy.deepcopy(A)
        new_List_B=copy.deepcopy(B)
        count+=1
    return new_List_A, new_List_B

myfile = open("KL_output.txt", "w")
myfile.write('\nNumber of Vertices in the given graph : '+ str(vertices))
myfile.write('\nNumber of Edges in the given graph : '+ str(edges))
myfile.write("\n\n")


init_part_cost = intcost(Vertex1_copy,Vertex2_copy,my_gd)
node1.sort()
node2.sort()
print('Partition 1 : '+ str(node1))
print('Partition 2 : '+ str(node2))
print('Initial Cost of the partition : '+str(init_part_cost)+'\n')

Var_Count = 0
set_F = True

while (set_F):
	listlen = len (Partition1_node)
	counter = 1
	while (counter <= listlen):
		HighSet, Partition1_node, Partition2_node, Vertex1_copy, Vertex2_copy = Kerrlin_algo(Partition1_node, Vertex1_copy, Partition2_node, Vertex2_copy, my_gd)
		SWAPG.append(HighSet)
		counter += 1
	MP_Gain, MP_GainIndex = PGAIN(SWAPG)

	if MP_Gain > 0:
		Var_Count +=1
		print('Iteration' +str(Var_Count)+ '\n')
		node1, node2 = iter_part(node1, node2, SWAPG, MP_GainIndex)
		Vertex1_copy = copy.deepcopy(node1)
		Vertex2_copy = copy.deepcopy(node2)
		Partition1_node = copy.deepcopy(node1)
		Partition2_node = copy.deepcopy(node2)
		SWAPG = []
		init_part_cost = intcost(Vertex1_copy, Vertex2_copy, my_gd)
		print('----- Iteration :'+str(Var_Count)+' -----\n')
		print('Cut cost : '+' ' +str(init_part_cost)+'\n\n')

		myfile.write('----- Iteration :'+str(Var_Count)+' -----\n')
		myfile.write('Cut cost : '+' ' +str(init_part_cost)+'\n')


	else:
		print('Final Partition:\n')
		print('Partition 1 : '+ str(node1))
		print('\nPartition 2 : '+ str(node2))
		print('\n Final Cut Cost '+str(init_part_cost)+'\n')
		set_F = False

		myfile.write('Final Partition:\n')
		myfile.write('Partition 1 : '+ str(node1))
		myfile.write('\nPartition 2 : '+ str(node2))
		myfile.write('\n Final Cut Cost '+str(init_part_cost)+'\n')
