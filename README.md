# GoldenCirclePlots
### The most beautiful plot. Do you want to make plots with the perfect ratio? Here we go! 


Download the file and add autoplotter.py to your project.

### Import
Use `from autoplot import my_plotter`


### Usage

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
