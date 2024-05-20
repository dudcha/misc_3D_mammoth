name='sierpinski'
alphabet={}
alphabet['1']=list('1')
alphabet['2']=list('2')
alphabet['3']=list('3')
alphabet['4']=list('4')

alphabet['5']=list('1')
alphabet['6']=list('2')
alphabet['7']=list('3')
alphabet['8']=list('4')

alphabet['F']=list('F')
alphabet['+']=list('+')
alphabet['-']=list('-')

rewrite={}

rewrite['5']=list('5FF+5-1-5FF+5')
rewrite['F']=list('F')
rewrite['+']=list('+')
rewrite['-']=list('-')

rewrite['1']=list('1')
rewrite['2']=list('2')
rewrite['3']=list('3')
rewrite['4']=list('4')

symbols=list('5-1-5-1') #to close, add '-1'








#an alternate, much less elegant version which
#1. does use rotations, and therefore multiplies the number of elements by four
#2. partitions certain rewritten segments into start ('1') and end ('2') segments
"""alphabet={}
alphabet['R1']=list('r')
alphabet['R2']=list('r')
alphabet['U1']=list('u')
alphabet['U2']=list('u')
alphabet['L1']=list('l')
alphabet['L2']=list('l')
alphabet['D1']=list('d')
alphabet['D2']=list('d')
alphabet['1']=list('1')
alphabet['2']=list('2')
alphabet['3']=list('3')
alphabet['4']=list('4')



rewrite={}
rewrite['R1']=['U2','1','R1']
rewrite['R2']=['R2','4','D1']
rewrite['U1']=['L2','2','U1']
rewrite['U2']=['U2','1','R1']
rewrite['L1']=['D2','3','L1']
rewrite['L2']=['L2','2','U1']
rewrite['D1']=['R2','4','D1']
rewrite['D2']=['D2','3','L1']
rewrite['1']=['R2']+list('412')+['U1']
rewrite['2']=['U2']+list('123')+['L1']
rewrite['3']=['L2']+list('234')+['D1']
rewrite['4']=['D2']+list('341')+['R1']


symbols=list('1234')
"""
