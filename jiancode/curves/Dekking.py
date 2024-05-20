name='dekking'

alphabet={}
alphabet['R']=list('F-F-F')
alphabet['L']=list('F+F+F')
alphabet['+']=list('+')
alphabet['-']=list('-')
alphabet['F']=list('F')
alphabet['W']=list('')
alphabet['X']=list('')
alphabet['Y']=list('')
alphabet['Z']=list('')

rewrite={}
rewrite['F']=list('')
rewrite['W']=list('FW+F-XFW-F+Z')
rewrite['X']=list('++F--Y-F+Z++F--Y-F+Z')
rewrite['Y']=list('++F--Y+F-X')
rewrite['Z']=list('FW+F-X')
rewrite['+']=list('+')
rewrite['-']=list('-')
symbols=list('WZYX')

