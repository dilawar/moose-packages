from moose import Annotator
from PyQt4.QtGui import QColor
import numpy as np
import os
import config
import pickle
from random import randint

colormap_file = open(os.path.join(config.settings[config.KEY_COLORMAP_DIR], 'rainbow2.pkl'),'rb')
colorMap = pickle.load(colormap_file)
colormap_file.close()

def getRandColor():
    color = (np.random.randint(low=0, high=255, size=3)).tolist()
    return QColor(color[0],color[1],color[2])
    

def getColor(iteminfo):
    """ Getting a textcolor and background color for the given  mooseObject \
        If textcolor is empty replaced with green \
           background color is empty replaced with blue
           if textcolor and background is same as it happend in kkit files \
           replacing textcolor with random color\
           The colors are not valid there are siliently replaced with some values \
           but while model building can raise an exception
    """
    textcolor = Annotator(iteminfo).getField('textColor')
    bgcolor = Annotator(iteminfo).getField('color')
    if(textcolor == ''): textcolor = 'green'
    if(bgcolor == ''): bgcolor = 'blue'
    if(textcolor == bgcolor):textcolor = getRandColor()
    textcolor = colorCheck(textcolor,"fc")
    bgcolor = colorCheck(bgcolor,"bg")
    return(textcolor,bgcolor)

def colorCheck(fc_bgcolor,fcbg):
    """ textColor or background can be anything like string or tuple or list \
        if string its taken as colorname further down in validColorcheck checked for valid color, \
        but for tuple and list its taken as r,g,b value.
    """
    if isinstance(fc_bgcolor,str):
        if fc_bgcolor.startswith("#"):
            fc_bgcolor = QColor(fc_bgcolor)
        elif fc_bgcolor.isdigit():
            """ color is int  a map from int to r,g,b triplets from pickled color map file """
            tc = int(fc_bgcolor)
            tc = 2*tc
            pickledColor = colorMap[tc]
            fc_bgcolor = QColor(*pickledColor)

        elif fc_bgcolor.isalpha() or fc_bgcolor.isalnum():
            fc_bgcolor = validColorcheck(fc_bgcolor)
        else:
            fc_bgcolor = QColor(*eval(fc_bgcolor))
            # fc_bgcolor = validColorcheck(fc_bgcolor)
    return(fc_bgcolor)

def validColorcheck(color):
	''' 
        Both in Qt4.7 and 4.8 if not a valid color it makes it as back but in 4.7 there will be a warning mssg which is taken here
        checking if textcolor or backgroundcolor is valid color, if 'No' making white color as default
        where I have not taken care for checking what will be backgroundcolor for textcolor or textcolor for backgroundcolor 
        '''
        if QColor(color).isValid():
            return (QColor(color))
        else:
            return(QColor("white"))

