#generates hamiltonian paths given a list of vertices, start point, and end point
#from sys import *
#string=argv[1]
from random import shuffle
from cgtools import plists	# dictionary of position lists
from cgtools import poslist,posarray	# to check that the movelists returned are good
from time import time
benchmark=time()

# based on the coordinate system in Processing
#  .--x
# /|
#z y

move={'d': [0, 1, 0], 'i': [0, 0, -1], 'l': [-1, 0, 0], 'o': [0, 0, 1], 'r': [1, 0, 0], 'u': [0, -1, 0]}


#depth first recursion
#given a list of moves, returns the rewrite rule

def solve(position,poslist,end,random=0):
	moves=move.keys()
	if random: shuffle(moves) #randomizes, optional
	for M in moves:	#M - move name
		newpos=[a+b for a,b in zip(position,move[M])]
		if poslist==[end]:
			if newpos==end:
				return M
		else:
			if newpos in poslist:
				rest=solve(newpos,filter(lambda x: x!=newpos,poslist),end,random)
				if rest: return M+rest
	return

def listsolve(position,poslist,end,random=0,printout=0):
	global i
	global j
	i=0	#counter for results
	j=0	#counter for function calls
	global alist
	alist=[]
	if position not in poslist: return 'error'
	listsolvehelper('',position,filter(lambda x: x!=position,poslist),end,random,printout)
	print 'total results', i
	print 'total calls', j
	return alist

def listsolvehelper(output,position,poslist,end,random=0, printout=0):
	global j
	j+=1
	moves=move.keys()
	if random: shuffle(moves) #randomizes, optional
	for M in moves:	#M - move name
		newpos=[a+b for a,b in zip(position,move[M])]
		if poslist==[end]:
			if newpos==end:
				if printout:
					global i
					i+=1
					print message(), i , j , output+M, j/i, (time()-benchmark)/i

				else: alist.append(output+M)
		else:
			if newpos in poslist and end in poslist and smartconnected(position,newpos,poslist):
				listsolvehelper(output+M,newpos,filter(lambda x: x!=newpos,poslist),end,random,printout)
	return

def connected(position,graph):
	moves=move.keys()
	for M in moves:
		newpos=[a+b for a,b in zip(position,move[M])]
		if newpos in graph: return 1
	return 0
	
def allconnected(graph):
	for position in graph:
		if not connected(position,graph): return 0
	return 1

def smartconnected(pos,newpos,graph):
	moves=move.keys()
	for M in moves:
		X=[a+b for a,b in zip(pos,move[M])]
		if X !=newpos and X in graph:
			if not connected(X,graph): return 0
	return 1

def message():
	return '%10.5f'%(time()-benchmark)+'\t'

from sys import argv

#print posarray(plists['jigsaw1R'])
#listsolve([0,0,0],plists['jigsaw1R'],[7,0,0],printout=1)
#listsolve([0,0,0],plists['peanomatic'],[2,0,0],random=1,printout=1)
#listsolve([0,0,0],plists['peano3D'],[2,0,0],random=1,printout=0)
#listsolve([0,0,0],plists['peanomatic4x4'],[3,0,0],random=0, printout=1)

