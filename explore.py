import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind, spearmanr

def red_white(df):
    '''
    compares the differneces between red and white wine
    '''
    red = df[df.wine_type == 'red']
    white = df[df.wine_type == 'white']
    for col in df.columns:
        if col == 'wine_type':
            continue
        plt.figure()
        sns.histplot(df, x=col, hue='wine_type')
        plt.axvline(x = red[col].mean(), color = 'blue', linestyle='dashed')
        plt.axvline(x = white[col].mean(), color = 'red', linestyle='dashed')
        plt.legend(labels=['average red wine','average white wine','white wine','red wine'])
        plt.show()


def cat_or_cont(df) -> list:
    '''
    find all continuous and catagorical features
    
    return: 2 lists of column names
    '''
    cont = []
    cat = []
    
    #takes all numerical colums
    num_df = df.select_dtypes('number') 
    
    for col in num_df:
        if num_df[col].nunique() > 20:
            cont.append(col)
        else:
            cat.append(col)
    return cat, cont


def ttest_viz(df):
    '''
    run and plots ttest for categorical features against a continuous target
    '''    
    cat, cont = cat_or_cont(df)
    for i in cont:
        print(f'Does the feature "{i}" have an effect on {cat[0]}?')
        print()
        print(f'H_0 {i} has no effect on {cat[0]}')
        print(f'H_a {i} has an effect on {cat[0]}')

        r_value, p_value = spearmanr(df[i], df[cat[0]])
        
        # box plot
        sns.barplot(data=df, y=i, x=cat[0])
        plt.title(f'{i.capitalize()} and {cat[0].capitalize()}')
        plt.grid(linestyle='-.', axis='y')  # Add grid line for better visualization
        plt.ylabel(i.capitalize())
        plt.xlabel(f'{cat[0].capitalize()}')
        plt.show()
        
        if p_value < 0.05:
            print(f'Reject the null hypothesis: {i} has an effect on {cat[0]}. (p-value: {p_value:.4e})')
            print(r_value)
            print('======================')
            print('======================')
            print()
            print()
        else:
            print(f"Fail to reject the null hypothesis: No significant evidence to suggest that {i} affects {cat[0]}. (p-value: {p_value:.4e})")
            print(r_value)
            print()
            print()
            
 
