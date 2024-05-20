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

## __PARAMETERS__

## Output Directory. Please reset this to your local directory name.
output_directory=''

## The code will automatically produce and analyze the smallest curve of each type larger than the characteristic size.
## Good convergence to theorical estimates for contact probability scaling is obtained for curves at least 10M units (10**7) long.
characteristic_size=10**3

## Make output images of the various curves. Note that for large curves, this may crash or take a long time.
## 1=YES; 0=NO
makeimage=1

## Make output files listing the coordinates of the various curves. Note that for large curves, this may take a long time and generate a large file.
## 1=YES; 0=NO
makecoordinatefile=0

## Make output files exhibiting the contact probability scaling, as in the supplemental figures of the paper.
## 1=YES; 0=NO
makescalingfile=0


###############################################
def loadcurve(curvename):
### This establishes the recursive grammar for the relevant curve. Each curve is represented by a series of symbols that have a geometrical interpretation;
### iterating the curve consists of replacing the symbols according to a given rule of replacement. An appropriate starting move is also chosen.
### For the 3D curves, reldict and relcasses contain a list of possible geometric interpretations of each symbol, making it possible to interpret the list
### of symbols stochastically. This can be used to generate an ensemble of related but distinct spacefilling curves.

#### A 3D Hilbert Curve (code can also create a randomized version)   
    if curvename=='Hilbert3D':
        curve3d=1
        grammar={'I': [[0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0], [0, 0, 1]]}
        replacement={'I':['X3Z3','D','XY','L','XY','U','Y2','F','Y2','D','X3Y','R','X3Y','U','XZ']}

#### A 3D Peano Curve (code can also create a randomized version)   
    if curvename=='Peano3D' or curvename=='Peano3D_random':
        curve3d=1
        grammar={'I': [[0, 0, -1], [0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 0, -1], [0, -1, 0], [0, 0, 1], [0, 0, 1], [1, 0, 0], [0, 0, -1], [0, 0, -1], [1, 0, 0], [0, 0, 1], [0, 0, 1], [0, -1, 0], [0, 0, -1],[0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 0, -1]]}
        replacement={'I':['I','D','X3Y','D','I','F','XY3','U','XZ','U','XY3','F','I','D','X3Y','D','I','L','X2','U','XZ3','U','X2','B','Z2','D','X3Z3','D','Z2','B','X2','U','XZ3','U','X2','L','I','D','X3Y','D','I','F','XY3','U','XZ','U','XY3','F','I','D','X3Y','D','I']}

#### This is the classic Hilbert Curve
    if curvename=='Hilbert':
        curve3d=0
        grammar={'CL': [(1, 0), (0, -1), (-1, 0)], 'CR': [(-1, 0), (0, 1), (1, 0)], 'CD': [(0, 1), (-1, 0), (0, -1)], 'CU': [(0, -1), (1, 0), (0, 1)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
        replacement={'CU':['CL','D','CU','R','CU','U','CR'],'CL':['CU','R','CL','D','CL','L','CD'],'CD':['CR','U','CD','L','CD','D','CL'],'CR':['CD','L','CR','U','CR','R','CU'],'L':'L','R':'R','U':'U','D':'D'}

#### This is the classic Peano Curve        
    if curvename=='Peano':
        curve3d=0
        grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
        replacement={'WUR': ['WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR'], 'D': 'D', 'WDL': ['WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL'], 'L': 'L', 'WDR': ['WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR'], 'R': 'R', 'U': 'U', 'WUL': ['WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL']}

#### Symmetrized 3x3 Peano
    if curvename=='PeanoSym':
        curve3d=0
        grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(0, 1), (0, 1), (-1, 0), (0, -1), (0, -1), (-1, 0), (0, 1), (0, 1)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(0, -1), (0, -1), (1, 0), (0, 1), (0, 1), (1, 0), (0, -1), (0, -1)],'L':[(0,-1)],'R':[(0,1)],'U':[(1,0)],'D':[(-1,0)]}
        replacement={'WUR': ['WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR'], 'D': 'D', 'WDL': ['WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL'], 'L': 'L', 'WDR': ['WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR'], 'R': 'R', 'U': 'U', 'WUL': ['WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL']}

#### Quadratic Gosper Curve
    if curvename=='qGosper':
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
            for key1 in directions.keys():
                    for key2 in allkeys:
                            dproducts[(key1,key2)]=rotateop(directions[key1],expand(key2))

            dshortcuts={}
            for key in dproducts.keys():
                newdir=''
                if dproducts[key][0][0]>1:
                    newdir+='R'+`abs(dproducts[key][0][0])`
                if dproducts[key][0][0]<-1:
                    newdir+='L'+`abs(dproducts[key][0][0])`                                    
                if dproducts[key][0][1]>1:
                    newdir+='B'+`abs(dproducts[key][0][1])`
                if dproducts[key][0][1]<-1:
                    newdir+='F'+`abs(dproducts[key][0][1])`
                if dproducts[key][0][2]>1:
                    newdir+='U'+`abs(dproducts[key][0][2])`
                if dproducts[key][0][2]<-1:
                    newdir+='D'+`abs(dproducts[key][0][2])`
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

#grammar,replacement,startmove,reldict,relclasses=loadcurve('Hilbert')

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
            print i
        
        for d in xrange(dim):
            currpos[d]+=entry[d]
        poslist.append([entry for entry in currpos])

    return poslist


###############################################
def poslist2posarray(poslist):
### Creates a 2D array showing at what point a 2D curve reaches all points in the array. Useful for computing contact probabilities.

    from numpy import zeros
    minx,maxx,miny,maxy=poslist2bounds(poslist)
    posarray=zeros((1+maxx-minx,1+maxy-miny))
    for i in range(len(poslist)):
        posarray[poslist[i][0]-minx,poslist[i][1]-miny]=i+1

    return posarray


###############################################
def poslist2bounds(poslist):
### Computes the smallest square in the first quadrant that can contain the entire curve, eg its extent in various directions.
    
    dim=len(poslist[0])
    bounds=[]
    for d in range(dim):
        bounds.append(min([entry[d] for entry in poslist]))
        bounds.append(max([entry[d] for entry in poslist]))        

    return bounds


###############################################
def poslist2image(poslist,tag,showends=0,lw=2,endsize=50,dpi=100):
### Makes a picture of the curve

    minx,maxx,miny,maxy=poslist2bounds(poslist)

    from pylab import close,savefig,plot,axis,xlim,ylim,scatter
    close('all')
    
    print len(poslist)

    index0=[entry[0] for entry in poslist]
    index1=[entry[1] for entry in poslist]    
    a=plot(index0,index1,color='g',lw=lw)    
    a=axis('off')
    a=xlim([minx-1,maxx+1])
    a=ylim([miny-1,maxy+1])
    if showends==1:
        scatter([poslist[0][0],poslist[-1][0]],[poslist[0][1],poslist[-1][1]],s=endsize,color=['g','r'])
    savefig(output_directory+curvename+'.'+`len(poslist)`+tag+'.png',dpi=dpi)


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
    for letter in string:
        movelist=rotate(movelist,axval[letter])

    return movelist


###############################################
def expand(string):
### Expands strings of operations using 'power'-like notation into a string of raw operations, eg 'X3Y2' --> 'XXXYY'.
    
	newstring=''
	for i in range(len(string)):
		if string[i] not in ['I']+[`intval` for intval in range(1,10) ]:
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
def reflectmoves(movelist,axis):
### Reflects a series of moves.
    
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
def printcurve(poslist):
### Prints a given iteration of the chosen curve out to file.

    curvelen=len(poslist)
    output1=open(output_directory+curvename+'.'+`curvelen`+'.txt','w')
    for entry in poslist:
            for coord in range(len(entry)):
                    if coord!=len(entry)-1:
                            output1.write(`entry[coord]`+'\t')
                    else:
                            output1.write(`entry[coord]`+'\n')
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
                            dists[abs(valref-val)]+=1
        possdists=[0]+[strandsize-i for i in range(1,strandsize)]

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
def diststats2plot(dists,possdists):    
### Computes long range contact stats for the curve, using posarray as input.

    from math import log
    from numpy import arange,zeros
    from pylab import polyfit

    logbase=int((1+len(grammar[startmove]))**(1./len(poslist[0])))
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
    fitall=polyfit(ratioindex[1:-1],ratio[1:-1],1)

    from pylab import close,plot,savefig,legend,xlabel,ylabel,title
    close('all')
    a=plot(ratioindex,ratio)
    a=plot(ratioindex[1:-1],[fitall[1]+(fitall[0]*i) for i in ratioindex[1:-1]],'r--',label='Slope: '+`fitall[0]`[:6])
    a=xlabel('Distance (log '+`logbase`+')')
    a=ylabel('Contact Probability (log '+`logbase`+')')
    a=legend()
    savefig(output_directory+'Scaling.'+curvename+'.'+`len(poslist)`+'.log'+`logbase`+'.png')


###############################################
## MAIN    
## This loops over all curves and produces files containing contact probability statistics. It will also (optionally) produce images.
    
#for curvename in ['Hilbert3D','Peano3D','Peano3D_random','Hilbert','Peano','PeanoSym','qGosper']:
for curvename in ['qGosper']:
    grammar,replacement,startmove,reldict,relclasses=loadcurve(curvename)
    
    from math import log,floor,pi
    curvesize=1+len(grammar[startmove])
    iterationcount=floor(log(characteristic_size,curvesize))
    print curvename,iterationcount

    if 'random' in curvename:
        poslist=movelist2poslist(symblist2randmovelist(hilbertiter([startmove],iterationcount)))
    else:
        poslist=movelist2poslist(symblist2movelist(hilbertiter([startmove],iterationcount)))
    
    if makeimage==1:
        if len(poslist[0])==2:
            poslist2image(poslist,'',showends=0,lw=2,endsize=50,dpi=100)
            
        if len(poslist[0])==3:
            poslist2image(poslist2projected(poslist,theta=(1./3)*pi,rescale=.4),'',showends=0,lw=2,endsize=50,dpi=100)

    if makecoordinatefile==1:
        printcurve(poslist)

    if makescalingfile==1:
        dists,possdists=poslist2contactlists(poslist)
        diststats2plot(dists,possdists)


