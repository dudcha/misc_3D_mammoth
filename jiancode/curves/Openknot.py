name='openknot'

def flipL(list):
	out=[]
	flip={}
	flip['l']=['i']
	flip['i']=['r']
	flip['r']=['o']
	flip['o']=['l']

	flip['L']=['I']
	flip['I']=['C']
	flip['C']=['O']
	flip['O']=['L']

	flip['R']=['G']
	flip['G']=['B']
	flip['B']=['F']
	flip['F']=['R']

	flip['W']=['T']
	flip['T']=['J']
	flip['J']=['P']
	flip['P']=['W']

	flip['H']=['M']
	flip['M']=['E']
	flip['E']=['Q']
	flip['Q']=['H']

	flip['U']=['V']
	flip['V']=['X']
	flip['X']=['N']
	flip['N']=['U']

	flip['D']=['Y']
	flip['Y']=['Z']
	flip['Z']=['S']
	flip['S']=['D']

	for item in list:
		try:
			out.extend(flip[item])
		except:
			out.extend(item)
	return out

def flipR(list):
	out=flipL(flipL(flipL(list)))
	return out

def flipx(list):
	out=[]
	flip={}
	flip['l']=['r']#
	flip['r']=['l']#

	flip['L']=['R']
	flip['R']=['L']
	flip['B']=['C']
	flip['C']=['B']
	flip['I']=['F']
	flip['F']=['I']
	flip['G']=['O']
	flip['O']=['G']

	flip['W']=['E']
	flip['E']=['W']
	flip['H']=['J']
	flip['J']=['H']
	flip['P']=['Q']
	flip['Q']=['P']
	flip['M']=['T']
	flip['T']=['M']

	flip['U']=['N']
	flip['N']=['U']
	flip['V']=['X']
	flip['X']=['V']

	flip['D']=['S']
	flip['S']=['D']
	flip['Y']=['Z']
	flip['Z']=['Y']

	for item in list:
		try:
			out.extend(flip[item])
		except:
			out.extend(item)
	return out

def flipy(list):
	out=[]
	flip={}
	flip['u']=['d']#
	flip['d']=['u']#

	flip['V']=['Y']
	flip['Y']=['V']
	flip['B']=['H']
	flip['H']=['B']
	flip['C']=['J']
	flip['J']=['C']
	flip['D']=['U']
	flip['U']=['D']
	flip['E']=['R']
	flip['R']=['E']
	flip['F']=['M']
	flip['M']=['F']
	flip['G']=['Q']
	flip['Q']=['G']
	flip['I']=['T']
	flip['T']=['I']
	flip['O']=['P']
	flip['P']=['O']
	flip['L']=['W']
	flip['W']=['L']
	flip['N']=['S']
	flip['S']=['N']
	flip['X']=['Z']
	flip['Z']=['X']

	for item in list:
		try:
			out.extend(flip[item])
		except:
			out.extend(item)
	return out

def flipCW(list):
	out=[]
	flip={}
	flip['l']=['u']
	flip['u']=['r']
	flip['r']=['d']
	flip['d']=['l']
	
	flip['V']=['C']
	flip['C']=['Z']
	flip['Z']=['H']
	flip['H']=['V']

	flip['Y']=['B']
	flip['B']=['X']
	flip['X']=['J']
	flip['J']=['Y']

	flip['D']=['L']
	flip['L']=['N']
	flip['N']=['E']
	flip['E']=['D']
	
	flip['U']=['R']
	flip['R']=['S']
	flip['S']=['W']
	flip['W']=['U']
	
	flip['F']=['M']
	flip['M']=['T']
	flip['T']=['I']
	flip['I']=['F']

	flip['G']=['O']
	flip['O']=['P']
	flip['P']=['Q']
	flip['Q']=['G']


	for item in list:
		try:
			out.extend(flip[item])
		except:
			out.extend(item)
	return out

def flipz(list):
	out=flipL(flipL(flipx(list)))
	return out

alphabet={}

#special closed
alphabet['A']=list('drilurol')

#group 1 top edge
alphabet['L']=list('ldrdldriiiuuuodloddiiuuuoorddilllouuriidddoouuiluidddooorulurul')

alphabet['R']=flipx(alphabet['L'])
alphabet['I']=flipL(alphabet['L'])
alphabet['O']=flipR(alphabet['L'])
#mirrors
alphabet['B']=flipz(alphabet['L'])
alphabet['C']=flipz(alphabet['R'])
alphabet['F']=flipx(alphabet['I'])
alphabet['G']=flipx(alphabet['O'])

#group 2 bottom edge
alphabet['W']=flipy(alphabet['L'])
alphabet['E']=flipx(alphabet['W'])#so far useless
alphabet['P']=flipR(alphabet['W'])#so far useless
alphabet['M']=flipR(alphabet['E'])
alphabet['Q']=flipx(alphabet['P'])
#mirrors
alphabet['H']=flipz(alphabet['W'])
alphabet['J']=flipz(alphabet['E'])
alphabet['T']=flipx(alphabet['M'])

#group 3 up
alphabet['U']=flipCW(alphabet['W'])
alphabet['N']=flipx(alphabet['U'])
#mirrors
alphabet['V']=flipz(alphabet['U'])
alphabet['X']=flipz(alphabet['N'])

#group 4 down
alphabet['D']=flipCW(alphabet['E'])
alphabet['S']=flipx(alphabet['D'])
#mirrors
alphabet['Z']=flipz(alphabet['S'])
alphabet['Y']=flipz(alphabet['D'])


alphabet['o']=['o']
alphabet['i']=['i']
alphabet['r']=['r']
alphabet['d']=['d']
alphabet['u']=['u']
alphabet['l']=['l']

rewrite={}

#special closed
rewrite['A']=list('SddddSrrrrTiiiiTllllXuuuuXrrrrGooooGllll')

#group 1 top edge
rewrite['R']=list('RrDdDlWdRrDdDlMiMiMiNuNuNuNoZdZrQoQdDdIiIiRuNuNuNoOoBlZdZdBiRrRrRrRoBuVuVlBiIiDdDdDdRoOoOuNuMiMrVuViDdDdDdDoQoQoQlNuNrRuWlNuNrR')
rewrite['L']=flipx(rewrite['R'])
rewrite['I']=flipL(rewrite['L'])
rewrite['O']=flipR(rewrite['L'])
#mirrors
rewrite['B']=flipz(rewrite['L'])
rewrite['C']=flipz(rewrite['R'])
rewrite['F']=flipx(rewrite['I'])
rewrite['G']=flipx(rewrite['O'])

#group 2 bottom edge
rewrite['M']=flipy(rewrite['F'])
rewrite['E']=flipL(rewrite['M'])
rewrite['W']=flipx(rewrite['E'])
rewrite['P']=flipR(rewrite['W'])#so far useless
rewrite['Q']=flipx(rewrite['P'])
#mirrors
rewrite['H']=flipz(rewrite['W'])
rewrite['J']=flipz(rewrite['E'])
rewrite['T']=flipx(rewrite['M'])

#group 3 up
rewrite['U']=flipCW(rewrite['W'])
rewrite['N']=flipx(rewrite['U'])
rewrite['V']=flipz(rewrite['U'])
rewrite['X']=flipz(rewrite['N'])

#group 4 down
rewrite['D']=flipy(rewrite['U'])
rewrite['S']=flipx(rewrite['D'])
rewrite['Z']=flipz(rewrite['S'])
rewrite['Y']=flipz(rewrite['D'])

rewrite['o']=['o']
rewrite['i']=['i']
rewrite['r']=['r']
rewrite['d']=['d']
rewrite['u']=['u']
rewrite['l']=['l']

symbols=list('R')
#symbols=list('SdSrTiTlXuXrGoGl')
