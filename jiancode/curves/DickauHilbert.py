#alternate implementation of Hilbert, more elegant, same results

name='dickauhilbert'

alphabet={}
alphabet['R']=list('-F+F+F-')
alphabet['L']=list('+F-F-F+')
alphabet['+']=list('+')
alphabet['-']=list('-')
alphabet['F']=list('F')

rewrite={}
rewrite['R']=list('-LF+RFR+FL-')
rewrite['L']=list('+RF-LFL-FR+')
rewrite['+']=list('+')
rewrite['-']=list('-')
rewrite['F']=list('F')
symbols=list('L')
