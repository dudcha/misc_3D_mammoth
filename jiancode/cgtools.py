#some tools that help the curvegenerator
from numpy import array
#dictionary of movelists
mlists={}
#4	2x2
mlists['hilbert']=list('rdl')
#8	2x2x2
mlists['hilbert3D']=list('rdlorul')
#9	3x3
mlists['peano']=list('rrdlldrr')
#27	3x3x3
mlists['peano3D']=list('rrdlldrrollurrullorrdlldrr')
mlists['peanomatic3x3x3']=list('rrdlldrrollurrullorrdlldrr')
#64	4x4x4
mlists['lego']=list('rdldrdlouruluruodldrdldoruluurdrurddldriuluruluidrdldrdilurulur')
#217	6x6x6
mlists['jigsaw3D']=list('rrrrdlllldrrirorrdllilolldrrrrrdlllllorrrrrulllllurrrrrulllllurrrrullllodrururdrdrdrdlddlulurululdldrdldluodrurulururdrdldrdruurululululdldluodddddruuuuurdddddruuuuurdddddruuuuoddddluuuullldddrrdllluuuuurrrrriiiidiu')

mlists['peanomatic']=list('rrdlldrr')#legacy, replaced by 3x3
mlists['peanomatic3x3']=list('rrdlldrr')

mlists['peanomatic4x4']=list('rrrdllldrrrdlll')
mlists['jigsaw1R']=list('drurrdldrdldlldrrdlldrrruuurdruuluruluuurddrdddddddruuuurrulluu')
mlists['jigsaw0R']=list('ruluurdrddruurrullluuullurrrdddruuuuurdddddruuurddrrdlldldrdldr')

def poslist(symblist):
	delta={}
	delta['F']=array([1,0,0])
	delta['l']=array([-1,0,0])
	delta['r']=array([1,0,0])
	delta['u']=array([0,-1,0])
	delta['d']=array([0,1,0])
	delta['i']=array([0,0,-1])
	delta['o']=array([0,0,1])

	position = array([0,0,0])
	out=[]
	out.append(list(position))
	counter=0
	for i in symblist:
#		if counter%1000000==0:
		position+=delta[i]
		out.append(list(position))
		counter+=1
	return out

plists={}
for key in mlists.keys():
	plists[key]=poslist(mlists[key])


#borrowed from main peano program for error-checking/visualization of the results
#pass in list of coordinates
def posarray(list,check=1):	#check means check if there are self-intersections
	from numpy import zeros
	dim=len(list[0])
	bounds=[]
	for d in range(dim):
		bounds.append(min([item[d] for item in list]))
		bounds.append(max([item[d] for item in list]))
	minx,maxx,miny,maxy,minz,maxz=bounds
	out=zeros((1+maxz-minz,1+maxy-miny,1+maxx-minx),int)
	for i in range(len(list)):
		if check and out[list[i][2]-minz,list[i][1]-miny,list[i][0]-minx] != 0:
			return 'error'
		out[list[i][2]-minz,list[i][1]-miny,list[i][0]-minx]=i+1
	return out

