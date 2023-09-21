import seaborn as sns
import matplotlib.pyplot as plt


def cont_plots(df, cont):
    '''
    scatter plot for all continous
    '''
    for i in cont:
        for l in cont:
            if i != l:
                sns.scatterplot(data=df, x=i , y=l)
                plt.title(f'{l.capitalize()} by {i.capitalize()}')
                plt.xlabel(i.capitalize())
                plt.ylabel(l.capitalize())
                plt.show()

                
def contnious_plot(df, cont,target):
    '''
    plots target continous variable against all other continuos varibles.
    '''
    for i in cont:
        l = target
        if i != l:
            sns.scatterplot(data=df, x=i , y=l)
            plt.title(f'{l.capitalize()} by {i.capitalize()}')
            plt.xlabel(i.capitalize())
            plt.ylabel(l.capitalize())
            plt.show()

            
def cont_plots(df, cont):
    '''
    scatter plot for all continous
    '''
    for i in cont:
        for l in cont:
            if i != l:
                sns.scatterplot(data=df, x=i , y=l)
                plt.title(f'{l.capitalize()} by {i.capitalize()}')
                plt.xlabel(i.capitalize())
                plt.ylabel(l.capitalize())
                plt.show()