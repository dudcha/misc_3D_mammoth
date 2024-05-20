

##curve3d=1

## A 3D Hilbert Curve
##grammar={'I': [[0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0], [0, 0, 1]]}
##replacement={'I':['X3Z3','D','XY','L','XY','U','Y2','F','Y2','D','X3Y','R','X3Y','U','XZ']}

## A 3D Peano Curve
##grammar={'I': [[0, 0, -1], [0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 0, -1], [0, -1, 0], [0, 0, 1], [0, 0, 1], [1, 0, 0], [0, 0, -1], [0, 0, -1], [1, 0, 0], [0, 0, 1], [0, 0, 1], [0, -1, 0], [0, 0, -1],[0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 0, -1]]}
##replacement={'I':['I','D','X3Y','D','I','F','XY3','U','XZ','U','XY3','F','I','D','X3Y','D','I','L','X2','U','XZ3','U','X2','B','Z2','D','X3Z3','D','Z2','B','X2','U','XZ3','U','X2','L','I','D','X3Y','D','I','F','XY3','U','XZ','U','XY3','F','I','D','X3Y','D','I']}

###This is a funny space-filling curve I just made as a comparison.
##grammar={'I': [[0, 0, -1], [0, 0, -1], [-1, 0, 0], [0, 0, 1], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, 0, -1], [0, -1, 0], [0, 0, 1], [0, 0, 1], [0, -1, 0], [0, 0, -1], [0, 0, -1], [1, 0, 0], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 0, -1], [0, 0, -1], [1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1], [0, -1, 0]]}
##replacement={'I':['X3Z3','D','XY','L','XY','U','Y2','F','Y2','D','X3Y','R','X3Y','U','XZ']}

###### This is the basic unit of the Z-Order/Lebesgue 3D spacefilling curve. Only works to second order. Argh.
##grammar={'I':[[1,0,0],[-1,1,0],[1,0,0],[-1,-1,1],[1,0,0],[-1,1,0],[1,0,0]]}
##replacement={'I':['I','RFD','I','L3B1D','I','RFD','I','L3F3U','I','RFD','I','L3B1D','I','RFD','I']}

curve3d=0
## This is the classic Hilbert Curve
#curvename='Hilbert'
#grammar={'CL': [(1, 0), (0, -1), (-1, 0)], 'CR': [(-1, 0), (0, 1), (1, 0)], 'CD': [(0, 1), (-1, 0), (0, -1)], 'CU': [(0, -1), (1, 0), (0, 1)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
#replacement={'CU':['CL','D','CU','R','CU','U','CR'],'CL':['CU','R','CL','D','CL','L','CD'],'CD':['CR','U','CD','L','CD','D','CL'],'CR':['CD','L','CR','U','CR','R','CU'],'L':'L','R':'R','U':'U','D':'D'}

## These are more general Peano curves. The contour is a simple back-and-forth; 2x3, 3x3, 4x3, 5x3.
##curvename='Peano'
##grammar={'WUR': [(1, 0), (0, 1), (-1, 0), (0, 1), (1, 0)], 'WDR': [(1, 0), (0, -1), (-1, 0), (0, -1), (1, 0)], 'WDL': [(-1, 0), (0, -1), (1, 0), (0, -1), (-1, 0)], 'WUL': [(-1, 0), (0, 1), (1, 0), (0, 1), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
##grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
##grammar={'WUR': [(1, 0), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (1, 0)], 'WDR': [(1, 0), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (1, 0)], 'WDL': [(-1, 0), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (-1, 0)], 'WUL': [(-1, 0), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
##grammar={'WUR': [(1, 0), (1, 0), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (1, 0), (1, 0)], 'WDR': [(1, 0), (1, 0), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (1, 0), (1, 0)], 'WDL': [(-1, 0), (-1, 0), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (-1, 0), (-1, 0)], 'WUL': [(-1, 0), (-1, 0), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (-1, 0), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
##This is a wigglier version of the above 3x3 curve, but I don't like it b/c it forms swastikas.
##grammar={'WUR': [(0, 1), (0, 1), (1, 0), (0, -1), (0, -1), (1, 0), (0, 1), (0, 1)], 'WDR': [(1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0)], 'WDL': [(0, -1), (0, -1), (-1, 0), (0, 1), (0, 1), (-1, 0), (0, -1), (0, -1)], 'WUL': [(-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
##This is a quick-and-dirty mirror image of the above which has erroneous labels but doesn't bother me visually.
##grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(0, 1), (0, 1), (-1, 0), (0, -1), (0, -1), (-1, 0), (0, 1), (0, 1)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(0, -1), (0, -1), (1, 0), (0, 1), (0, 1), (1, 0), (0, -1), (0, -1)],'L':[(0,-1)],'R':[(0,1)],'U':[(1,0)],'D':[(-1,0)]}
##replacement={'WUR': ['WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR'], 'D': 'D', 'WDL': ['WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL'], 'L': 'L', 'WDR': ['WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR'], 'R': 'R', 'U': 'U', 'WUL': ['WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL']}

##Standard 3x3 Peano
##curvename='Peano'
##grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0)],'L':[(-1,0)],'R':[(1,0)],'U':[(0,1)],'D':[(0,-1)]}
##replacement={'WUR': ['WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR'], 'D': 'D', 'WDL': ['WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL'], 'L': 'L', 'WDR': ['WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR'], 'R': 'R', 'U': 'U', 'WUL': ['WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL']}

##Symmetric 3x3 Peano
##curvename='PeanoSym'
##grammar={'WUR': [(1, 0), (1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0), (1, 0)], 'WDR': [(0, 1), (0, 1), (-1, 0), (0, -1), (0, -1), (-1, 0), (0, 1), (0, 1)], 'WDL': [(-1, 0), (-1, 0), (0, -1), (1, 0), (1, 0), (0, -1), (-1, 0), (-1, 0)], 'WUL': [(0, -1), (0, -1), (1, 0), (0, 1), (0, 1), (1, 0), (0, -1), (0, -1)],'L':[(0,-1)],'R':[(0,1)],'U':[(1,0)],'D':[(-1,0)]}
##replacement={'WUR': ['WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR'], 'D': 'D', 'WDL': ['WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL'], 'L': 'L', 'WDR': ['WDR', 'R', 'WUR', 'R', 'WDR', 'D', 'WDL', 'L', 'WUL', 'L', 'WDL', 'D', 'WDR', 'R', 'WUR', 'R', 'WDR'], 'R': 'R', 'U': 'U', 'WUL': ['WUL', 'L', 'WDL', 'L', 'WUL', 'U', 'WUR', 'R', 'WDR', 'R', 'WUR', 'U', 'WUL', 'L', 'WDL', 'L', 'WUL']}

def hilbertstep(symblist):
    newlist=[]
    for symb in symblist:
        newlist+=replacement[symb]
            
    return newlist

def hilbertiter(symblist,steps):

    for step in range(steps):
        symblist=hilbertstep(symblist)

    return symblist

def symblist2movelist(symblist):
    movelist=[]
    for symb in symblist:
        movelist+=grammar[symb]

    return movelist


def symblist2randmovelist(symblist):

    from random import choice
    
    movelist=[]
    for symb in symblist:
        if symb in reldict.keys():
            randpick=choice(relclasses[reldict[symb]])
            movelist+=grammar[randpick]
        else:
            movelist+=grammar[symb]
    

    return movelist

def movelist2poslist(movelist):

    print len(movelist)
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

def poslist2posarray(poslist):

    from numpy import zeros
    minx,maxx,miny,maxy=poslist2bounds(poslist)
    posarray=zeros((1+maxx-minx,1+maxy-miny))
    for i in range(len(poslist)):
        posarray[poslist[i][0]-minx,poslist[i][1]-miny]=i+1

    return posarray

def poslist2bounds(poslist):

    dim=len(poslist[0])
    bounds=[]
    for d in range(dim):
        bounds.append(min([entry[d] for entry in poslist]))
        bounds.append(max([entry[d] for entry in poslist]))        

    return bounds


def poslist2image(poslist,tag,showends=0,lw=2,endsize=50,dpi=100):

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
    savefig(dirx+'trycurve'+tag+'.png',dpi=dpi)

##def posarray2loopstats(posarray,shrinkfactor,cut=[0,0],valrange=[0,0]):
def posarray2loopstats(posarray,shrinkfactor,cut=[0,0]):    

    if shrinkfactor==2:
        logbase=2
        step=1
        top=30
##        cutoff=14
        cutoff=18
##        cutoff=10
##        cutoff=13

    if shrinkfactor==3:    
        logbase=3
        step=1
        top=18
        cutoff=10

    if shrinkfactor==5:    
        logbase=5
        step=1
        top=14
        cutoff=8
        
    chainlength=int(posarray.max())-1
    print chainlength
    
    from numpy import zeros
    strandsize=chainlength+1
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
##                    if (val>valrange[0] and val<(chainlength-valrange[1])) or (valref>valrange[0] and valref<(chainlength-valrange[1])):
                        dists[abs(valref-val)]+=1
    possdists=[0]+[strandsize-i for i in range(1,strandsize)]
    distratio=[float(possdists[i])/dists[i] for i in range(strandsize)]
    oddratio=[distratio[i] for i in range(strandsize) if i%2==1]

    for i in range(50):
        if i%2==1:
            print i,'\t',int(dists[i]),'\t',possdists[i]

##    for i in range(len(oddratio)):
##        if oddratio[i]<100000:
##            print 2*i+1,'\t',oddratio[i],'\t',1./oddratio[i]


    from numpy import arange
    from math import log
    from pylab import polyfit

    lbins=arange(0,top,step)
    binposs=zeros(len(lbins))
    binact=zeros(len(lbins))
    currbin=0
    for i in range(1,len(dists)):
        while log(i,logbase)>lbins[currbin]:
                currbin+=1
        binposs[currbin]+=possdists[i]
        binact[currbin]+=dists[i]


    minstart=2

    newlen=arange(0,cutoff+1,step)

    ratioindex=range(minstart,len(newlen))

    ratio=[log(float(binact[i])/binposs[i],logbase) for i in ratioindex]
##    fit=polyfit(ratioindex[:-1],ratio[:-1],1)
    print ratio
    print ratio[cut[0]:len(ratioindex)-cut[1]]
    print cut[0],len(ratioindex)-cut[1]
    fitall=polyfit(ratioindex[cut[0]:len(ratioindex)-cut[1]],ratio[cut[0]:len(ratioindex)-cut[1]],1)

    print fitall
    

    from pylab import close,plot,savefig,legend,xlabel,ylabel,title
    close('all')
    a=plot(ratioindex,ratio)
    a=plot(ratioindex,[fitall[1]+(fitall[0]*i) for i in ratioindex],'r--',label='Slope: '+`fitall[0]`[:6])
##    a=plot(ratioindex,[fit[1]+(fit[0]*i) for i in ratioindex],'r--',label='Slope: '+`fit[0]`[:6])    
    a=xlabel('Distance (log '+`logbase`+')')
    a=ylabel('Contact Probability (log '+`logbase`+')')
    a=legend()
    savefig(dirx+'Scaling.'+curvename+'.'+`chainlength`+'.log'+`logbase`+'.png')



def poslist2projected(poslist):

    newlist=[]
    for pos in poslist:
        newlist.append([pos[0]-.4*pos[1],pos[2]+.2*pos[1]])

    return newlist

def rotate(movelist,axnum,plusminus=1):
	newlist=[]
	for move in movelist:
		newmove=[0,0,0]
		newmove[axnum]=move[axnum]
		newmove[(axnum+1)%3]=plusminus*move[(axnum-1)%3]
		newmove[(axnum-1)%3]=-1*plusminus*move[(axnum+1)%3]
		newlist.append(newmove)
	return newlist

def rotateop(movelist,string):
    axval={'X':0,'Y':1,'Z':2}
    for letter in string:
        movelist=rotate(movelist,axval[letter])

    return movelist

##def expand(string):
##	newstring=''
##	for i in range(len(string)):
##		if string[i] not in ['X','Y','Z']:
##			newstring+=string[i]
##		elif string[i]!='I':
##			newstring+=string[i-1]*(int(string[i])-1)
##	return newstring

def expand(string):
	newstring=''
	for i in range(len(string)):
		if string[i] not in ['I']+[`intval` for intval in range(1,10) ]:
			newstring+=string[i]
		elif string[i]!='I':
			newstring+=string[i-1]*(int(string[i])-1)
	return newstring

def poslist2posdict(poslist):
##for 3d lists

    posdict={}
    minx,maxx,miny,maxy,minz,maxz=poslist2bounds(poslist)
    for i in range(len(poslist)):
        posdict[(poslist[i][0]-minx,poslist[i][1]-miny,poslist[i][2]-minz)]=i
    return posdict


def reflectmoves(movelist,axis):
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

def flipmoves(movelist):
	newlist=[]
	for move in movelist:
		newlist.append([move[1],move[0]])
	return newlist

def revmoves(movelist):
	newlist=[]
	for move in movelist[::-1]:
		newlist.append([-1*move[0],-1*move[1]])
	return newlist



def reflectmoves(movelist,axis):
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


def rotate2D(movelist):
	newlist=[]
	for move in movelist:
	    newlist.append(move+[0])
	rotlist=rotate(newlist,2)
	newrotlist=[[entry[0],entry[1]] for entry in rotlist]
	    
	return newrotlist



if curve3d==1:
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

##
##for nullit in range(1):
##	pd=poslist2posdict(movelist2poslist(symblist2movelist(hilbertiter(['I'],6))))
##	print 'lenpd',len(pd)
##	posdict=pd
##	from numpy import zeros
##	strandsize=len(posdict)
##	dists=zeros(strandsize)
##	bounds=poslist2bounds(posdict.keys())
##	for i in range(bounds[1]+1):
##		for j in range(bounds[3]+1):
##			for k in range(bounds[5]+1):
##				valref=posdict[(i,j,k)]
##				comparevals=[]
##				if i>0:
##					comparevals.append(posdict[(i-1,j,k)])
##				if j>0:
##					comparevals.append(posdict[(i,j-1,k)])
##				if k>0:
##					comparevals.append(posdict[(i,j,k-1)])
##				for val in comparevals:
##					dists[abs(valref-val)]+=1
##	possdists=[strandsize-i for i in range(strandsize)]
##	distratio=[float(possdists[i])/dists[i] for i in range(strandsize)]
##	oddratio=[distratio[i] for i in range(strandsize) if i%2==1]
##	for i in range(len(oddratio)):
##		if oddratio[i]<100:
##			print 2*i+1,'\t',oddratio[i]
##
##
##	from numpy import arange
##	from math import log
##	from pylab import polyfit
##
##        logbase=2
##        step=2
##        top=24
##        cutoff=24
##
##	lbins=arange(0,top,step)
##	binposs=zeros(len(lbins))
##	binact=zeros(len(lbins))
##	currbin=0
##	for i in range(len(dists)):
##		while log(i+1,logbase)>lbins[currbin+1]:
##			currbin+=1
##		binposs[currbin]+=possdists[i]
##		binact[currbin]+=dists[i]
##
##	newlen=arange(0,cutoff,step)
##	ratio=[log(float(binact[i])/binposs[i],logbase) for i in range(len(newlen)-1)]
##	fit=polyfit(range(0,(len(ratio)-2)*2,2),ratio[1:-1],1)
##	print ratio
##	print fit
##
##        dirx='C:\\Users\\Erez\\Documents\\Pyworkspace\\'
##	from pylab import close,plot,savefig
##	close('all')
##	a=plot(range(0,(len(ratio)-4)*step,step),ratio[2:-2])
##	a=plot(range(0,(len(ratio)-4)*step,step),[fit[1]+fit[0]*i for i in range(0,(len(ratio)-4)*step,step)],'r--')
##
####	a=plot(range(0,(len(ratio))*step,step),ratio)
####	a=plot(range(0,(len(ratio))*step,step),[fit[1]+(fit[0]*i) for i in range(0,(len(ratio))*step,step)],'r--')
##
##	savefig(dirx+'plotbanana.png')

####-------------------------------------------------------------------
#### Other Curves of Interest.

## Aubrey Jaffer's Units
## Peano.
##ajp=[[0,0,0],[1,0,0],[2,0,0],[2,1,0],[1,1,0],[0,1,0],[0,2,0],[1,2,0],[2,2,0],[2,2,1],[1,2,1],[0,2,1],[0,1,1],[1,1,1],[2,1,1],[2,0,1],[1,0,1],[0,0,1],[0,0,2],[1,0,2],[2,0,2],[2,1,2],[1,1,2],[0,1,2],[0,2,2],[1,2,2],[2,2,2],[3,2,2]]
## Hilbert
##ajh=[[0, 0, 0],[1, 0, 0],[1, 0, 1],[0, 0, 1],[0, 1, 1],[1, 1, 1],[1, 1, 0],[0, 1, 0],[0, 2, 0],[0, 2, 1],[0, 3, 1],[0, 3, 0],[1, 3, 0],[1, 3, 1],[1, 2, 1],[1, 2, 0],[2, 2, 0],[2, 2, 1],[2, 3, 1],[2, 3, 0],[3, 3, 0],[3, 3, 1],[3, 2, 1],[3, 2, 0],[3, 1, 0],[3, 0, 0],[2, 0, 0],[2, 1, 0],[2, 1, 1],[2, 0, 1],[3, 0, 1],[3, 1, 1],[3, 1, 2],[3, 0, 2],[2, 0, 2],[2, 1, 2],[2, 1, 3],[2, 0, 3],[3, 0, 3],[3, 1, 3],[3, 2, 3],[3, 2, 2],[3, 3, 2],[3, 3, 3],[2, 3, 3],[2, 3, 2],[2, 2, 2],[2, 2, 3],[1, 2, 3],[1, 2, 2],[1, 3, 2],[1, 3, 3],[0, 3, 3],[0, 3, 2],[0, 2, 2],[0, 2, 3],[0, 1, 3],[1, 1, 3],[1, 1, 2],[0, 1, 2],[0, 0, 2],[1, 0, 2],[1, 0, 3],[0, 0, 3],[0, 0, 4]]



## These apply to the Jigsaw curve but probably not to other curves.
def flipsymb(symblist):

    newlist=[]
    for symb in symblist:
        newlist.append(symb.replace('R','u').replace('L','d').replace('U','r').replace('D','l').replace('l','L').replace('r','R').replace('u','U').replace('d','D'))

    return newlist        
        
def revsymb(symblist):

    newlist=[]
    for symb in symblist[::-1]:
        newlist.append(symb.replace('R','l').replace('L','r').replace('U','d').replace('D','u').replace('l','L').replace('r','R').replace('u','U').replace('d','D'))

    return newlist


#### This is my fractal-boundaried Peano curve
#### My new wierd fractal spacefiller idea.
curvename='Jigsaw'
mlbottom=[[1,0],[0,1],[-1,0],[0,1],[0,1],[1,0],[0,-1],[1,0],[0,-1],[0,-1],[1,0],[0,1],[0,1],[1,0],[1,0],[0,1],[-1,0],[-1,0],[-1,0],[0,1],[0,1],[0,1],[-1,0],[-1,0],[0,1],[1,0],[1,0],[1,0],[0,-1],[0,-1],[0,-1],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[1,0],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[1,0],[0,1],[0,1],[0,1],[1,0],[0,-1],[0,-1],[1,0],[1,0],[0,-1],[-1,0],[-1,0],[0,-1],[-1,0],[0,-1],[1,0],[0,-1],[-1,0],[0,-1],[1,0]]
mltop=[[0,-1],[0,-1],[1,0],[1,0],[0,-1],[-1,0],[-1,0],[0,-1],[0,-1],[0,-1],[0,-1],[-1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[-1,0],[0,1],[0,1],[-1,0],[0,-1],[0,-1],[0,-1],[1,0],[0,-1],[-1,0],[0,-1],[1,0],[0,-1],[0,-1],[-1,0],[0,1],[-1,0],[0,-1],[0,-1],[0,-1],[-1,0],[-1,0],[-1,0],[0,1],[1,0],[1,0],[0,1],[-1,0],[-1,0],[0,1],[1,0],[1,0],[0,1],[1,0],[0,1],[-1,0],[0,1],[1,0],[0,1],[-1,0],[-1,0],[0,-1],[-1,0],[0,1]]
grammar={}
grammar['0R']=mlbottom
grammar['0L']=revmoves(mlbottom)
grammar['0U']=flipmoves(mlbottom)
grammar['0D']=revmoves(flipmoves(mlbottom))
grammar['1L']=mltop
grammar['1R']=revmoves(mltop)
grammar['1D']=flipmoves(mltop)
grammar['1U']=revmoves(flipmoves(mltop))
grammar['R']=[[1,0]]
grammar['L']=[[-1,0]]
grammar['U']=[[0,1]]
grammar['D']=[[0,-1]]
replacement={'L':'L','R':'R','U':'U','D':'D'}
replacement['0R']=['0R','R','0U','U','0U','L','1L','U','0U','U','0R','R','0R','D','1D','R','0R','D','1D','D','1D','R','0U','U','0U','U','0R','R','0R','R','0U','U','0U','L','1L','L','1L','L','1L','U','0U','U','0U','U','0U','L','1L','L','1L','U','0R','R','0R','R','0R','R','0R','D','1D','D','1D','D','1D','R','0U','U','0U','U','0U','U','0U','U','0U','U','0R','R','0R','D','1D','D','1D','D','1D','D','1D','D','1D','R','0U','U','0U','U','0U','U','0R','R','0R','D','1D','D','1D','R','0R','R','0R','D','1L','L','1L','L','1D','D','1L','L','1D','D','1D','R','0R','D','1L','L','1D','D','1D','R','0R']
replacement['0L']=revsymb(replacement['0R'])
replacement['0U']=flipsymb(replacement['0R'])
replacement['0D']=revsymb(flipsymb(replacement['0R']))
replacement['1L']=['1D','D','1D','D','1D','R','0R','R','0R','D','1L','L','1L','L','1D','D','1D','D','1D','D','1D','D','1L','L','1L','U','0U','U','0U','U','0U','U','0U','U','0U','U','0U','U','0U','L','1L','U','0U','U','0U','L','1D','D','1D','D','1D','D','1D','R','0R','D','1L','L','1D','D','1D','R','0R','D','1D','D','1L','L','1L','U','0U','L','1D','D','1D','D','1D','D','1L','L','1L','L','1L','L','1L','U','0R','R','0R','R','0U','U','0U','L','1L','L','1L','U','0R','R','0R','R','0U','U','0R','R','0U','U','0U','L','1L','U','0R','R','0U','U','0U','L','1L','L','1D','D','1L','L','1L','U','0U']
replacement['1R']=revsymb(replacement['1L'])
replacement['1D']=flipsymb(replacement['1L'])
replacement['1U']=revsymb(flipsymb(replacement['1L']))

##This is a mini-square made of 4 iteration 2 Jigsaws.
ml=hilbertiter(['0R'],2)+['R']+hilbertiter(['0U'],2)+['U']+hilbertiter(['0U'],2)+['L']+hilbertiter(['1L'],2)+['L']+hilbertiter(['1D'],2)+['D']+hilbertiter(['1D'],2)+['D']+hilbertiter(['1D'],2)+['R']+hilbertiter(['0R'],2)+['R']+hilbertiter(['0R'],2)


def revgosper(symblist):

    newlist=[]
    for symb in symblist[::-1]:
        newsymb=''
        newsymb+=symb[0].replace('R','l').replace('L','r').replace('U','d').replace('D','u').replace('l','L').replace('r','R').replace('u','U').replace('d','D')
        newsymb+=symb[1]
        newlist.append(newsymb)
        
    return newlist

def rotgosper(symblist):

    rotdict={'DR':'LD','UR':'RD','LD':'UL','RD':'DL','DL':'LU','UL':'RU','LU':'UR','RU':'DR'}
    newlist=[]
    for symb in symblist:
        newlist.append(rotdict[symb])
        
    return newlist

##Trying to build the quadratic Gosper curve
##curvename='qGosper'
##grammar={'DR': [[0,-1],[0,-1],[1,0],[0,1],[1,0],[0,-1],[1,0],[0,1],[0,1],[1,0],[0,-1],[0,-1],[0,-1],[1,0],[0,-1],[-1,0],[-1,0],[0,1],[-1,0],[-1,0],[0,-1],[1,0],[0,-1],[-1,0],[-1,0]]}
##grammar['UR']=revmoves(grammar['DR'])
##grammar['LD']=rotate2D(grammar['DR'])
##grammar['RD']=rotate2D(grammar['UR'])
##grammar['UL']=rotate2D(grammar['LD'])
##grammar['DL']=rotate2D(grammar['RD'])
##grammar['LU']=rotate2D(grammar['DL'])
##grammar['RU']=rotate2D(grammar['UL'])
##replacement={}
##replacement['DR']=['DR','DR','RD','UR','RU','DR','RD','UR','UL','RD','DR','DR','DL','RU','DL','LD','LD','UR','LD','LU','DL','RU','DR','LU','LU']
##replacement['UR']=revgosper(replacement['DR'])
##replacement['LD']=rotgosper(replacement['DR'])
##replacement['RD']=rotgosper(replacement['UR'])
##replacement['UL']=rotgosper(replacement['LD'])
##replacement['DL']=rotgosper(replacement['RD'])
##replacement['LU']=rotgosper(replacement['DL'])
##replacement['RU']=rotgosper(replacement['UL'])



##replacement['DR']=['DR','DR','RD']


import os
opsys1=os.name

from sys import argv
"""for number in range(1,5):
	for x in ['1R']:
	        plist= movelist2poslist(symblist2movelist(hilbertiter([x],number-1)))
		f=open('scratch'+'/'+x+`number`+'.txt', 'w')
		for point in plist:
			f.write(`point[0]`+'\t'+`point[1]`+'\t0\n')
		f.close()
"""
print poslist2posarray( movelist2poslist( symblist2movelist(hilbertiter([argv[1]],0))    ))
