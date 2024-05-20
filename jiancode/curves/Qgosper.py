name='qgosper'

alphabet={}

alphabet['X'] = list('F-F-F+F+F-F-FF+F+FFF-F+F+FF+F-FF-F-F+F+FF-')
alphabet['Y'] = list('+FF-F-F+F+FF+F-FF-F-F+FFF-F-FF+F+F-F-F+F+F')

alphabet['+']=list('+')
alphabet['-']=list('-')
alphabet['F']=list('F')


rewrite={}

rewrite['X'] = list('XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-')
rewrite['Y'] = list('+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY')

rewrite['+']=list('+')
rewrite['-']=list('-')
rewrite['F']=list('F')

symbols=list('-YF')
