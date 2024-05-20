#generates rewrites based on base cases

#from sys import *
#string=argv[1]

from random import shuffle
string='abcdefg'

#  z
# /
#.--x
#|
#y

cube={}

cube['D']=[[0,0,0],[0,1,0]]
cube['U']=[[0,1,0],[0,0,0]]

cube['E']=[[0,1,0],[1,1,0]]
cube['W']=[[1,1,0],[0,1,0]]

cube['L']=[[1,0,0],[0,0,0]]
cube['R']=[[0,0,0],[1,0,0]]

cube['N']=[[1,1,0],[1,0,0]]
cube['S']=[[1,0,0],[1,1,0]]


move={}

move['l']=[-1,0,0]
move['r']=[1,0,0]
move['u']=[0,-1,0]
move['d']=[0,1,0]

#returns true if the position agrees with the starting position of the cube
def agree(pos,cube):
	if pos==cube[0]:
		return True
	else:
		return False

#given the ending position of a cube and a move, returns the new position if the move is valid
#does not return otherwise (evaluates as boolean false)
def newPos(cube,move):
	pos=[0,0,0]
	for i in range(3):
		pos[i]=cube[1][i]+move[i]
	if pos!=[i%2 for i in pos]:
		return [i%2 for i in pos]

#depth first recursion
#given a list of moves, returns the rewrite rule

def solve(position,movelist,end,random=0):
	cubes=cube.keys()
	if random: shuffle(cubes) #randomizes
	for X in cubes:	#X - cube name
		if movelist==[]:
			if agree(position,cube[X]) and cube[X][1]==end:
				return X
		else:
			m=movelist[0]	#m - move name

			if agree(position,cube[X]) and newPos(cube[X],move[m]):
				rest = solve(newPos(cube[X],move[m]),movelist[1:],end,random)
				if rest: return X+m+rest
	return

def printsolve(output,position,movelist,end,random=0):
	cubes=cube.keys()
	if random: shuffle(cubes) #randomizes, optional
	for X in cubes:	#X - cube name
		if movelist==[]:
			if agree(position,cube[X]) and cube[X][1]==end:
				print output+X
		else:
			m=movelist[0]	#m - move name

			if agree(position,cube[X]) and newPos(cube[X],move[m]):
				printsolve(output+X+m,newPos(cube[X],move[m]),movelist[1:],end,random)
	return

def listsolve(position,movelist,end,random=0):
	global alist
	alist=[]
	listsolvehelper([],'',position,movelist,end,random=0)
	return alist

def listsolvehelper(output,position,movelist,end,random=0):
	cubes=cube.keys()
	if random: shuffle(cubes) #randomizes, optional
	for X in cubes:	#X - cube name
		if movelist==[]:
			if agree(position,cube[X]) and cube[X][1]==end:
				alist.append(output+X)
		else:
			m=movelist[0]	#m - move name

			if agree(position,cube[X]) and newPos(cube[X],move[m]):
				listsolvehelper(output+X+m,newPos(cube[X],move[m]),movelist[1:],end,random)

