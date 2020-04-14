import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def qp(input,x=[None],cols=0):
    ''' Creates a plot of the input with pandas in a single call. figsize = (20,8)
        returns the axes of the plot so that you can modify
        Usage : p = qp(samples)
        p.set(title="title")
    '''
    if cols == 0:
        df=pd.DataFrame(input)
    else:
        df=pd.DataFrame(input,columns=cols)
    #if user provides the x axis
    
    if x[0] != None:
        #print(x)
        df['x']=x
        return df.plot(x='x',figsize=(20,8))
    
    p = df.plot(figsize=(20,8))
    p.title.set_fontsize(25)
    p.xaxis.label.set_fontsize(20)
    p.yaxis.label.set_fontsize(20)
    return p

def darken(pl,title="",lw=1.0):
    pl.set_title(title,color='white')
    pl.figure.set_facecolor("#000000")
    pl.axes.set_facecolor('#000000')
    pl.lines[0].set(color='lightblue', linewidth=lw)

    pl.axes.spines['left'].set_color('white')
    pl.axes.spines['top'].set_color('white')
    pl.axes.spines['bottom'].set_color('white')
    pl.axes.xaxis.label.set_color('white')
    pl.axes.yaxis.label.set_color('white')
    pl.axes.tick_params( colors='white')