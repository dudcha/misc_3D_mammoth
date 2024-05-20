#this program only generates the Lebesgue curve


#!/usr/bin/python
from time import time
from sys import argv, stdout
from numpy import array, dot, zeros
from math import log, ceil

output_directory='output/'
name='lebesgue'
def message(text):
	print '%10.5f'%(time()-benchmark)+'\t'+text

benchmark=time()
message('begin timing')

def poslist(steps):
	out=[]
	for n in range(4**steps):
		if n%1000000==0:
			message('poslist\t'+`n`)
		number=[n>>p&1 for p in range(2*steps-1,-1,-1)]
		# write out the first 4**steps binary numbers which require 2*steps digits
		binx=number[1:len(number):2]	#x is the binary number constructed by using every other (odd) digit
		biny=number[0:len(number):2]	#y is the binary number constructed by using every other (even) digit
		x=sum([binx[i]*2**(len(binx)-1-i) for i in range(len(binx))])	#convert to decimal
		y=sum([biny[i]*2**(len(biny)-1-i) for i in range(len(biny))])	#convert to decimal
		out.append([x,y,0])
	return out

#returns an array with the numbered steps
#uses poslist
def posarray(steps):
	list=poslist(steps)
	message('posarray...')
	dim=len(list[0])
	bounds=[]
	for d in range(dim):
		bounds.append(min([item[d] for item in list]))
		bounds.append(max([item[d] for item in list]))
	minx,maxx,miny,maxy,minz,maxz=bounds
	out=zeros((1+maxz-minz,1+maxy-miny,1+maxx-minx),int)
	for i in range(len(list)):
		if out[list[i][2]-minz,list[i][1]-miny,list[i][0]-minx] != 0:
			return 'error'
		out[list[i][2]-minz,list[i][1]-miny,list[i][0]-minx]=i+1
	message('done')
	return out

#returns a list of contacts and potential contacts as a function of distance
#uses posarray
def contacts(steps):
	A=posarray(steps)
	message('contacts...')
	strandsize=int(A.max())
	actual=[0]*strandsize
	for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			for k in range(A.shape[2]):
				if A[i][j][k]!=0:
					valref=A[i][j][k]
					comparevals=[]
					if i>0 and A[(i-1,j,k)]: comparevals.append(A[(i-1,j,k)])
					if j>0 and A[(i,j-1,k)]: comparevals.append(A[(i,j-1,k)])
					if k>0 and A[(i,j,k-1)]: comparevals.append(A[(i,j,k-1)])
					for val in comparevals:
						actual[abs(valref-val)]+=1
	possible=[0]+[strandsize-i for i in range(1,strandsize)]
#	print actual, possible #comment out for long poslists
	message('done')
	logbase=4
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

	for start in range(0,4):
		for end in range(0,4):
			fitall=polyfit(ratioindex[start:len(ratioindex)-end:1],ratio[start:len(ratioindex)-end:1],1)
	
			print fitall

			close('all')
			a=plot(ratioindex,ratio)
		#	a=plot(ratioindex[1:-1],[fitall[1]+(fitall[0]*i) for i in ratioindex[1:-1]],'r--',label='Slope: '+`fitall[0]`[:6])
			a=plot(ratioindex[start:len(ratioindex)-end:1],[fitall[1]+(fitall[0]*i) for i in ratioindex[start:len(ratioindex)-end:1]],'r--',label='Slope:'+`fitall[0]`[:6])
#			a=plot(ratioindex,[0+(-1.333*i) for i in ratioindex],'g--',label='Slope:'+`-1.333`[:6])#
		#	a=plot(ratioindex,[0+(-1.5*i) for i in ratioindex],'g--',label='Slope:'+`-1.500`[:6])#
			a=xlabel('Distance (log '+`logbase`+')')
			a=ylabel('Contact Probability (log '+`logbase`+')')
			a=legend()
		#	savefig(output_directory+'Scaling.'+name+'.'+`len(actual)`+'.log'+`logbase`+'.png')
			savefig(output_directory+'Scaling.'+name+'.'+'%.8i'%len(actual)+'.log'+`logbase`+'.'+`start`+'.'+`end`+'.png')

#actual,possible,logbase=contacts(int(argv[1]))
#plot(actual,possible,logbase)

#print posarray(int(argv[1]))

f=open('poslists/'+name+'/'+name+argv[1]+'.txt', 'w')
for point in poslist(int(argv[1])):
	f.write(`point[0]`+'\t'+`point[1]`+'\t'+`point[2]`+'\n')
f.close()
