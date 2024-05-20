#depends on curvegenerator and rewrite2D

name='peanomatic4x4'

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
def reverse(originalList):
	list=originalList[:]
	out=[]
	rev={}

	rev['l']=['r']
	rev['r']=['l']

	rev['i']=['o']
	rev['o']=['i']

	rev['u']=['d']
	rev['d']=['u']

	rev['B']=['C']
	rev['C']=['B']

	rev['D']=['U']
	rev['U']=['D']

	rev['E']=['W']
	rev['W']=['E']

	rev['F']=['O']
	rev['O']=['F']

	rev['G']=['I']
	rev['I']=['G']

	rev['H']=['J']
	rev['J']=['H']

	rev['X']=['Z']
	rev['Z']=['X']

	rev['L']=['R']
	rev['R']=['L']

	rev['M']=['P']
	rev['P']=['M']

	rev['N']=['S']
	rev['S']=['N']

	rev['Q']=['T']
	rev['T']=['Q']

	rev['V']=['Y']
	rev['Y']=['V']

	list.reverse()
	for item in list:
		out.extend(rev[item])
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
alphabet['R']=list(listsolve([0,0,0],plists['peanomatic4x4'],[3,0,0],random=0)[1])
alphabet['S']=clockwise(alphabet['R'])
alphabet['W']=clockwise(alphabet['S'])
alphabet['U']=clockwise(alphabet['W'])

alphabet['L']=reverse(alphabet['R'])
alphabet['N']=clockwise(alphabet['L'])
alphabet['E']=clockwise(alphabet['N'])
alphabet['D']=clockwise(alphabet['E'])

alphabet['r']=['r']
alphabet['d']=['d']
alphabet['u']=['u']
alphabet['l']=['l']


#for key in alphabet.keys():
#	print key, alphabet[key]

print listsolve([0,0,0],plists['peanomatic4x4'],[3,0,0],random=0)

print
print

from rewrite2D import solve
rewrite={}
rewrite['R']=list(solve([0,0,0],alphabet['R'],[1,0,0],random=1))

rewrite['S']=clockwise(rewrite['R'])
rewrite['W']=clockwise(rewrite['S'])
rewrite['U']=clockwise(rewrite['W'])


rewrite['L']=reverse(rewrite['R'])
rewrite['N']=clockwise(rewrite['L'])
rewrite['E']=clockwise(rewrite['N'])
rewrite['D']=clockwise(rewrite['E'])

rewrite['r']=['r']
rewrite['d']=['d']
rewrite['u']=['u']
rewrite['l']=['l']

#for key in rewrite.keys():
#	print key, rewrite[key]
symbols=list('D')
