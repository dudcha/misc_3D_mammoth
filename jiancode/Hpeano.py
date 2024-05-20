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
#		print line
#		print float(line[0])*2,float(line[1])/(sqrt(3)/4.0),line[2]
		x = int(round(float(line[0])*2))
		y = int(round(float(line[1])/(sqrt(3)/4.0)))
		z = int(round(float(line[2])))
		poslist.append([x,y,z])
#		print x,y,z
	lastline=line



#returns an array with the numbered steps
#uses poslist

miny=0
maxy=0
def posarray(check=1):	#check means check if there are self-intersections
	list=poslist
	message('posarray...')
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
	message('done')
	return out


#returns a list of contacts and potential contacts as a function of distance
#uses posarray
def contacts():
	A=posarray()
	message('contacts...')
	strandsize=int(A.max())
	actual=[0]*strandsize
	for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			for k in range(A.shape[2]):
				if A[i][j][k]!=0:
					valref=A[i][j][k]
					comparevals=[]
					if k>1 and A[(i,j,k-2)]:
						comparevals.append(A[(i,j,k-2)])
					if k>0 and j>0  and A[(i,j-2,k-1)]:
						comparevals.append(A[(i,j-2,k-1)])##
					if k>1 and j<(maxy-miny-1) and A[(i,j+2,k-1)]:
						comparevals.append(A[(i,j+2,k-1)])
					for val in comparevals:
						actual[abs(valref-val)]+=1
	possible=[0]+[strandsize-i for i in range(1,strandsize)]
	#print actual, possible #comment out for long poslists#####
	message('done')
	logbase=7
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
	# range defines the number of excluded ends
	for start in range(0,3):
		for end in range(0,3):
			try:
				fitall=polyfit(ratioindex[start:len(ratioindex)-end:jump],ratio[start:len(ratioindex)-end:jump],1)
	
				print fitall, start, end

				close('all')
				a=plot(ratioindex,ratio)
			#	a=plot(ratioindex[1:-1],[fitall[1]+(fitall[0]*i) for i in ratioindex[1:-1]],'r--',label='Slope: '+`fitall[0]`[:6])
				a=plot(ratioindex[start:len(ratioindex)-end:jump],[fitall[1]+(fitall[0]*i) for i in ratioindex[start:len(ratioindex)-end:jump]],'r--',label='Slope:'+`fitall[0]`[:7])
	#			a=plot(ratioindex,[0+(-1.333*i) for i in ratioindex],'g--',label='Slope:'+`-1.333`[:6])#
			#	a=plot(ratioindex,[0+(-1.5*i) for i in ratioindex],'g--',label='Slope:'+`-1.500`[:6])#
				a=xlabel('Distance (log '+`logbase`+')')
				a=ylabel('Contact Probability (log '+`logbase`+')')
				a=legend()
			#	savefig(output_directory+'Scaling.'+name+'.'+`len(actual)`+'.log'+`logbase`+'.png')
				if jump==1:
					savefig(output_directory+'Scaling.'+name+'.'+'%.8i'%len(actual)+'.log'+`logbase`+'.'+`start`+'.'+`end`+'.png')
				else:
					savefig(output_directory+'Scaling.'+name+'.'+'%.8i'%len(actual)+'.log'+`logbase`+'.step'+`jump`+'.'+`start`+'.'+`end`+'.png')
			except:
				print 'error', start, end


#for visualizing shapes
#print posarray()

actual,possible,logbase=contacts()
plot(actual,possible,logbase)



#iteration, logbase, step
