name='peano3D'

def flipX(list):
	out=[]
	flip={}
#	flip['l']=['l']
#	flip['r']=['r']
	flip['u']=['u']
	flip['d']=['d']
	flip['i']=['i']
	flip['o']=['o']

	flip['l']=['r']
	flip['r']=['l']

	flip['0']=['X']
	flip['X']=['0']

	flip['Y']=['XY']
	flip['XY']=['Y']

	flip['Z']=['ZX']
	flip['ZX']=['Z']

	flip['XYZ']=['YZ']
	flip['YZ']=['XYZ']

	for item in list:
		out.extend(flip[item])
	return out

def flipY(list):
	out=[]
	flip={}
	flip['l']=['l']
	flip['r']=['r']
#	flip['u']=['u']
#	flip['d']=['d']
	flip['i']=['i']
	flip['o']=['o']

	flip['u']=['d']
	flip['d']=['u']

	flip['0']=['Y']
	flip['Y']=['0']

	flip['X']=['XY']
	flip['XY']=['X']

	flip['Z']=['YZ']
	flip['YZ']=['Z']

	flip['XYZ']=['ZX']
	flip['ZX']=['XYZ']

	for item in list:
		out.extend(flip[item])
	return out

def flipZ(list):
	out=[]
	flip={}
	flip['l']=['l']
	flip['r']=['r']
	flip['u']=['u']
	flip['d']=['d']
#	flip['i']=['i']
#	flip['o']=['o']

	flip['i']=['o']
	flip['o']=['i']

	flip['0']=['Z']
	flip['Z']=['0']

	flip['X']=['ZX']
	flip['ZX']=['X']

	flip['Y']=['YZ']
	flip['YZ']=['Y']

	flip['XYZ']=['XY']
	flip['XY']=['XYZ']

	for item in list:
		out.extend(flip[item])
	return out

alphabet={}

alphabet['l']=['l']
alphabet['r']=['r']
alphabet['u']=['u']
alphabet['d']=['d']
alphabet['i']=['i']
alphabet['o']=['o']

alphabet['0']=list('oouiiuooriidoodiiroouiiuoo')

alphabet['X']=flipX(alphabet['0'])
alphabet['Y']=flipY(alphabet['0'])
alphabet['Z']=flipZ(alphabet['0'])

alphabet['XY']=flipX(flipY(alphabet['0']))
alphabet['ZX']=flipX(flipZ(alphabet['0']))
alphabet['YZ']=flipY(flipZ(alphabet['0']))
alphabet['XYZ']=flipX(flipY(flipZ(alphabet['0'])))

rewrite={}

rewrite['l']=['l']
rewrite['r']=['r']
rewrite['u']=['u']
rewrite['d']=['d']
rewrite['i']=['i']
rewrite['o']=['o']

rewrite['0']=['0','o','XY','o','0','u','ZX','i','YZ','i','ZX','u','0','o','XY','o','0','r','YZ','i','ZX','i','YZ','d','XY','o','0','o','XY','d','YZ','i','ZX','i','YZ','r','0','o','XY','o','0','u','ZX','i','YZ','i','ZX','u','0','o','XY','o','0']

rewrite['X']=flipX(rewrite['0'])
rewrite['Y']=flipY(rewrite['0'])
rewrite['Z']=flipZ(rewrite['0'])

rewrite['XY']=flipX(flipY(rewrite['0']))
rewrite['ZX']=flipX(flipZ(rewrite['0']))
rewrite['YZ']=flipY(flipZ(rewrite['0']))
rewrite['XYZ']=flipX(flipY(flipZ(rewrite['0'])))

symbols=list('0')

