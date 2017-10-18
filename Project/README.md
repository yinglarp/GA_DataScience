# GA_DataScience
General Assembly Data Science Course - Project Idea

The dataset is sourced from https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients

The idea is to apply classification techniques to the dataset and see if it's possible to identify features that will have a high probability of predicting credit card default. Current idea is to try using decision tree techniques and cross validate the model using logistics regression. Not much work at the moment, still exploratory stage.


Objective: Is to classifiy clients into 2 groups (High Risk of Default/Low Risk of Default) using XGBoost classifier.

1) Load dataset and display dataset info (X rows, Y attributes)
2) Perform preprocessing/transformations on datasets  - Xgboost manages only numeric vectors. Hence non-numeric data types attributes should be converted to numerical values.
3) Create the input features (X) and target variable (y)
4) Split the dataset into training data and test data 
5) Fit/Train the XGBoost model on the training dataset
6) Using theBuilt-in XGBoost Feature Importance Plot to come out with Feature Importance Ranking/Scores
7) Make predictions for test data and evaluate model (accuracy,precision,recall) - https://stats.stackexchange.com/questions/179977/scikit-predict-proba-output-interpretation
8) Fit model using each importance scores as a threshold by using XGBoost Feature Importance Scores for feature selection to determine model performance on accuracy vs. no. of features - https://stats.stackexchange.com/questions/158136/identifying-filtered-features-after-feature-selection-with-scikit-learn
9) Plot the partial dependency graphs for each features
10) Plot the XGBoost Trees




