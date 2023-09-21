import seaborn as sns
import matplotlib.pyplot as plt
import explore


def cont_plots(df):
    '''
    scatter plot for all continuous
    '''
    cat, cont = explore.cat_or_cont(df)
    for i in cont:
        for l in cont:
            if i != l:
                sns.scatterplot(data=df, x=i , y=l)
                plt.title(f'{l.capitalize()} by {i.capitalize()}')
                plt.xlabel(i.capitalize())
                plt.ylabel(l.capitalize())
                plt.show()

                
def continuous_plot(df,target):
    '''
    plots target continuous variable against all other continuos varibles.
    '''
    cat, cont = explore.cat_or_cont(df)
    for i in cont:
        l = target
        if i != l:
            sns.scatterplot(data=df, x=i , y=l)
            plt.title(f'{l.capitalize()} by {i.capitalize()}')
            plt.xlabel(i.capitalize())
            plt.ylabel(l.capitalize())
            plt.show()

            
def cont_plots(df):
    '''
    scatter plot for all continuous
    '''
    cat, cont = explore.cat_or_cont(df)
    for i in cont:
        for l in cont:
            if i != l:
                sns.scatterplot(data=df, x=i , y=l)
                plt.title(f'{l.capitalize()} by {i.capitalize()}')
                plt.xlabel(i.capitalize())
                plt.ylabel(l.capitalize())
                plt.show()