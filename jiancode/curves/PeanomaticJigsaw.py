name='peanomaticJigsaw'

def reverse(originalList):
	list=originalList[:]
	out=[]
	rev={}

	rev['l']=['r']
	rev['r']=['l']

	rev['u']=['d']
	rev['d']=['u']

	rev['D']=['U']
	rev['U']=['D']

	rev['E']=['W']
	rev['W']=['E']

	rev['L']=['R']
	rev['R']=['L']

	rev['N']=['S']
	rev['S']=['N']

	list.reverse()
	for item in list:
		out.extend(rev[item])
	return out

def flipx(list):
	out=[]
	flip={}
	flip['l']=['r']#
	flip['r']=['l']#

	flip['L']=['R']
	flip['R']=['L']

	flip['W']=['E']
	flip['E']=['W']

	flip['U']=['N']
	flip['N']=['U']

	flip['D']=['S']
	flip['S']=['D']

	for item in list:
		try:
			out.extend(flip[item])
		except:
			out.extend(item)
	return out

def clockwise(list):
	out=[]
	flip={}
	flip['R']=['S']
	flip['S']=['W']
	flip['W']=['U']
	flip['U']=['R']
	flip['L']=['N']
	flip['N']=['E']
	flip['E']=['D']
	flip['D']=['L']

	flip['r']=['d']
	flip['d']=['l']
	flip['l']=['u']
	flip['u']=['r']

	for item in list:
		try:
			out.extend(flip[item])
		except:
			out.extend(item)
	return out


alphabet={}

from curvegenerator import *
#group 1 top edge
print plists['jigsaw1R']
#alphabet['R']=list(listsolve([0,0,0],plists['jigsaw1R'],[7,0,0],random=1)[0])
listsolve([0,0,0],plists['hilbert'],[1,0,0],random=1,printout=1)
print plists['jigsaw1R']
listsolve([0,0,0],plists['jigsaw1R'],[7,0,0],random=1,printout=1)


for key in alphabet.keys():
	print key, alphabet[key]



"""from rewrite2D import solve
rewrite={}
rewrite['R']=list(solve([0,0,0],alphabet['R'],[1,0,0]))

rewrite['r']=['r']
rewrite['d']=['d']
rewrite['u']=['u']
rewrite['l']=['l']

for key in rewrite.keys():
	print key, rewrite[key]
symbols=list('R')
"""
