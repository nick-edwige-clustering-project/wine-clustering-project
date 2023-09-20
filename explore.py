import matplotlib.pyplot as plt
import seaborn as sns

for col in wine.columns:
    '''
    displays distribution for all feature of wine
    '''
    plt.figure()
    sns.histplot(wine, x=col, hue='wine_type')
    plt.show()