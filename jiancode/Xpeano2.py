###posarray, contacts modified for self-intersecting curves!!!!
#this second version of Xpeano uses a dictionary instead of an array
#for the posarray
#however, it's not appreciably faster

#!/usr/bin/python
from time import time
from sys import argv, stdout
from numpy import array, dot, zeros
from math import log, ceil

jump=2

#from Dragon import *
#from Levy import *
#from Kochright import *
#from Dekking import *

output_directory='output/'

def message(text):
	print '%10.5f'%(time()-benchmark)+'\t'+text

benchmark=time()
message(name)

#rewrites the string using rewrite
def step(symblist):
	out=[]
	for item in symblist:
		out.extend(rewrite[item])
	return out

#rewrites the specified number of times
#uses step
def iterate(symblist,steps):
	for i in range(steps-1):
		message('iteration\t'+`i+1`)
		symblist=step(symblist)
	return symblist

#converts to geometric instructions
#uses iterate
def instructions(symblist,steps):
	symblist=iterate(symblist,steps)
	message('alphabetize...')
	out=[]
	for symbol in symblist:
		out.extend(alphabet[symbol])
	message('done')
	return out


#returns a list of position coordinates
#uses instructions
def poslist(symblist, steps):
	#transposed rotation matrices
	#right multiply for rotations from the fixed reference frame
	#left multiply for turtle rotations
	#dependent on Processing coordinate specifications
	#(x-axis points right, y-axis points down, z-axis points out)
	rot={}
	rot['+']=array([	[0,1,0],	[-1,0,0],	[0,0,1]])
	rot['-']=array([	[0,-1,0],	[1,0,0],	[0,0,1]])
	rot['L']=array([	[0,0,1],	[0,1,0],	[-1,0,0]])
	rot['R']=array([	[0,0,-1],	[0,1,0],	[1,0,0]])
	rot['U']=array([	[1,0,0],	[0,0,1],	[0,-1,0]])
	rot['D']=array([	[1,0,0],	[0,0,-1],	[0,1,0]])

	delta={}
	delta['F']=array([1,0,0])
	delta['l']=array([-1,0,0])
	delta['r']=array([1,0,0])
	delta['u']=array([0,-1,0])
	delta['d']=array([0,1,0])
	delta['i']=array([0,0,-1])
	delta['o']=array([0,0,1])

	delta['1']=array([1,-1,0])
	delta['2']=array([-1,-1,0])
	delta['3']=array([-1,1,0])
	delta['4']=array([1,1,0])

	orientation = array([[1,0,0],[0,1,0],[0,0,1]])
	position = array([0,0,0])
	out=[]
	out.append(list(position))
	counter=0
	for i in instructions(symblist, steps):
		if counter%1000000==0:
			message('poslist\t'+`counter`)
		try:
			orientation=dot(rot[i],orientation)
		except:
			position+=dot(delta[i],orientation)
			out.append(list(position))
		counter+=1
	return out

#returns an array with the numbered steps
#uses poslist
def posarray(symblist,steps,check=1):	#check means check if there are self-intersections
	list=poslist(symblist,steps)
	message('posarray...')
	dim=len(list[0])
	bounds=[]
	for d in range(dim):
		bounds.append(min([item[d] for item in list]))
		bounds.append(max([item[d] for item in list]))
	minx,maxx,miny,maxy,minz,maxz=bounds
	# changes are here!!!!!
	from copy import deepcopy
	out={}
	for i in range(len(list)):
		try:
			out[`list[i][2]`+'-'+`list[i][1]`+'-'+`list[i][0]`].append(i+1)
		except:
			out[`list[i][2]`+'-'+`list[i][1]`+'-'+`list[i][0]`]=[i+1]

	message('done')
	return out, len(list)

#returns a list of contacts and potential contacts as a function of distance
#uses posarray
def contacts(symblist,steps):
	A,strandsize=posarray(symblist,steps)
	message('contacts...')
	actual=[0]*strandsize
	for k in A:
		values=A[k]
		if len(values)>1:
#			print values
			comparevals=[]
			for i1 in values:
				for i2 in values:
					if i1>i2: comparevals.append(abs(i1-i2)) # bool to avoid double-counts, self-counts
			for diff in comparevals:
				#print val
				actual[abs(diff)]+=1
	possible=[0]+[strandsize-i for i in range(1,strandsize)]
	#print actual, possible #comment out for long poslists#####
	message('done')
#	logbase=int(round((1+len(alphabet[list[0]]))**(1./3)))##not very general. cf z-order (no grammar) and hilbert (rotations)
	logbase=2
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
	for i in range(len(binact)-2):
		if binact[i]==0:
			startval=i
			print 'startval moved:\t'+`startval`

	#moves stopval back one if its bin is empty
	stopval=len(binact)
	if binact[-1]==0:
		stopval=len(binact)-1
		print 'stopval moved:\t'+`stopval`
		if binact[-2]==0:
			stopval=len(binact)-2
			print 'stopval moved:\t'+`stopval`

	print 'lbins:\t'+`lbins`
	print 'binact:\t'+`binact`
	print 'binposs:\t'+`binposs`

	# ratioindex avoids all zero acts
	ratioindex=range(startval+1,stopval)

	print 'ratioindex:\t'+`ratioindex`

	ratio=[log(float(binact[i])/binposs[i],logbase) for i in ratioindex]

	for start in range(0,13):
		for end in range(0,8):
			try:
				fitall=polyfit(ratioindex[start:len(ratioindex)-end:jump],ratio[start:len(ratioindex)-end:jump],1)
				print fitall
				close('all')
				a=plot(ratioindex,ratio)
			#	a=plot(ratioindex[1:-1],[fitall[1]+(fitall[0]*i) for i in ratioindex[1:-1]],'r--',label='Slope: '+`fitall[0]`[:6])
				a=plot(ratioindex[start:len(ratioindex)-end:jump],[fitall[1]+(fitall[0]*i) for i in ratioindex[start:len(ratioindex)-end:jump]],'r--',label='Slope:'+`fitall[0]`[:7])
	#			a=plot(ratioindex,[0+(-1.333*i) for i in ratioindex],'g--',label='Slope:'+`-1.333`[:6])#
			#	a=plot(ratioindex,[0+(-1.5*i) for i in ratioindex],'g--',label='Slope:'+`-1.500`[:6])#
				a=xlabel('Distance (log '+`logbase`+')')
				a=ylabel('Contact Probability (log '+`logbase`+')')
				a=legend()
				if jump==1:
					savefig(output_directory+'Scalingexp.'+name+'.'+'%.8i'%len(actual)+'.log'+`logbase`+'.'+`start`+'.'+`end`+'.png')
				else:
					savefig(output_directory+'Scalingexp.'+name+'.'+'%.8i'%len(actual)+'.log'+`logbase`+'.step'+`jump`+'.'+`start`+'.'+`end`+'.png')
			except:
				print 'error', start, end


def write(end):
	for number in range(1,end+1):
		f=open('poslists/'+name+'/'+name+`number`+'.txt', 'w')
		for point in poslist(symbols,number):
			f.write(`point[0]`+'\t'+`point[1]`+'\t'+`point[2]`+'\n')
		f.close()
		print 'written'+`number`


actual,possible,logbase=contacts(symbols,int(argv[1]))
plot(actual,possible,logbase)
