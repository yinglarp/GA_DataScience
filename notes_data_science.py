classification (got labels used, supervised learning) vs clustering (no labels, unsupervised learning)

KNN - classification - calculate the distance between data points and make a prediction
logistics regression -assume data linear relationship, Logistic Regression is usually used to predict result according to the probability.
(sample: http://hamelg.blogspot.sg/2015/11/python-for-data-analysis-part-28.html)

decision tree - can handle non-linear relationship, prone to overfitting, To use Decision Tree, you should transform the continuous variable into categorical.
URL: https://datascience.stackexchange.com/questions/6048/decision-tree-or-logistic-regression

Model Evaulation Metrics:
Regression vs classification models: For classification, use confusion matrix,accuracy,precision,recall. For regression, use RMSE etc
Precision: High Precision = few false positive (Out of your dataset that the model makes a predictions, how many are correctly predicted?)
Recall: High Recall = Few false negative (Out of your dataset of 100 observations, if 10 of the y_responses are positive, how many does your model correctly predict it as true)
Typically, we want higer recall than precision,based on business objetives. To improve both measures, either increase the data sample size to run more iterations or fine tune the model variables

Moving Average = greater weights on more recent timespan than later timespan as recent events are more significant
Autocorrelation = how a variable correlates to itself (1 variable) across different timespan. Specifically, how related are variables earlier in time with 
variables later in time. Autocorrelations are a measure of how much a data point is dependent on previous data points.

peterkai.15@gmail.com (Grab Data Scientist)

Matrix Multiplication

What is a regression tree?
Decision trees used in data mining are of two main types: Classification tree analysis is when the predicted outcome is the class to which the data belongs.Regression tree analysis is when the predicted outcome can be considered a real number (e.g. the price of a house, or a patient's length of stay in a hospital).

XGBoost is an algorithm that has recently been dominating applied machine learning and Kaggle competitions for structured or tabular data. XGBoost is an implementation of gradient boosted decision trees designed for speed and performance.
Gradient boosting is a machine learning technique for regression and classification problems, which produces a prediction model in the form of an ensemble of weak prediction models, typically decision trees.
URL: http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/

How to deal with unbalanced dataset -> 1) Apply stratified sampling to maintain the distriubtion of the y_responses variable in the training and testing dataset. The ratio of class_label=0 and class_label=1 will be maintained. This contrasts with randomly selection of the dataset for training/testing, which is better. 2) Apply XGBoost and play with the model paramters (max_depth or num_of_estimators) tuning it to have a better performance. 3) Handle the imbalanced dataset by applying SMOTE (Upssampling vs. Downsampling). Downsampling is preferred as compared to Upssampling as it doesnt create duplicates of the records.

R2 is a statistic that will give some information about the goodness of fit of a model. In regression, the R2 coefficient of determination is a statistical measure of how well the regression line approximates the real data points. An R2 of 1 indicates that the regression line perfectly fits the data
A statistical method that explains how much of the variability of a factor can be caused or explained by its relationship to another factor. Coefficient of determination is used in trend analysis. It is computed as a value between 0 (0 percent) and 1 (100 percent)

Partial dependence plots
Y-axis values represent the model outcome in relation to the given independent variable, after considering the average effect of other independent variables in the model.
Partial dependence plot is plotting the independent variable x1 vs the model outcome y_bar, after considering the average effect of other independent variables in the model. Notice that partial dependence plot is NOT plotting relationship between independent variables and target variable.

K-Means clustering (no labels, unsupervised learning)

Similarity measures= Euclidean distance, Jaccard Coefficient, Cosine Similarity

Differences between K-Means(Based on distance to cluster) and DBSCAN (Based on frequencies using density instead of Distance to cluster) 

For text mining, need to perform vectorization to convert text to numeric vector form and then possible to do clustering based on the above. Another example is to cluster customers loyality based on several features.. Perform PCA to project these features into a 2D pane and do clustering.
