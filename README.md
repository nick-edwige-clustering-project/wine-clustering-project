# Wine-clustering-project


# Project Description

* Construct ML models that predict wine quality scores.
* Use unpervised learning clustering models to derive insights.


# Project Goal
* Predict the quality of wine while incorporating unsupervised learning techniques.
* What are the drivers for quality?
* What are the strongest features to focus on for improving quality
* Present our process and findings to the data science team.


# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from https://data.world/food/wine-quality.
3) Put the data in the file containing the cloned repo.
4) Run notebook.


# Seed State
seed = 100


# Modules / Files

| Module/Filename        | Description                                                                 |
|:-----------------------|:----------------------------------------------------------------------------|
| prepare.py             | Scrubs, and splits the wines data.                                |
| evaluate.py            | Contains functions to evaluate model performance and metrics.               |
| model.py               | Contains functions to create and evaluate different models.                 |
| README.md              | Provides an overview of the project.                                        |
| viz.py                 | A module dedicated to creating visualizations for data analysis.            |

# Data Dictionary
| Feature                | Definition                                                           |
|:-----------------------|:---------------------------------------------------------------------|
| fixed acidity          | Numeric. The amount of fixed acidity present in the wine, measured in g/dm³. |
| volatile acidity       | Numeric. The amount of volatile acidity present in the wine, measured in g/dm³. |
| citric acid            | Numeric. The amount of citric acid present in the wine, measured in g/dm³. |
| residual sugar         | Numeric. The amount of residual sugar present in the wine, measured in g/dm³. |
| chlorides              | Numeric. The amount of chlorides present in the wine, measured in g/dm³. |
| free sulfur dioxide    | Numeric. The amount of free sulfur dioxide present in the wine, measured in mg/dm³. |
| total sulfur dioxide   | Numeric. The total amount of sulfur dioxide present in the wine, measured in mg/dm³. |
| density                | Numeric. The density of the wine, typically measured in g/cm³. |
| pH                     | Numeric. The pH value of the wine, indicating its acidity or basicity. |
| sulphates              | Numeric. The amount of sulphates present in the wine, measured in g/dm³. |
| alcohol                | Numeric. The alcohol content in the wine, measured in percentage volume/volume (% vol). |
| quality                | Numeric. The quality rating assigned to the wine, typically on a scale from 0 to 10. |

# Initial Thoughts and Questions

* What is the best way to use clustering to provide value for building predictive models.

* Are there any other useful devides besides red and white wine?


# Takeaways and Conclusions
* Clustering did not meaningfully impact our models as we used it. If we leaned into red versus white then we could perhaps increase our model accuracy.

* Our model was able to beat the baseline model by:


# Next Steps

* Explore Davies-Bouldin Index, & Calinski-Harabasz Index for determining minimum number of ideal clusters for the different clustering models. This will allow a progromatic assessment of clustering.
* Explore silhouette scoreing as means to determine quality of clustering.
* Cluster all variables by white and red. The clusters that we did do show that a lot of the data is representented in that catagory. Clustering might allow us to greatly reduce noise using those two obvious splits.
* Create two seperate models for red and white respectively.