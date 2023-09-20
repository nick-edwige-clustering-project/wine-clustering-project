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
                
for i in cont:
    l = residual_sugar
    if i != l:
        sns.scatterplot(data=df, x=i , y=l)
        plt.title(f'{l.capitalize()} by {i.capitalize()}')
        plt.xlabel(i.capitalize())
        plt.ylabel(l.capitalize())
        plt.show()