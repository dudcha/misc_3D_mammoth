name='jigsaw'

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

#group 1 top edge

alphabet['E']=list('ruluurdrddruurrullluuullurrrdddruuuuurdddddruuurddrrdlldldrdldr')
alphabet['W']=reverse(alphabet['E'])
alphabet['U']=clockwise(flipx(alphabet['E']))
alphabet['D']=reverse(alphabet['U'])

alphabet['R']=list('drurrdldrdldlldrrdlldrrruuurdruuluruluuurddrdddddddruuuurrulluu')
alphabet['L']=reverse(alphabet['R'])
alphabet['N']=clockwise(flipx(alphabet['R']))
alphabet['S']=reverse(alphabet['R'])

alphabet['r']=['r']
alphabet['d']=['d']
alphabet['u']=['u']
alphabet['l']=['l']

from rewrite2D import solve


rewrite={}

rewrite['E']=list(solve([0,1,0],alphabet['E'],[1,1,0],random=0))
rewrite['W']=reverse(rewrite['E'])
rewrite['U']=clockwise(flipx(rewrite['E']))
rewrite['D']=reverse(rewrite['U'])

rewrite['R']=list(solve([0,0,0],alphabet['R'],[1,0,0],random=0))
rewrite['L']=reverse(rewrite['R'])
rewrite['N']=clockwise(flipx(rewrite['R']))
rewrite['S']=reverse(rewrite['R'])


rewrite['r']=['r']
rewrite['d']=['d']
rewrite['u']=['u']
rewrite['l']=['l']

#for key in rewrite.keys():
#	print key, rewrite[key]
symbols=list('R')
