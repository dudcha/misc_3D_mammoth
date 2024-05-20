#!/usr/bin/python
from time import time
from sys import argv, stdout
from numpy import array, dot, zeros
from math import log, ceil,sqrt


try: jump=int(argv[3])
except: jump=1

output_directory='output/'

def message(text):
	print '%10.5f'%(time()-benchmark)+'\t'+text
benchmark=time()
name = argv[1]
message(name+' '+argv[2])


poslist=[]
#cut through all the computation and just read the transformed coordinates directly from file
inputfile = open('poslists/'+name+'/'+name+argv[2]+'.txt', 'r')

#store the last line to avoid repeats
lastline = []
for row in inputfile:
	line = row.strip('\n').split('\t')
	if line!=lastline:
		print line
#		print float(line[0])*2,float(line[1])/(sqrt(3)/4.0),line[2]
		x = int(round(float(line[0])*2))
		y = int(round(float(line[1])/(sqrt(3)/4.0)))
		z = int(round(float(line[2])))
		poslist.append([x,y,z])
#		print x,y,z
	lastline=line



#returns an array with the numbered steps
#uses poslist



#returns an array with the numbered steps
#uses poslist
def posarray(check=0):	#check means check if there are self-intersections
	list=poslist
	message('posarray...')
	dim=len(list[0])
	bounds=[]
	for d in range(dim):
		bounds.append(min([item[d] for item in list]))
		bounds.append(max([item[d] for item in list]))
	minx,maxx,miny,maxy,minz,maxz=bounds
	# changes are here!!!!!
	from copy import deepcopy
	out = [deepcopy([]) for i in range(1+maxx-minx)]
	out = [deepcopy(out) for i in range(1+maxy-miny)]
	out = [deepcopy(out) for i in range(1+maxz-minz)]
#	out=zeros((1+maxz-minz,1+maxy-miny,1+maxx-minx),int)
	for i in range(len(list)):
#		if check and out[list[i][2]-minz][list[i][1]-miny][list[i][0]-minx] != 0:
#			return 'error'
		out[list[i][2]-minz][list[i][1]-miny][list[i][0]-minx].append(i+1)
	message('done')
	return out, len(list)

#returns a list of contacts and potential contacts as a function of distance
#uses posarray
def contacts(pr=0):
	A,strandsize=posarray()
	message('contacts...')
	actual=[0]*strandsize
	for i in range(len(A)):
		for j in range(len(A[0])):
			for k in range(len(A[0][0])):
				if A[i][j][k]!=[]:
					values=A[i][j][k]
#					print values
					comparevals=[]
					for i1 in values:
						for i2 in values:
							if i1>i2: comparevals.append(abs(i1-i2)) # bool to avoid double-counts, self-counts
					for diff in comparevals:
#						print val
						actual[abs(diff)]+=1
	possible=[0]+[strandsize-i for i in range(1,strandsize)]
	if pr: print actual, possible #comment out for long poslists#####
	message('done')
#	logbase=int(round((1+len(alphabet[list[0]]))**(1./3)))##not very general. cf z-order (no grammar) and hilbert (rotations)
	logbase=3
	return actual,possible,logbase


#uses contacts
def plot(actual,possible,logbase):
	from pylab import polyfit
	from pylab import close,plot,savefig,legend,xlabel,ylabel,title

	top=log(len(actual)-1,logbase)
	lbins=range(0,int(ceil(top))+1,1)

	print 'top:\t'+`top`
	print 'lbins:\t'+`lbins`
	
	binact=[0]*len(lbins)
	binposs=[0]*len(lbins)
	
	currbin=0

	for i in range(1,len(actual)):
		while log(i,logbase)>lbins[currbin]:
			currbin+=1
		binact[currbin]+=actual[i]
		binposs[currbin]+=possible[i]
    	#moves startval to the last empty bin other than the last bin
	startval=-1
	for i in range(len(binact)-1):
		if binact[i]==0:
			startval=i
			print 'startval moved:\t'+`startval`

	#moves stopval back one if its bin is empty
	stopval=len(binact)
	if binact[-1]==0:
		stopval=len(binact)-1
		print 'stopval moved:\t'+`stopval`

	print 'lbins:\t'+`lbins`
	print 'binact:\t'+`binact`
	print 'binposs:\t'+`binposs`

	# ratioindex avoids all zero acts
	ratioindex=range(startval+1,stopval)

	print 'ratioindex:\t'+`ratioindex`

	ratio=[log(float(binact[i])/binposs[i],logbase) for i in ratioindex]

	for start in range(0,8):
		for end in range(0,4):
			try:
				fitall=polyfit(ratioindex[start:len(ratioindex)-end:1],ratio[start:len(ratioindex)-end:1],1)
	
				print fitall

				close('all')
				a=plot(ratioindex,ratio)
			#	a=plot(ratioindex[1:-1],[fitall[1]+(fitall[0]*i) for i in ratioindex[1:-1]],'r--',label='Slope: '+`fitall[0]`[:6])
				a=plot(ratioindex[start:len(ratioindex)-end:1],[fitall[1]+(fitall[0]*i) for i in ratioindex[start:len(ratioindex)-end:1]],'r--',label='Slope:'+`fitall[0]`[:7])
	#			a=plot(ratioindex,[0+(-1.333*i) for i in ratioindex],'g--',label='Slope:'+`-1.333`[:6])#
			#	a=plot(ratioindex,[0+(-1.5*i) for i in ratioindex],'g--',label='Slope:'+`-1.500`[:6])#
				a=xlabel('Distance (log '+`logbase`+')')
				a=ylabel('Contact Probability (log '+`logbase`+')')
				a=legend()
			#	savefig(output_directory+'Scaling.'+name+'.'+`len(actual)`+'.log'+`logbase`+'.png')
				savefig(output_directory+'Scaling.'+name+'.'+'%.8i'%len(actual)+'.log'+`logbase`+'.'+`start`+'.'+`end`+'.png')
			except:
				print 'error', start, end



actual,possible,logbase=contacts(1)
#plot(actual,possible,logbase)
