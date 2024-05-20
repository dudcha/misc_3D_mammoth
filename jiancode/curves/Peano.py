"""name='2x3peano'
alphabet{}
alphabet['CL']=['F','+','F','+','F','-','F','-','F']
alphabet['CR']=['F','-','F','-','F','+','F','+','F']"""

name='peano'
alphabet={}
alphabet['CL']=['F','F','+','F','+','F','F','-','F','-','F','F']
alphabet['CR']=['F','F','-','F','-','F','F','+','F','+','F','F']

"""name='4x3peano'
alphabet={}
alphabet['CL']=['F','F','F','+','F','+','F','F','F','-','F','-','F','F','F']
alphabet['CR']=['F','F','F','-','F','-','F','F','F','+','F','+','F','F','F']"""

"""name='5x3peano'
alphabet={}
alphabet['CL']=['F','F','F','F','+','F','+','F','F','F','F','-','F','-','F','F','F','F']
alphabet['CR']=['F','F','F','F','-','F','-','F','F','F','F','+','F','+','F','F','F','F']"""

alphabet['+']=['+']
alphabet['-']=['-']
alphabet['F']=['F']

rewrite={}
rewrite['CL']=['CL','F','CR','F','CL','+','F','+','CR','F','CL','F','CR','-','F','-','CL','F','CR','F','CL']
rewrite['CR']=['CR','F','CL','F','CR','-','F','-','CL','F','CR','F','CL','+','F','+','CR','F','CL','F','CR']
rewrite['+']=['+']
rewrite['-']=['-']
rewrite['F']=['F']

symbols=['CL']
