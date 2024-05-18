## Comprehensive mapping of long-range interactions reveals folding principles of the human genome.
## Lieberman-Aiden E*, van Berkum NL*, Williams L, Imakaev M et al.
##
## Supplemental Codeset III: Contact Probabilities on Peano Curves.
## (c) 2009 Erez Lieberman-Aiden.
##
## This code can be used to construct finite iterations of various Peano Curves.
## It may be used to draw these curves and write their coordinates to file.
## It may also be used to compute long-range contact probability scalings.
##
## Seven different types of curves may be generated:
## (1) Peano Curve (2) Hilbert Curve (3) Symmetrized Peano Curves (4) Quadratic Gosper Curve
## (5) 3D Peano Curve (6) 3D Hilbert Curve (7) Randomized 3D Peano Curves
##
## Please Cite:
## Lieberman-Aiden E*, van Berkum NL*, Williams L, Imakaev M et al.
## Comprehensive mapping of long-range interactions reveals folding principles of the human genome. Science 2009 Oct 9;326(5950):289-93. PMID: 19815776
##
## This codebase was used to construct Figures S13-S19.
## An automated curve-fitting algorithm has been included in this version, which may lead to minor differences in the linear fits observed.
## To use the code, modify the parameters below, and then run the code.
## Log-log plots of contact probability, image files, and curve coordinates are produced.
##
## UPDATED to Python 3 and modified for use in the Aiden Lab 3D Mammoth 2024 Paper by Ishawnia Christopher

## __PARAMETERS__

## Output Directory. Please reset this to your local directory name.
output_directory= '/Users/ishawniachristopher/Downloads/AidenLab/diffused-curves/finalout/'

## The code will automatically produce and analyze the smallest curve of each type larger than the characteristic size.
## Good convergence to theorical estimates for contact probability scaling is obtained for curves at least 10M units (10**7) long.
characteristic_size=10**4

## Make output images of the various curves. Note that for large curves, this may crash or take a long time.
## 1=YES; 0=NO
makeimage=1

## Make output files listing the coordinates of the various curves. Note that for large curves, this may take a long time and generate a large file.
## 1=YES; 0=NO
makecoordinatefile=1

## Make output files exhibiting the contact probability scaling, as in the supplemental figures of the paper.
## 1=YES; 0=NO
makescalingfile=1

GLOBAL_Q = 0
GLOBAL_log = 0

###############################################
def loadcurve(curvename):
### This establishes the recursive grammar for the relevant curve. Each curve is represented by a series of symbols that have a geometrical interpretation;
### iterating the curve consists of replacing the symbols according to a given rule of replacement. An appropriate starting move is also chosen.
### For the 3D curves, reldict and relcasses contain a list of possible geometric interpretations of each symbol, making it possible to interpret the list
### of symbols stochastically. This can be used to generate an ensemble of related but distinct spacefilling curves.

#### A 3D Hilbert Curve (code can also create a randomized version)   
    if curvename=='Hilbert3D':
        print('hilbert3d')
        curve3d=1
        grammar={'I': [[0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0], [0, 0, 1]]}
        replacement={'I':['X3Z3','D','XY','L','XY','U','Y2','F','Y2','D','X3Y','R','X3Y','U','XZ']}

#### A 3D Peano Curve (code can also create a randomized version)   
    if curvename=='Peano3D' or curvename=='Peano3D_random':
        print('peano3d')
        curve3d=1
        grammar={'I': [[0, 0, -1], [0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 0, -1], [0, -1, 0], [0, 0, 1], [0, 0, 1], [1, 0, 0], [0, 0, -1], [0, 0, -1], [1, 0, 0], [0, 0, 1], [0, 0, 1], [0, -1, 0], [0, 0, -1],[0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 0, -1]]}
        replacement={'I':['I','D','X3Y','D','I','F','XY3','U','XZ','U','XY3','F','I','D','X3Y','D','I','L','X2','U','XZ3','U','X2','B','Z2','D','X3Z3','D','Z2','B','X2','U','XZ3','U','X2','L','I','D','X3Y','D','I','F','XY3','U','XZ','U','XY3','F','I','D','X3Y','D','I']}

#### This is the classic Hilbert Curve
    if curvename=='Hilbert':
        print('hilbert')
        curve3d=0
        grammar={'CL': [(1, 0), (0, -1), (-1, 0)], 'CR': [(-1, 0), (0, 1), (1, 0)], 'CD': [(0, 1), (-1, 0), (0, -1)], 'CU': [(0, -1), (1, 0), (0, 1)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
        replacement={'CU':['CL','D','CU','R','CU','U','CR'],'CL':['CU','R','CL','D','CL','L','CD'],'CD':['CR','U','CD','L','CD','D','CL'],'CR':['CD','L','CR','U','CR','R','CU'],'L':'L','R':'R','U':'U','D':'D'}

#### This is the classic Peano Curve        
    if curvename=='Peano':
        print('Peano')
        curve3d=0
        grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
        replacement={'WUR': ['WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR'], 'D': 'D', 'WDL': ['WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL'], 'L': 'L', 'WDR': ['WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR'], 'R': 'R', 'U': 'U', 'WUL': ['WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL']}

#### Symmetrized 3x3 Peano
    if curvename=='Sympeano':
        print('PeanoSym')
        curve3d=0
        grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(0, 1), (0, 1), (-1, 0), (0, -1), (0, -1), (-1, 0), (0, 1), (0, 1)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(0, -1), (0, -1), (1, 0), (0, 1), (0, 1), (1, 0), (0, -1), (0, -1)],'L':[(0,-1)],'R':[(0,1)],'U':[(1,0)],'D':[(-1,0)]}
        replacement={'WUR': ['WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR'], 'D': 'D', 'WDL': ['WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL'], 'L': 'L', 'WDR': ['WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR'], 'R': 'R', 'U': 'U', 'WUL': ['WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL']}

#### Quadratic Gosper Curve
    if curvename=='qGosper':
        print('qGosper')
        curve3d=0
        grammar={'DR': [[0,-1],[0,-1],[1,0],[0,1],[1,0],[0,-1],[1,0],[0,1],[0,1],[1,0],[0,-1],[0,-1],[0,-1],[1,0],[0,-1],[-1,0],[-1,0],[0,1],[-1,0],[-1,0],[0,-1],[1,0],[0,-1],[-1,0],[-1,0]]}
        grammar['UR']=revmoves(grammar['DR'])
        grammar['LD']=rotate2D(grammar['DR'])
        grammar['RD']=rotate2D(grammar['UR'])
        grammar['UL']=rotate2D(grammar['LD'])
        grammar['DL']=rotate2D(grammar['RD'])
        grammar['LU']=rotate2D(grammar['DL'])
        grammar['RU']=rotate2D(grammar['UL'])
        replacement={}
        replacement['DR']=['DR','DR','RD','UR','RU','DR','RD','UR','UL','RD','DR','DR','DL','RU','DL','LD','LD','UR','LD','LU','DL','RU','DR','LU','LU']
        replacement['UR']=revgosper(replacement['DR'])
        replacement['LD']=rotgosper(replacement['DR'])
        replacement['RD']=rotgosper(replacement['UR'])
        replacement['UL']=rotgosper(replacement['LD'])
        replacement['DL']=rotgosper(replacement['RD'])
        replacement['LU']=rotgosper(replacement['DL'])
        replacement['RU']=rotgosper(replacement['UL'])
    

    if curve3d==0:
        for key in grammar.keys():
                if len(grammar[key])>1:
                        startmove=key
                        break

        return grammar,replacement,startmove,{},{}

    elif curve3d==1:
        ### The main goal of this section is to apply symmetries to the underlying grammar and geometric interpretations, generating the entire algebraic group.
        directions={'L':[[-1,0,0]],'R':[[1,0,0]],'U':[[0,0,1]],'D':[[0,0,-1]],'F':[[0,-1,0]],'B':[[0,1,0]]}
        for entry in replacement['I']:
            string=expand(entry)
            for key in directions.keys():
                string=string.replace(key,'')
            if string=='' and len(entry)>1:
                sumdirection=[0,0,0]
                for letter in expand(entry):
                    sumdirection=[sumdirection[i]+directions[letter][0][i] for i in range(len(sumdirection))]
                directions[entry]=[sumdirection]


        allkeys=['I','X','X2','X3','Y','XY','X2Y','X3Y','Y2','XY2','X2Y2','X3Y2','Y3','XY3','X2Y3','X3Y3','Z','XZ','X2Z','X3Z','Z2','XZ2','X2Z2','X3Z2','Z3','XZ3','X2Z3','X3Z3']

        from copy import deepcopy
        olddirections=deepcopy(directions)
        start=0
        while directions!=olddirections or start==0:
            start=1
            dproducts={}
            print('directions.keys', directions.keys())
            print('allkeys', allkeys)
            for key1 in directions.keys():
                    for key2 in allkeys:
                            dproducts[(key1,key2)]=rotateop(directions[key1],expand(key2))

            dshortcuts={}
            for key in dproducts.keys():
                newdir=''
                if dproducts[key][0][0]>1:
                    newdir+='R'+ abs(dproducts[key][0][0])
                if dproducts[key][0][0]<-1:
                    newdir+='L'+ abs(dproducts[key][0][0])                                    
                if dproducts[key][0][1]>1:
                    newdir+='B'+ abs(dproducts[key][0][1])
                if dproducts[key][0][1]<-1:
                    newdir+='F'+ abs(dproducts[key][0][1])
                if dproducts[key][0][2]>1:
                    newdir+='U'+ abs(dproducts[key][0][2])
                if dproducts[key][0][2]<-1:
                    newdir+='D'+ abs(dproducts[key][0][2])
                if dproducts[key][0][0]==1:
                    newdir+='R'
                if dproducts[key][0][0]==-1:
                    newdir+='L'
                if dproducts[key][0][1]==1:
                    newdir+='B'
                if dproducts[key][0][1]==-1:
                    newdir+='F'
                if dproducts[key][0][2]==1:
                    newdir+='U'
                if dproducts[key][0][2]==-1:
                    newdir+='D'

                dshortcuts[key]=newdir
                directions[newdir]=dproducts[key]

            olddirections=deepcopy(directions)

        for direction in directions.keys():
            grammar[direction]=directions[direction]
            replacement[direction]=[direction]

        for key in allkeys[1:]:
            grammar[key]=rotateop(grammar['I'],expand(key))
            
        products={}
        for key1 in allkeys+directions.keys():
                for key2 in allkeys:
                        products[(key1,key2)]=rotateop(grammar[key1],expand(key2))
                        
        shortcuts={}
        for key1 in allkeys+directions.keys():
                for key2 in allkeys:
                        for refkey in allkeys+directions.keys():
                                if products[(key1,key2)]==grammar[refkey]:
                                        shortcuts[(key1,key2)]=refkey

        for key in allkeys:
            replacement[key]=[shortcuts[entry,key] for entry in replacement['I']]

        reldict={}
        relclasses={}
        for key in grammar:
                if len(grammar[key])>1:
                        relpos=tuple(movelist2poslist(grammar[key])[-1])
                        relclasses[relpos]=relclasses.get(relpos,[])+[key]
                        reldict[key]=relpos

        for key in grammar.keys():
                if len(grammar[key])>1:
                        startmove=key
                        break

        return grammar,replacement,startmove,reldict,relclasses

###############################################
def hilbertstep(symblist):
### This iterates a given list of symbols exactly once.
    
    newlist=[]
    for symb in symblist:
        newlist+=replacement[symb]
            
    return newlist


###############################################
def hilbertiter(symblist,steps):
### This iterates a given list of symbols a specified number of times.

    for step in range(steps):
        symblist=hilbertstep(symblist)

    return symblist


###############################################
def symblist2movelist(symblist):
### Interprets symbols as a series of geometric moves according to the grammar.

    movelist=[]
    for symb in symblist:
        movelist+=grammar[symb]

    return movelist


###############################################
def symblist2randmovelist(symblist):
### Interprets symbols as a series of geometric moves according to the 'stochastic' reldict grammar.

    from random import choice
    
    movelist=[]
    for symb in symblist:
        if symb in reldict.keys():
            randpick=choice(relclasses[reldict[symb]])
            movelist+=grammar[randpick]
        else:
            movelist+=grammar[symb]
    
    return movelist


###############################################
def movelist2poslist(movelist):
### Interprets a series of geometric moves as a series of spatial positions defining the final curve.

    dim=len(movelist[0])
    currpos=[0]*dim
    poslist=[[0]*dim]

    i=0
    for entry in movelist:

        i+=1
        if i%100000==0:
            print (i)
        
        for d in range(dim): #used to say xrange
            currpos[d]+=entry[d]
        poslist.append([entry for entry in currpos])

    return poslist


###############################################
def poslist2posarray(poslist):
### Creates a 2D array showing at what point a 2D curve reaches all points in the array. Useful for computing contact probabilities.

    from numpy import zeros
    minx,maxx,miny,maxy=poslist2bounds(poslist)
    print("OG Bounds", minx, maxx, miny, maxy)
    posarray=zeros((1+int(maxx-minx),1+int(maxy-miny)))
    for i in range(len(poslist)):
        posarray[int(poslist[i][0]-minx),int(poslist[i][1]-miny)]=i+1

    print ("old posarray")
    print(str(posarray))
    return posarray


###############################################
def poslist2bounds(poslist):
### Computes the smallest square in the first quadrant that can contain the entire curve, eg its extent in various directions.
    
    dim=len(poslist[0])
    bounds=[]
    for d in range(dim):
        bounds.append(min([entry[d] for entry in poslist]))
        bounds.append(max([entry[d] for entry in poslist]))        

    print(str(bounds) + str(len(bounds)))
    return bounds


###############################################
def poslist2image(poslist,tag,showends=0,lw=2,endsize=50,dpi=100,diff=0):
### Makes a picture of the curve
    
    bounds = poslist2bounds(poslist)
    minx,maxx,miny,maxy=bounds[0],bounds[1], bounds[2],bounds[3]

    from pylab import close,savefig,plot,axis,xlim,ylim,scatter
    close('all')

    a=axis('off')
    a=xlim([minx-1,maxx+1])
    a=ylim([miny-1,maxy+1])

    colors = ['r','orangered','orange','gold','yellow','greenyellow','lawngreen','limegreen','lightseagreen','dodgerblue','royalblue',
              'b','rebeccapurple','darkviolet','mediumorchid','violet']

    groups = len(poslist)//len(colors)   

    for i in range(len(colors)):
        start = (i*groups)-1
        end = (i+1)*groups;
        if i==0:
            start = 0
        if i==len(colors)-1:
            end = len(poslist)
        colorsection(poslist[start:end], colors[i], lw,diff)

    if showends==1:
        scatter([poslist[0][0],poslist[-1][0]],[poslist[0][1],poslist[-1][1]],s=endsize,color=['g','g'])

    if diff:   
        savefig(output_directory+curvename+str(iterationcount)+'Dotsdiff' + str(diff)+ ''+ tag +'.png',dpi=dpi)
    else:
        savefig(output_directory+curvename+str(iterationcount)+'' + tag +'.png',dpi=dpi)


###############################################
def poslist2projected(poslist,theta=1,rescale=.4):
### Computes a 2D projection of the 3D curve. Y-axis is rescaled, which is visually inaccurate but makes small iterations of the contour easier to see.
    
    from math import sin,cos
    
    newlist=[]
    for pos in poslist:
        newlist.append([pos[0]-(rescale*sin(theta)*pos[1]),pos[2]+(rescale*cos(theta)*pos[1])])

    return newlist


###############################################
def rotate(movelist,axnum,plusminus=1):
### Rotates a list of moves around an axis.
    
	newlist=[]
	for move in movelist:
		newmove=[0,0,0]
		newmove[axnum]=move[axnum]
		newmove[(axnum+1)%3]=plusminus*move[(axnum-1)%3]
		newmove[(axnum-1)%3]=-1*plusminus*move[(axnum+1)%3]
		newlist.append(newmove)
	return newlist


###############################################
def rotateop(movelist,string):
### Performs a series of rotations.
    
    axval={'X':0,'Y':1,'Z':2}
    print("str: ", string)
    print('movelist', movelist)
    for letter in string:
        movelist=rotate(movelist,axval[letter])

    return movelist


###############################################
def expand(string):
### Expands strings of operations using 'power'-like notation into a string of raw operations, eg 'X3Y2' --> 'XXXYY'.
    
	newstring=''
	for i in range(len(string)):
		if string[i] not in ['I']+[intval for intval in range(1,10) ]:
			newstring+=string[i]
		elif string[i]!='I':
			newstring+=string[i-1]*(int(string[i])-1)
	return newstring


###############################################
def poslist2posdict(poslist):
### A dictionary telling you where the 3D curve is along its length when it reaches a certain spatial position; serves as a 3D version of posarray.

    posdict={}
    minx,maxx,miny,maxy,minz,maxz=poslist2bounds(poslist)
    for i in range(len(poslist)):
        posdict[(poslist[i][0]-minx,poslist[i][1]-miny,poslist[i][2]-minz)]=i
    return posdict


###############################################
def reflectmoves(movelist,axis):
### Reflects moves along an axis.
    
    newlist=[]
    for move in movelist:
        newmove=[]
        for i in range(len(move)):
            if axis==i:
                newmove.append(-1*move[i])
            else:
                newmove.append(move[i])
        newlist.append(newmove)
        
    return newlist


###############################################
def flipmoves(movelist):
### Flips a series of moves.
	newlist=[]
	for move in movelist:
		newlist.append([move[1],move[0]])
	return newlist


###############################################
def revmoves(movelist):
### Reverses a series of moves.
	newlist=[]
	for move in movelist[::-1]:
		newlist.append([-1*move[0],-1*move[1]])
	return newlist


###############################################
def rotate2D(movelist):
### Performs 2D rotation on a series of moves.    
    newlist=[]
    for move in movelist:
        newlist.append(move+[0])
    rotlist=rotate(newlist,2)
    newrotlist=[[entry[0],entry[1]] for entry in rotlist]
    
    return newrotlist


###############################################
def revgosper(symblist):
### A custom reversal operation for the gosper curve.
    
    newlist=[]
    for symb in symblist[::-1]:
        newsymb=''
        newsymb+=symb[0].replace('R','l').replace('L','r').replace('U','d').replace('D','u').replace('l','L').replace('r','R').replace('u','U').replace('d','D')
        newsymb+=symb[1]
        newlist.append(newsymb)
        
    return newlist


###############################################
def rotgosper(symblist):
### A custom rotation operation for the gosper curve.
    
    rotdict={'DR':'LD','UR':'RD','LD':'UL','RD':'DL','DL':'LU','UL':'RU','LU':'UR','RU':'DR'}
    newlist=[]
    for symb in symblist:
        newlist.append(rotdict[symb])
        
    return newlist


###############################################
def printcurve(poslist,diff=0):
### Prints a given iteration of the chosen curve out to file.

    curvelen=len(poslist)
    if diff:
        # Name of file is first letter of curve + diff + amount diffused by
        output1=open(output_directory+curvename[:1]+'diff'+str(diff)+'.txt','w')
    else:
        # Name of file is curve name + curve length
        output1=open(output_directory+curvename+'.'+ str(curvelen) +'.txt','w')
    for entry in poslist:
            for coord in range(len(entry)):
                    if coord!=len(entry)-1:
                            output1.write('{'+str(entry[coord])+',\t')
                    else:
                            output1.write(str(entry[coord])+'},\n')
    output1.close()


###############################################
def poslist2contactlists(poslist):    
### Given a poslist, creates a list of contacts (=lattice adjacency) at various distances along the chain.

    if len(poslist[0])==2:
        posarray=poslist2posarray(poslist)
        strandsize=int(posarray.max())
        from numpy import zeros
        dists=zeros(strandsize)
        for i in range(posarray.shape[0]):
            for j in range(posarray.shape[1]):
                if posarray[i][j]!=0:
                    valref=posarray[i][j]
                    comparevals=[]
                    if i>0 and posarray[i-1][j]!=0:
                            comparevals.append(posarray[i-1][j])
                    if j>0 and posarray[i][j-1]!=0:
                            comparevals.append(posarray[i][j-1])
                    for val in comparevals:
                            dists[int(abs(valref-val))]+=1
        possdists=[0]+[strandsize-i for i in range(1,strandsize)]
        print("Possdists:" + str(possdists)+ "\n")
        print("dists:" + str(dists)+ "\n")


    elif len(poslist[0])==3:

        posdict=poslist2posdict(poslist)
        from numpy import zeros
        strandsize=len(posdict)
        dists=zeros(strandsize)
        bounds=poslist2bounds(posdict.keys())
        for i in range(bounds[1]+1):
                for j in range(bounds[3]+1):
                        for k in range(bounds[5]+1):
                                valref=posdict[(i,j,k)]
                                comparevals=[]
                                if i>0:
                                        comparevals.append(posdict[(i-1,j,k)])
                                if j>0:
                                        comparevals.append(posdict[(i,j-1,k)])
                                if k>0:
                                        comparevals.append(posdict[(i,j,k-1)])
                                for val in comparevals:
                                        dists[abs(valref-val)]+=1
        possdists=[strandsize-i for i in range(strandsize)]

    return dists,possdists


###############################################
def diststats2plot(dists,poslist,possdists,diff=0):    
### Computes long range contact stats for the curve, using posarray as input.

    from math import log
    from numpy import arange,zeros, polyfit
    from matplotlib.pyplot import close,savefig,plot,close,plot,savefig,legend,xlabel,ylabel,title

    
    logbase=int((1+len(grammar[startmove]))**(1./len(poslist[0])))
    # logbase = 2
    top=log(len(poslist),logbase)+1

    lbins=arange(0,top,1)
    binact=zeros(len(lbins))
    binposs=zeros(len(lbins))
    currbin=0
    for i in range(1,len(dists)):
        while log(i,logbase)>lbins[currbin]:
                currbin+=1
        binact[currbin]+=dists[i]
        binposs[currbin]+=possdists[i]
    
    startval=0
    for i in range(len(binact)-1):
        if binact[i]==0:
            startval=i

    stopval=len(binact)
    if binact[-1]==0:
        stopval=len(binact)-1

    ratioindex=range(startval+1,stopval)
    ratio=[log(float(binact[i])/binposs[i],logbase) for i in range(startval+1,stopval)]
    
    # Finds a polynomial fit of degree 1
    print("Fitting...")
    fitall=polyfit(ratioindex[1:-1],ratio[1:-1],1)

    close('all')
    a=plot(ratioindex,ratio,label='actual')

    print(fitall)

    slope, intercept = fitall  # Assuming fitall is a tuple with two elements, the coefficients ax+b
    
    a=plot(ratioindex[1:-1],[intercept+(slope*i) for i in ratioindex[1:-1]],'r--',label='Slope: '+ str(slope))
    a=xlabel('Distance (log '+ str(logbase) +')')
    a=ylabel('Contact Probability (log '+ str(logbase) +')')
    a=legend()

    if diff:   
        savefig(output_directory+'Scaling.'+curvename+'diff' + str(diff)+ '.' +'log'+ str(logbase) +'.png')
    else:
        savefig(output_directory+'Scaling.'+curvename+'.'+'log'+ str(logbase) +'.png')




##################### Ishawnia 2023-2024 Functions ##########################


#######################################
def diffuseposlist(coords, range):
### Takes array of coordinates from poslist and returns a "diffused" array of those coords

	import random
	diffcoords=[]
	for coord in coords:
		if len(coord)==3:
			dc = [0,0,0]
			dc[2] = coord[2] + random.uniform(-1*range,range)
		else:
			dc = [0,0]
		dc[0] = coord[0] + random.uniform(-1*range,range)
		dc[1] = coord[1] + random.uniform(-1*range,range)
		diffcoords.append(dc)
	return diffcoords


#######################################
def colorsection(positions, color='',lw=2, diff=0):
### Ishawnia: plots positions coordinates with given color

    from pylab import plot,scatter
    index0=[entry[0] for entry in positions]
    index1=[entry[1] for entry in positions]
    
    if diff:
        #a=plot(index0, index1, color, lw )
        a=scatter(index0, index1, 2, color, marker='o')
    else:
        a=plot(index0, index1, color, lw )
        #a=scatter(index0, index1, 2, color, marker='o')



#######################################
def diststats2plotconditions(dists,poslist,possdists,diff=0):    
### Ishawnia: Computes & returns long range contact stats for the diffused curve

    from math import log
    from numpy import arange,zeros, polyfit
    from matplotlib.pyplot import close,savefig,plot,close,plot,savefig,legend,xlabel,ylabel,title


    print('cuvy name ' + curvename)
    if curvename == 'Dragon':
        logbase = 2
    else:
        if '2D Random Walk' in curvename:
            print("skdfjlskdfslkjs")
            logbase = 2
        else:
            logbase=int((1+len(grammar[startmove]))**(1./len(poslist[0])))

    top=log(len(poslist),logbase)+1

    lbins=arange(0,top,1)
#     print("lbins"+ str(lbins) +"\n")
    binact=zeros(len(lbins))
#     print("binact b4"+ str(binact) +"\n")
    binposs=zeros(len(lbins))
#     print("binposs b4"+ str(binposs) +"\n")
    currbin=0
    for i in range(1,len(dists)):
        while log(i,logbase)>lbins[currbin]:
                currbin+=1
        binact[currbin]+=dists[i]
        binposs[currbin]+=possdists[i]
    
#     print("binact af"+ str(binact) +"\n")

#     print("binposs af"+ str(binposs) +"\n")

    startval=0
    for i in range(len(binact)-1):
        if binact[i]==0:
            startval=i

    stopval=len(binact)
    if binact[-1]==0:
        stopval=len(binact)-1

    ratioindex=range(startval+1,stopval)

    ratio=[log(float(binact[i])/binposs[i],logbase) for i in ratioindex]

    fitall=polyfit(ratioindex[1:-1],ratio[1:-1],1)

    print("Fitall"+str(fitall))

    slope, intercept = fitall  # Assuming fitall is a tuple with two elements

    return ratioindex,ratio,intercept,slope,logbase

#######################################
def fileToCoords(filename):
# ChatGPT: To create array of coordinates read from a file
 
    # Initialize an empty list to store the coordinates
    coordinates = []
    
    # Specify the path to the text file
    file_path = "/Users/ishawniachristopher/Documents/AidenLab/jiancodeupdated/" + filename

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read each line and parse the coordinates
            for line in file:
                # Split the line into components using a comma as the delimiter
                components = line.strip().split('	')
                
                # Convert the components to floating-point numbers and create a tuple
                if len(components) >= 3:
                    x, y, z = map(float, components[:3])  # Assuming 3D coordinates
                    coordinates.append((x, y, z))
                elif len(components) >= 2:
                    x, y = map(float, components[:2])  # Assuming 2D coordinates
                    coordinates.append((x, y))

        # Print the read coordinates
        for coord in coordinates:
            print(coord)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return coordinates

#######################################
def combinedPlotHil(plotconditions,diffs,A):
    # Ishawnia: plots both the predicted and actual scaling probabilities for Hilbert curve and relevant data ranges.
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.pyplot import close,savefig,plot,close,savefig,legend,xlabel,ylabel,title,loglog

    plt.close('all')

    plt.ylim(-23, 2)   # Set x-axis limits
    plt.xlim(1, 14)      # Set y-axis limits
    plt.xticks([3.32, 6.64, 9.96 , 13.28], ['10', '100', '1000', '10000'])
    plt.yticks([-20, -15, -10 , -5, 0], ['$2^{-20}$,', '$2^{-15}$', '$2^{-10}$', '$2^{-5}$', '0'])
    ss = np.logspace(2**1, 13.5, 100, base=2)

    gamma = -3/2
    j = 0
    
    t = 0
    for elem in plotconditions:
            q = diffs[j]
            xrange = elem[0][1:-1]
            yrange = elem[1][1:-1]

            base = elem[4]
            gamma = -3/2
            Dt = (4/3) * (q**2) / 8
            expression = [s**gamma * (A**(-2/3) + 8 * Dt * s**(2*gamma/3))**(-3/2) for s in ss]

            plt.plot(np.log2(ss), np.log2(expression), '--',color=grphColors[j])
            plt.plot(xrange,yrange,color=grphColors[j],label=f'q={q}')

            print("hilbert x data" + str(q))
            print(xrange)

            print("hilbert y ex data"+ str(q))
            print(yrange)

            j+=1

    # Add labels and title
    plt.xlabel('Distance (monomers)')
    plt.ylabel('Contact Probability, simulated')
    plt.title(curvename)# + ' Curve - Model vs Actual\n Contact Probability Scalings with Different q Values')
    
    plt.legend()
    plt.savefig(output_directory+'AcombinedPlot.'+curvename[:1]+'.png')


#######################################
def combinedPlotRW(plotconditions,diffs,A,gamma=-1):
    # Ishawnia: plots both the predicted and actual scaling probabilities for a random 2D curve and relevant data ranges.
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.pyplot import close,savefig,plot,close,savefig,legend,xlabel,ylabel,title,loglog

    plt.close('all')

    plt.ylim(-23, 2)   # Set x-axis limits
    plt.xlim(1, 14)      # Set y-axis limits

    plt.xticks([3.32, 6.64, 9.96 , 13.28], ['10', '100', '1000', '10000'])
    plt.yticks([-20, -15, -10 , -5, 0], ['$2^{-20}$,', '$2^{-15}$', '$2^{-10}$', '$2^{-5}$', '0'])

    ss = np.logspace(2**1, 13.5, 100, base=2)
    j = 0
    base = 0
    
    print("in rw")
    t = 0
    for elem in plotconditions:
            q = diffs[j]
            xrange = elem[0][1:-1]
            yrange = elem[1][1:-1]

            base = elem[4]
            Dt = (4/3) * (q**2) / 8
            expression = [s**gamma * (A**(-2/3) + 8 * Dt * s**(2*gamma/3))**(-3/2) for s in ss]

            a=plot(np.log2(ss), np.log2(expression), '--',color=grphColors[j])
            a=plot(xrange,yrange,color=grphColors[j],label=f'q={q}')
            j+=1

    # Add labels and title
    plt.xlabel('Distance (monomers)')
    plt.ylabel('Contact Probability, simulated')
    plt.title(curvename) # 2D Random Walk 160000 Curve - Model vs Actual\n Contact Probability Scalings with Different q Values')
    
    plt.legend()
    plt.savefig(output_directory+'AcombinedPlot.'+'RW'+'.png')

#######################################  
def combinedPlotDra(plotconditions,diffs,A,gamma=-1.2383):
    # Ishawnia: plots both the predicted and actual scaling probabilities for dragon curve and relevant data ranges.
    import matplotlib.pyplot as plt
    import numpy as np

    plt.close('all')
    ss = np.logspace(2**1, 13.5, 100, base=2)
    j = 0
    base = 0
    
    print("in drag")
    for elem in plotconditions:
            q = diffs[j]
            xrange = elem[0][1:-1]
            yrange = elem[1][1:-1]

            base = elem[4]
            print('nnh' + str(base))
            Dt = (4/3) * (q**2) / 8
            expression = [s**gamma * (A**(-2/3) + 8 * Dt * s**(2*gamma/3))**(-3/2) for s in ss]

            print("dragon x data" + str(q))
            print(xrange)

            print("dragon y ex data"+ str(q))
            print(yrange)

            plt.plot(np.log2(ss), np.log2(expression), '--',color=grphColors[j])
            plt.plot(xrange,yrange,color=grphColors[j],label=f'{q}')
            j+=1

    # Add labels and title
    plt.xlabel('Distance (monomers)')
    plt.ylabel('Contact Probability, simulated')
    plt.title(curvename)#plt.title('Dragon - Model vs Actual\n Contact Probability Scalings with Different q Values')
    
    plt.legend()
    plt.savefig(output_directory+'AcombinedPlot.'+'D'+'.png')



####################################### 
def combinedPlotPea(plotconditions,diffs,A):
    # Ishawnia: plots both the predicted and actual scaling probabilities for peano curve and relevant data ranges.
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.pyplot import close,savefig,plot,close,savefig,legend,xlabel,ylabel,title,loglog

    plt.close('all')

    plt.ylim(-15, -1)   # Set x-axis limits
    plt.xlim(1, 10)      # Set y-axis limits
    plt.xticks([2.09, 4.19, 6.28 , 8.38], ['10', '100', '1000', '10000'])
    plt.yticks([-14, -10, -6 , -2], ['$3^{-14}$,', '$3^{-10}$', '$3^{-6}$', '$3^{-2}$'])

    ss = np.logspace(3**0.5, 9.5, 100, base=3)

    gamma = -3/2
    j = 0
    
    print("in combined")
    t = 0
    for elem in plotconditions:
            q = diffs[j]
            xrange = elem[0][1:-1]
            yrange = elem[1][1:-1]

            base = elem[4]
            Dt = (4/3) * (q**2) / 8
            expression = [s**gamma * (A**(-2/3) + 8 * Dt * s**(2*gamma/3))**(-3/2) for s in ss]
            expressionlog3 = np.log(expression) / np.log(3)
            sslog3 = np.log(ss) / np.log(3)
            a=plot(sslog3, expressionlog3, '--',color=grphColors[j])
            a=plot(xrange,yrange,color=grphColors[j],label=f'q={q}')
            j+=1

            print("peano x data" + str(q))
            print(xrange)

            print("peano y ex data"+ str(q))
            print(yrange)

    # Add labels and title
    plt.xlabel('Distance (monomers)')
    plt.ylabel('Contact Probability, simulated')
    plt.title(curvename)#+ ' Curve - Model vs Actual\n Contact Probability Scalings with Different q Values')
    
    
    plt.legend()
    plt.savefig(output_directory+'AcombinedPlot.'+curvename[:1]+'.png')


####################################### 
def combinedPlotSym(plotconditions,diffs,A):
    # Ishawnia: plots both the predicted and actual scaling probabilities for symmetric peano curve and relevant data ranges.
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.pyplot import close,savefig,plot,close,savefig,legend,xlabel,ylabel,title,loglog

    plt.close('all')

    plt.ylim(-15, -1)   # Set x-axis limits
    plt.xlim(1.25, 9.5)      # Set y-axis limits

    plt.xticks([2.09, 4.19, 6.28 , 8.38], ['10', '100', '1000', '10000'])
    plt.yticks([-14, -10, -6 , -2], ['$3^{-14}$,', '$3^{-10}$', '$3^{-6}$', '$3^{-2}$'])

    ss = np.logspace(3**0.5, 9, 100, base=3)

    gamma = -3/2
    j = 0
    
    print("in combined")
    t = 0
    for elem in plotconditions:
            q = diffs[j]
            xrange = elem[0][1:-1]
            yrange = elem[1][1:-1]
               
            base = elem[4]
            Dt = (4/3) * (q**2) / 8
            expression = [s**gamma * (A**(-2/3) + 8 * Dt * s**(2*gamma/3))**(-3/2) for s in ss]
            expressionlog3 = np.log(expression) / np.log(3)
            sslog3 = np.log(ss) / np.log(3)
            a=plot(sslog3, expressionlog3, '--',color=grphColors[j])
            a=plot(xrange,yrange,color=grphColors[j],label=f'q={q}')
            j+=1

            print("sympeano x data" + str(q))
            print(xrange)

            print("sympeano y ex data"+ str(q))
            print(yrange)

    # Add labels and title
    plt.xlabel('Distance (monomers)')
    plt.ylabel('Contact Probability, simulated')
    plt.title('Symmetric Peano')# + ' Curve - Model vs Actual\n Contact Probability Scalings with Different q Values')
    
    plt.legend()
    plt.savefig(output_directory+'AcombinedPlot.'+curvename[:1]+'.png')


####################################### 
def combinedPlotqGo(plotconditions,diffs,A,gamma=-1.3174):
    # Ishawnia: plots both the predicted and actual scaling probabilities for quadratic gosper curve and relevant data ranges.
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.pyplot import close,savefig,plot,close,savefig,legend,xlabel,ylabel,title,loglog

    plt.close('all')

    plt.ylim(-8.5, -1)   # Set x-axis limits
    plt.xlim(1.5, 5.5)      # Set y-axis limits

    ss = np.logspace(5**0.35, 5.25, 100, base=5)

    plt.xticks([1.43, 2.86, 4.29 , 5.72], ['10', '100', '1000', '10000'])
    plt.yticks([-8, -6 , -4, -2], ['$5^{-8}$,', '$5^{-6}$', '$5^{-4}$', '$5^{-2}$'])

    j = 0
    
    print("in combined")
    t = 0
    for elem in plotconditions:
            q = diffs[j]
            xrange = elem[0][1:-1]
            yrange = elem[1][1:-1]
              
            base = 5
            Dt = (4/3) * (q**2) / 8
            expression = [s**gamma * (A**(-2/3) + 8 * Dt * s**(2*gamma/3))**(-3/2) for s in ss]
            expressionlog5 = np.log(expression) / np.log(5)
            sslog5 = np.log(ss) / np.log(5)
            a=plot(sslog5, expressionlog5, '--',color=grphColors[j])
            a=plot(xrange,yrange,color=grphColors[j],label=f'q={q}')
            j+=1

    # Add labels and title
    plt.xlabel('Distance (monomers)')
    plt.ylabel('Contact Probability, simulated')
    plt.title('Quadratic Gosper')# + ' Curve - Model vs Actual\n Contact Probability Scalings with Different q Values')
    
    plt.legend()
    plt.savefig(output_directory+'AcombinedPlot.'+curvename[:1]+'.png')

####################################### 
def diffposlist2posarray(diffpos):
    from numpy import zeros
    from ScienceSupplemental  import poslist2bounds
    print("in new diff array func\n")
    minx, maxx, miny, maxy = poslist2bounds(diffpos)
    print("Bounds",minx, maxx, miny, maxy)
    posarray = [[[] for _ in range(1 + int(maxy - miny))] for _ in range(1 + int(maxx - minx))]
    print("bob")
    for idx, position in enumerate(diffpos):
        print(idx, position)
        x, y = position
        posarray[int(x - minx)][int(y - miny)].append(idx)
    print("new posarray")
    print (posarray)
    return posarray

####################################### 
def diffposlist2contactlist(diffpos):
    print("in new diff func\n")
    posarray = diffposlist2posarray(diffpos)
    strandsize = len(diffpos)
    from numpy import zeros
    dists = zeros(strandsize)
    for i in range(len(posarray)):
        for j in range(len(posarray[0])):
            segments_in_tile = posarray[i][j]
            adjacent_segments = []
            # Check left
            if i > 0:
                adjacent_segments.extend(posarray[i-1][j])
            # Check above
            if j > 0:
                adjacent_segments.extend(posarray[i][j-1])
            # Calculate all possible contacts
            for seg1 in segments_in_tile:
                for seg2 in adjacent_segments + segments_in_tile:
                    if seg1 != seg2:
                        dists[abs(seg1 - seg2)] += 1
    possdists = [strandsize - i for i in range(strandsize)]
    print("Diff Possdists:" + str(possdists)+ "\n")
    print("Diff dists:" + str(dists)+ "\n")
    return dists, possdists

def newposarray2list(poslist):
    from numpy import zeros
    from ScienceSupplemental  import poslist2bounds
    minx, maxx, miny, maxy = poslist2bounds(poslist)
    posarray = [[[] for _ in range(1 + int(maxy - miny))] for _ in range(1 + int(maxx - minx))]
    for idx, position in enumerate(poslist):
        x, y = position
        posarray[int(x - minx)][int(y - miny)].append(idx)
    return posarray

def add_contact(seg1, seg2, contact_set, dists):
    # Ensure a consistent order for the segments
    seg1, seg2 = sorted([seg1, seg2])
    # If this contact hasn't been recorded yet, add it
    if (seg1, seg2) not in contact_set:
        contact_set.add((seg1, seg2))
        dists[abs(seg1 - seg2)] += 1

def newdiff2contacts(poslist):
    posarray = newposarray2list(poslist)
    strandsize = len(poslist)
    from numpy import zeros
    dists = zeros(strandsize)
    contact_set = set()
    
    for i in range(len(posarray)):
        for j in range(len(posarray[0])):
            segments_in_tile = posarray[i][j]
            adjacent_segments = []
            
            # Check left
            if i > 0:
                adjacent_segments.extend(posarray[i-1][j])
            # Check above
            if j > 0:
                adjacent_segments.extend(posarray[i][j-1])
            
            # Check contacts within the same cell
            for idx1, seg1 in enumerate(segments_in_tile):
                for seg2 in segments_in_tile[idx1+1:]:
                    add_contact(seg1, seg2, contact_set, dists)
            
            # Check contacts with adjacent cells
            for seg1 in segments_in_tile:
                for seg2 in adjacent_segments:
                    add_contact(seg1, seg2, contact_set, dists)
    
    possdists = [strandsize - i for i in range(strandsize)]
    return dists, possdists


# 2D Random Walk Function
def random_walk_2D(steps):
    import random
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    poslist = [(0, 0)]
    for _ in range(steps):
        dx, dy = random.choice(directions)
        x, y = poslist[-1]
        poslist.append((x + dx, y + dy))
    return poslist


# Dragon Curve Generation
def generate_dragon_curve(iterations):
    dragon = "R"
    nogard = "L"
    for i in range(iterations):
        temp_dragon = dragon
        dragon += "R"
        dragon += nogard
        nogard = temp_dragon + "L" + nogard
    print("hi\n"+dragon)
    return dragon

def recDragonCurve(iter):
     if iter == 1:
          print('R')
          return 'R'
     else:
          half = recDragonCurve(iter-1)
          secondhalf = ''
          for letter in half:
               if letter == 'R':
                    secondhalf+= 'L'
               else:
                    secondhalf+='R'
          secondhalf = ''.join(reversed(secondhalf))
          full = half+'R'+secondhalf
          print(full)
          return full
          

# Dragon Curve to Poslist
def dragon_to_poslist(dragon_curve):
    x, y = 0, 0
    poslist = [(x, y)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    for move in dragon_curve:
        if move == "R":  # Right turn
            direction_index = (direction_index + 1) % 4  # Cycle through directions
        elif move == "L":  # Left turn
            direction_index = (direction_index - 1) % 4
        else:
            continue  # Skip invalid turns

        dx, dy = directions[direction_index]  # Get the new direction
        x += dx  # Update x coordinate
        y += dy  # Update y coordinate
        poslist.append((x, y))
    return poslist

# Define your theoretical function
def theory(ss: any, gamma: float, A: float, x: float):
    import numpy as np
    
    thry = []
    q = GLOBAL_Q
    log = GLOBAL_log

    # Define the theoretical function from the paper
    Dt = (4/3) * ((q*x)**2) / 8
    print("in theory", q)
    for s in ss:
        ay = A**(-2/3)
        term = ay + 8 * Dt * s**(2*gamma/3)
        thry.append(s**gamma * (term)**(-3/2))
    
    # Return the log_2
    return np.log(thry)/np.log(log)

###### function to find fitted parametes A and gamma for the Hilbert curve ####
def fittedHil(diffs, curve):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    # Close other plots
    plt.close('all')

     # Set axis limits
    plt.ylim(-23, 2)
    plt.xlim(1, 14)     

    # Set tick marks
    plt.xticks([3.32, 6.64, 9.96 , 13.28], ['10', '100', '1000', '10000'])
    plt.yticks([-20, -15, -10 , -5, 0], ['$2^{-20}$,', '$2^{-15}$', '$2^{-10}$', '$2^{-5}$', '0'])

    # Set up the x values and diffused curve contact probabilities
    oldx_data = np.logspace(2**1, 13.5, 12, base=2)
    oldx_data = np.log2(oldx_data)
    experiments = [[-4.447238768615319, -5.6579361266895765, -7.447094249625348, -8.65587299039279, -10.444583098455224, -11.643099021497305, -13.442177243680591, -14.608763049087607, -16.398500793538616, -17.3784574344716, -19.32185764907369],
                    [-2.657895001774582, -4.4448386764948316, -5.654602983025459, -7.440377333410768, -8.652537277829536, -10.436888706665222, -11.647558669688005, -13.442177243680591, -14.599774265860354, -16.398500793538616, -17.3784574344716, -19.277463529715234],
                      [-2.6567837403748364, -4.446758430658197, -5.6557131754933945, -7.424193847515269, -8.638170988659333, -10.402762922760596, -11.614442562874236, -13.388310371701857, -14.590841141090344, -16.390326862092916, -17.351657375127886, -19.34457772557377],
                        [-2.5627200291173384, -4.022147604672552, -5.204889245920304, -6.60928553102603, -8.072395507858223, -9.481702554015921, -10.834472442203651, -12.72972500783752, -13.697071467215267, -15.595837566805734, -16.628923166802338, -18.3911203115108],
                          [-4.683410242420191, -4.887639792371458, -5.162453979599907, -5.6130572849152385, -6.395345440169573, -7.568624362398595, -9.01464222995113, -10.497624313359506, -11.872022893634398, -13.259879912014313, -14.343933559137207, -16.237049261269327],
                            [-6.565063546529687, -6.688814746512942, -6.687150575936316, -6.938496574184167, -7.160856954915398, -7.580496291299063, -8.39587474718092, -9.54236062321911, -10.913882856288417, -12.339771056418956, -13.617571191686688, -15.214640573482304]]
    params = []

    # Get the plots for each diffusion q range
    for i in range(len(diffs)):

        # Get our calculated y values from our diffused curve
        y_experimental = experiments[i]

        # Set the diffusion range q variable
        setQ(diffs[i])

        # Get correct range of xdata that matches the length of the corresponding experimental data
        x_data = oldx_data
        if (len(y_experimental) != len(oldx_data)):
             x_data = oldx_data[:len(y_experimental)]

        # Get our initial theory y values using our initial gamma and A values
        y_theoretical = theory(2**(x_data), -1.5, 1, 1)  # Use some example parameters

        # Fit the experimental data to the theoretical function
        initial_guess = [ -1.5, 1, 1]
        fit_params, covariance = curve_fit(theory, 2**(x_data), y_experimental, p0=initial_guess)
        
        # Print the fitted parameters
        print("Fitted Parameters:", fit_params)

        # Plot the results
        plt.scatter(x_data, y_experimental, label='Actual '+ str(diffs[i]), color=grphColors[i])
        plt.plot(x_data, y_theoretical, label='Initial Theory '+ str(diffs[i]),linestyle='--',  color=grphColors[i])
        plt.plot(x_data, theory(2**(x_data), *fit_params), label='Fitted '+ str(diffs[i]) + " " + str(fit_params), color=grphColors[i])
        
        # Add labels and title
        plt.title(curve)
        plt.xlabel('Distance (monomers)')
        plt.ylabel('Contact Probability, simulated')
        params.append(fit_params)
    
    # Show the graph
    plt.legend(fontsize=5)
    plt.savefig(output_directory+"fitted"+curve+".png")
    return fit_params, covariance

###### function to find fitted parametes A and gamma for the Peano curve ####
def fittedPea(diffs, curve):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    # Close other plots
    plt.close('all')

     # Set axis limits
    plt.ylim(-15, -1)
    plt.xlim(1, 10)    

    # Set tick marks
    plt.xticks([2.09, 4.19, 6.28 , 8.38], ['10', '100', '1000', '10000'])
    plt.yticks([-14, -10, -6 , -2], ['$3^{-14}$,', '$3^{-10}$', '$3^{-6}$', '$3^{-2}$'])

    # Set up the x values and diffused curve contact probabilities
    oldx_data = np.logspace(3**0.5, 9.5, 8, base=3)
    oldx_data = np.log(oldx_data)/np.log(GLOBAL_log)
    experiments = [[-2.8927044729329663, -4.261713030712788, -5.2611577481341, -7.260600590278552, -8.25557852525374, -10.25040190350377, -11.203105689447085, -13.14030408590523],
                    [-2.8871718341397647, -4.254434394944578, -5.261065248847742, -7.245445659469519, -8.25446780000716, -10.24871783414896, -11.203105689447085, -13.134702596064043],
                      [-2.8679481867142425, -4.25931109895342, -5.245111816156595, -7.256718967225139, -8.23824011099498, -10.249559479356062, -11.196388026288075, -13.137499032139498],
                        [-2.317065541330808, -3.9579570940919653, -4.806791244288973, -6.80433755925281, -7.7626964760121115, -9.721482858719817, -10.720602948636635, -12.741749829398387],
                          [-3.087272440920234, -3.4794359437147393, -4.09725948411251, -5.61156035969267, -6.48231268223849, -8.456564511953815, -9.284147585017301, -11.241913335349672],
                            [-4.152223873881251, -4.319078178568505, -4.5474762109613645, -5.261619947116356, -6.142773114577048, -7.947348071433917, -8.71270065938102, -10.63467341302699]]

    # Get the plots for each diffusion q range
    for i in range(len(diffs)):

        # Get our calculated y values from our diffused curve
        y_experimental = experiments[i]

        # Set the diffusion range q variable
        setQ(diffs[i])

        # Get correct range of xdata that matches the length of the corresponding experimental data
        x_data = oldx_data
        if (len(y_experimental) != len(oldx_data)):
             x_data = oldx_data[:len(y_experimental)]

        # Get our initial theory y values using our initial gamma and A values
        y_theoretical = theory(GLOBAL_log**(x_data), -1.5, 1, 1)  # Use some example parameters

        # Fit the experimental data to the theoretical function
        initial_guess = [ -1.5, 1, 1]
        fit_params, covariance = curve_fit(theory, GLOBAL_log**(x_data), y_experimental, p0=initial_guess)
        
        # Print the fitted parameters
        print("Fitted Parameters:", fit_params)

        # Plot the results
        plt.scatter(x_data, y_experimental, label='Actual '+ str(diffs[i]), color=grphColors[i])
        plt.plot(x_data, y_theoretical, label='Initial Theory '+ str(diffs[i]),linestyle='--',  color=grphColors[i])
        plt.plot(x_data, theory(GLOBAL_log**(x_data), *fit_params), label='Fitted '+ str(diffs[i]) + " " + str(fit_params), color=grphColors[i])
       
        # Add labels and title
        plt.title(curve)
        plt.xlabel('Distance (monomers)')
        plt.ylabel('Contact Probability, simulated')

    
    # Show the graph
    plt.legend(fontsize=5)
    plt.savefig(output_directory+"fitted"+curve+".png")
    return fit_params, covariance

###### function to find fitted parametes A and gamma for the symmetric peano curve ####
def fittedSym(diffs, exp, curve, xdata, xtick, xlab, xrange, ytick, ylab, yrange): 
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    # Close other plots
    plt.close('all')

     # Set axis limits
    if xrange != None:
        plt.xlim(xrange[0], xrange[1])    
    if yrange != None:
        plt.ylim(yrange[0], yrange[1])

    # Set tick marks
    if xtick != None and xlab != None:
        plt.xticks(xtick, xlab)
    if ytick != None and ylab != None:
        plt.yticks(ytick, ylab)

    # Set up the x values and diffused curve contact probabilities
    oldx_data = xdata
    oldx_data = np.log(oldx_data)/np.log(GLOBAL_log)

    # Get the plots for each diffusion q range
    for i in range(len(diffs)):

        # Get our calculated y values from our diffused curve
        y_experimental = exp[i]

        # Set the diffusion range q variable
        setQ(diffs[i])

        # Get correct range of xdata that matches the length of the corresponding experimental data
        x_data = oldx_data
        if (len(y_experimental) != len(oldx_data)):
             x_data = oldx_data[:len(y_experimental)]

        # Get our initial theory y values using our initial gamma and A values
        y_theoretical = theory(GLOBAL_log**(x_data), -1.5, 1, 1)  # Use some example parameters

        # Fit the experimental data to the theoretical function
        initial_guess = [ -1.5, 1, 1]
        fit_params, covariance = curve_fit(theory, GLOBAL_log**(x_data), y_experimental, p0=initial_guess)
        
        # Print the fitted parameters
        print("Fitted Parameters:", fit_params)

        # Plot the results
        plt.scatter(x_data, y_experimental, label='Actual '+ str(diffs[i]), color=grphColors[i])
        plt.plot(x_data, y_theoretical, label='Initial Theory '+ str(diffs[i]),linestyle='--',  color=grphColors[i])
        plt.plot(x_data, theory(GLOBAL_log**(x_data), *fit_params), label='Fitted '+ str(diffs[i]) + " " + str(fit_params), color=grphColors[i])
       
        # Add labels and title
        plt.title(curve)
        plt.xlabel('Distance (monomers)')
        plt.ylabel('Contact Probability, simulated')

    
    # Save the graph
    plt.legend(fontsize=5)
    plt.savefig(output_directory+"fitted"+curve+".png")
    return fit_params, covariance



###### function to set a globally accessible diffusion value ####
def setQ(val):
    global GLOBAL_Q
    GLOBAL_Q = val

###### function to set a globally accessible log base value ####
def setLog(val):
    global GLOBAL_log
    GLOBAL_log = val






###############################################
## MAIN    
## This loops over all curves and produces files containing contact probability statistics. It will also (optionally) produce images of the curves and their coordinates.
    
from math import log,floor,pi
from sys import argv
import numpy as np

grphColors = ['b', 'g','brown', 'orange', 'y', 'indianred', 'olive',  'mediumorchid', 'pink','gold', 'cornflowerblue',  'r', 'yellowgreen',  'chocolate', 'orchid', 'goldenrod', 'coral', 'silver', 'tomato', 'firebrick', 'darkorange']
diffusion = [0, 4, 8, 12, 16] # amount to diffuse by

for curvename in ['Sympeano', 'qGosper', 'Dragon', 'Hilbert', '2D Random Walk']:

    print('Curve: '+curvename)

    diffuse = 1 # Set to 0 if you don't want to diffuse
    poslist = [] #list of curve coordinates
    difflist = [] #list of diffused curve coordinates
    dists,possdists = [], []

    if curvename=='Dragon':
        # Case added in so not in original load curve
        print("in dragon")
        iterationcount = 14
        # moves = recDragonCurve(iterationcount)
        moves = generate_dragon_curve(iterationcount)
        poslist = dragon_to_poslist(moves)
    else:
        if curvename == '2D Random Walk':
            poslist = random_walk_2D(16000)
            curvename = "2D Random Walk"+ str(16000)
            iterationcount = 0
        else:
            print("Not added case, just load curve")
            grammar,replacement,startmove,reldict,relclasses=loadcurve(curvename)
            curvesize=1+len(grammar[startmove])
            iterationcount=floor(log(characteristic_size,curvesize))

            print('brother')
            poslist=movelist2poslist(symblist2movelist(hilbertiter([startmove],iterationcount)))
            if makescalingfile==1:
                dists, possdists = poslist2contactlists(poslist)
                diststats2plot(dists,poslist,possdists)
        
    print ("Iteration: ", str(iterationcount))
    print("Length: ", str(len(poslist)))
    print ("PosList: \n", poslist)

    # Make image of the curve
    if makeimage==1:
        if len(poslist[0])==2: # 2D
            poslist2image(poslist,'',showends=0,lw=2,endsize=50,dpi=500)
            
        if len(poslist[0])==3: # 3D only if relevant
            poslist2image(poslist2projected(poslist,theta=(1./3)*pi,rescale=.4),'',showends=0,lw=2,endsize=50,dpi=500)

    # Prints coordinates to a file
    if makecoordinatefile==1:
        printcurve(poslist)

    # Diffuse the curve 
    if diffuse:
        plotconditions = []
        for num in diffusion: # Each value in diffusion array
            difflist = diffuseposlist(poslist,num)
            
            print ("Diffused PosList ", str(num), ": \n", difflist)
             # Make image of the diffused curve
            if makeimage==1:
                if len(poslist[0])==2:
                    poslist2image(difflist,'',showends=0,lw=2,endsize=50,dpi=100,diff=num)
        
            # Prints diffused corodinates to a file
            if makecoordinatefile==1:
                printcurve(difflist,num)
        
            # Makes contact probability data sets
            if makescalingfile==1:
                diffdists, diffpossdists = newdiff2contacts(difflist)
                cond = diststats2plotconditions(diffdists,difflist,diffpossdists,num)
                print("Cond:", str(cond))
                plotconditions.append(cond)

        A=1
        gamma = -1.3174

        if curvename == 'Dragon':
            combinedPlotDra(plotconditions, diffusion,A)
            setLog(2)

                # Set additional parameters to make the plot cover relevant ranges

            exp = [[-3.192862130288933, -4.540914771776032, -6.001035793531273, -6.8727725422840455, -8.049569831522994, -9.37863120508818, -10.57358036357238, -11.789588593268473, -13.085224190009436, -14.402629483551687, -15.833133884294787],
                   [-1.765477505558238, -3.178039447586754, -4.505093946987812, -5.939745483445283, -6.833427495522685, -8.002806736080741, -9.316424781993776, -10.536404890644016, -11.731842533788983, -13.035138958573128, -14.345710061027068, -15.783786701793213],
                   [-1.7392938430059572, -3.1772425435875435, -4.518406975586903, -5.951456148041964, -6.85479880095589, -8.00706038547439, -9.354422045235557, -10.529957945243769, -11.734540561664776, -13.05113099134103, -14.388823684026656, -15.804837341623763],
                   [-2.1212201655092446, -3.046153891676355, -4.336558691381595, -5.666744475297689, -6.717382271268927, -7.819260224954663, -9.071891463775966, -10.330126326708104, -11.53374189556347, -12.783509316011582, -14.121132004757383, -15.55193604182617],
                   [-4.7086751959927415, -4.860802074338611, -5.06023766785426, -5.4243273940227725, -5.9831451517272916, -6.9819862362151035, -8.221042277447197, -9.451955433242496, -10.694882447047176, -11.934417304266438, -13.174304106461499, -14.615272162302686],
                   [-6.464570518693799, -6.59457232934501, -6.6797774295736625, -6.840942471414951, -7.009000908803853, -7.366274607618385, -7.9387618528294, -8.974542677639503, -10.24754997660392, -11.493612412045414, -12.80114966827564, -14.217100669005095]]
            xdata = np.logspace(2**1, 13.5, 12, base=2)
            xticks = [3.32, 6.64, 9.96 , 13.28]
            xlab = ['10', '100', '1000', '10000']
            yticks = [-20, -16, -12, -8, -4, 0]
            ylab = ['$2^{-20}$','$2^{-16}$', '$2^{-12}$', '$2^{-8}$', '$2^{-4}$', '0']
            fittedSym(diffusion, exp, curvename, xdata, xticks, xlab, None, yticks, ylab, None)
        if curvename == 'Hilbert':
             combinedPlotHil(plotconditions, diffusion,A)
             setLog(2)
             fittedHil(diffusion, curvename)
        if curvename == 'Peano':
             combinedPlotPea(plotconditions, diffusion, A)
             setLog(3)
             fittedPea(diffusion, curvename)
        if curvename == 'Sympeano':
             combinedPlotSym(plotconditions, diffusion, A)
             setLog(3)

                # Set additional parameters to make the plot cover relevant ranges
             exp = [[-2.3690394135942183, -5.892642784284246, -5.427113980987631, -7.260600590278552, -8.25557852525374, -10.25040190350377, -11.203105689447085, -13.14030408590523],
                    [-2.3673413672218624, -5.877233287890416, -5.427224992540501, -7.2600450582340725, -8.253358428478458, -10.24871783414896, -11.200580752386635, -13.129135366313818],
                    [-2.3622317234024615, -5.827846870009281, -5.40930653529823, -7.260322781875167, -8.233075233674418, -10.24871783414896, -11.183924492083287, -13.14030408590523],
                    [-2.0885459304483303, -4.566633701902702, -4.921416209697916, -6.803664554248674, -7.738919921304435, -9.724788530102089, -10.692758740594652, -12.658628459396695],
                    [-3.077399901334372, -3.488251888916122, -4.0895404389322385, -5.630782918979362, -6.472895990737102, -8.433143486852948, -9.317508688719368, -11.26811417295395],
                    [-4.150012466925099, -4.3219397926736995, -4.555621203161467, -5.266796089466804, -6.143045894472591, -7.948893298377135, -8.728240900133788, -10.64457818134223]]
             xdata = np.logspace(3**0.5, 9.5, 8, base=3)
             xticks = [2.09, 4.19, 6.28 , 8.38]
             xlab = ['10', '100', '1000', '10000']
             xrange = [1, 10]
             yticks = [-14, -10, -6 , -2]
             ylab = ['$3^{-14}$,', '$3^{-10}$', '$3^{-6}$', '$3^{-2}$']
             yrange = [-15, -1]
             fittedSym(diffusion, exp, curvename, xdata, xticks, xlab, xrange, yticks, ylab, yrange)
        if curvename == 'qGosper':
             combinedPlotqGo(plotconditions, diffusion, A)
        if '2D Random Walk' in curvename:
             combinedPlotRW(plotconditions, diffusion, A)