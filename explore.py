import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind, spearmanr

def reajust_range(wine):
    wine = wine[(wine.fixed_acidity < 12) & (wine.fixed_acidity > 4.5)]
    wine = wine[wine.volatile_acidity < 0.8]
    wine = wine[wine.citric_acid < 0.8]
    wine = wine[wine.residual_sugar < 22]
    wine = wine[wine.chlorides < .12]
    wine = wine[wine.free_sulfur_dioxide < 80]
    wine = wine[wine.total_sulfur_dioxide < 275]
    wine = wine[wine.density < 1.01]
    wine = wine[wine.pH < 3.8]
    wine = wine[wine.sulphates < 1.00]
    # wine = wine[wine.alcohol < 1000]
    return wine


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


def ttest_viz(df, cat,cont):
    '''
    run and plots ttest for categorical features against a continuous target
    '''    
    for i in cont:
        print(f'H_0 {i} has no effect on {cat[0]}')
        print(f'H_a {i} has an effect on {cat[0]}')

        t_stat, p_value = spearmanr(df[i], df[cat[0]])
        
        # box plot
        sns.barplot(data=df, y=i, x=cat[0])
        plt.title(f'{i.capitalize()} and {cat[0].capitalize()}')
        plt.ylabel(i.capitalize())
        plt.xlabel(f'{cat[0].capitalize()}')
        plt.show()
        
        if p_value < 0.05:
            print(f'Reject the null hypothesis: {i} has an effect on {cat[0]}. (p-value: {p_value:.4e})')
            print()
            print()
        else:
            print(f"Fail to reject the null hypothesis: No significant evidence to suggest that {i} affects {cat[0]}. (p-value: {p_value:.4e})")
            print()
            print()
            
 
