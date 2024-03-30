import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.feature_selection import VarianceThreshold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.decomposition import PCA
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from quart import jsonify

class PartOne:
    def __init__(self):
        self.file_name = r'/app/proj/Iris.csv'
        self.df = pd.read_csv(self.file_name)

    def run(self):
        items = []
        
        df = self.df
        df: DataFrame = pd.read_csv(self.file_name)

        
        label_encoder = LabelEncoder()
        df['Species_encoded'] = label_encoder.fit_transform(df['Species'])
        df.drop(['Id', 'Species'], axis=1, inplace=True)



        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        plt.figure(figsize=(7,4))
        sns.heatmap(df.corr(),annot=True,cmap='cubehelix_r')
        # plt.show()

        feature_Pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('poly', PolynomialFeatures(degree=2, include_bias=False)),
            ('pca', PCA(n_components=2)),
            ('linear', LinearDiscriminantAnalysis()),
            ('var_threshold', VarianceThreshold(threshold=0.1)),
        ])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=10)
        feature_Pipeline.fit(X_train, y_train)
        
        X_train_selected = feature_Pipeline.transform(X_train)
        X_test_selected = feature_Pipeline.transform(X_test)
        
        model = {
            'perceptron': Perceptron(max_iter=2000),
            'logistic_regression': LogisticRegression(max_iter=2000),
            'svm': SVC(max_iter=2000),
            'decision_tree': DecisionTreeClassifier(max_depth=15),
            'random_forest': RandomForestClassifier(max_depth=15, max_samples=0.6),
            'gradient_boosting': GradientBoostingClassifier(),
            'multilayer_perceptron': MLPClassifier(max_iter=2000),
            'knn': KNeighborsClassifier(), 
            # 'linear': LinearDiscriminantAnalysis(),
            # 'quadrtic': QuadraticDiscriminantAnalysis(),
        }

        model_copy = model.copy()
        
        print("Datasets with feature selection:")
        flag = 1
        for idx, (name, model) in enumerate(model.items()):
            model_pipeline = Pipeline([
                ('model', model)
            ])
            model_pipeline.fit(X_train, y_train)
            score = model_pipeline.score(X_test, y_test)
            items.append({'name': name, 'value': str(score), 'flag': flag})
            flag = 0  

        print("---------------------------------------------------")
        print("Datasets without feature selection:")
        first_loop = True
        for name, model in model_copy.items():
            if first_loop:
                flag = 2
                first_loop = False
            else:
                flag = 0
            model.fit(X_train, y_train)
            score = model.score(X_test, y_test)
            items.append({'name': name, 'value': str(score), 'flag': flag})
            print(f"{name} score: {score}")

        param_grid = {
            'C': [0.01, 0.1, 1, 10],
            'gamma': [0.01, 0.1, 1],
            'kernel': ['linear', 'rbf'],

        }
        print("---------------------------------------------------")
        grid_search = GridSearchCV(SVC(), param_grid, cv=5, n_jobs=-1)
        grid_search.fit(X_train_selected, y_train)

        best_params = grid_search.best_params_
        print(best_params)
        items.append({'name':'best params','value':str(best_params)})
        return jsonify(items)

