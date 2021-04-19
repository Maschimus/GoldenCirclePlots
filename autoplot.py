import matplotlib as mpl
import numpy as np


def my_plotter(ax, data1, data2, xlabel, ylabel, param_dict,scientif_axis=False,plotxlabel=True):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    param_dict.update({'linewidth':1,'linestyle':'-'})
    out = ax.plot(data1, data2, **param_dict)
    if(plotxlabel):
        ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    #ax.get_yaxis().set_label_coords(-0.11,0.5)
    #ax.legend(loc='best')
    if(scientif_axis):
        ax.ticklabel_format(style='sci', axis='both', scilimits=(0,0))


    return out


def figsize(scale):
    fig_width_pt = 420.38953                       # Get this from LaTeX using \showthe\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size

def figsize3plot(scale):
    fig_width_pt = 420.38953                       # Get this from LaTeX using \showthe\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = 1./((np.sqrt(5.0)-1.0)/2.0)            # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,1.2*fig_width]
    return fig_size

def figsize2plot(scale):
    fig_width_pt = 420.38953                       # Get this from LaTeX using \showthe\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,2*fig_height]
    return fig_size



def latexfont3plot():
# Use Latex Sans-Serif font
    params = {
        'text.usetex': True,
        'text.latex.unicode': True,
        'figure.figsize': figsize3plot(0.8), # default figsize
        'axes.labelsize': 10, # LaTeX default is 10pt font.
        'font.size': 10,
        'legend.fontsize': 9, # Make the legend/label fonts a little smaller
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'text.latex.preamble': [
            r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
            r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
    #        r'\usepackage{helvet}',   # if you want to use helvetica
    #        r'\usepackage[helvet]{sfmath}' # if you want to use helvetica
            r'\usepackage{lmodern}',
            r'\renewcommand*\familydefault{\sfdefault}' # Only if the base font of the document is to be sans serif
            r'\usepackage{sfmath}'
            ]
        }
    mpl.rcParams.update(params)

def latexfont():
# Use Latex Sans-Serif font
    params = {
        'text.usetex': True,
        'text.latex.unicode': True,
        'figure.figsize': figsize(0.8), # default figsize
        'axes.labelsize': 10, # LaTeX default is 10pt font.
        'font.size': 10,
        'legend.fontsize': 9, # Make the legend/label fonts a little smaller
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'text.latex.preamble': [
            r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
            r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
    #        r'\usepackage{helvet}',   # if you want to use helvetica
    #        r'\usepackage[helvet]{sfmath}' # if you want to use helvetica
            r'\usepackage{lmodern}',
            r'\renewcommand*\familydefault{\sfdefault}' # Only if the base font of the document is to be sans serif
            r'\usepackage{sfmath}'
            ]
        }
    mpl.rcParams.update(params)
    
def latexfont2plot():
# Use Latex Sans-Serif font
    params = {
        'text.usetex': True,
        'text.latex.unicode': True,
        'figure.figsize': figsize2plot(0.8), # default figsize
        'axes.labelsize': 10, # LaTeX default is 10pt font.
        'font.size': 10,
        'legend.fontsize': 9, # Make the legend/label fonts a little smaller
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'text.latex.preamble': [
            r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
            r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
    #        r'\usepackage{helvet}',   # if you want to use helvetica
    #        r'\usepackage[helvet]{sfmath}' # if you want to use helvetica
            r'\usepackage{lmodern}',
            r'\renewcommand*\familydefault{\sfdefault}' # Only if the base font of the document is to be sans serif
            r'\usepackage{sfmath}'
            ]
        }
    mpl.rcParams.update(params)
