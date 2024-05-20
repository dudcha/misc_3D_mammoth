name='moore'

alphabet={}
alphabet['M']=list('F+F+F')
alphabet['R']=list('F-F-F')
alphabet['L']=list('F+F+F')
alphabet['+']=list('+')
alphabet['-']=list('-')
alphabet['F']=list('F')

rewrite={}
rewrite['M']=list('-L-F-LFL-F-L')
rewrite['R']=list('-L-FR+F+RF-L-')
rewrite['L']=list('+R+FL-F-LF+R+')
rewrite['+']=list('+')
rewrite['-']=list('-')
rewrite['F']=list('F')

symbols=list('-M')
