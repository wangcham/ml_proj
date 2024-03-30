<template>
 <div class="container">
        <h1>Report</h1>
        <p><strong>Date:</strong> March 2024</p>
        <h2>Part 1 Result</h2>
        <img class="image" src="../assets/image1.jpg" alt="Heat Map Analysis">
        <p>
            On the RFID data set, by comparing the performance of feature selection and non-feature selection algorithms, we found that logistic regression performed well in both cases, with an accuracy of 0.9833333333333333. This shows that logistic regression has significant classification accuracy on this dataset and is able to effectively distinguish different categories of data.
        </p>

        <h2>Part 2 Result</h2>
        <img class="image" src="../assets/image2.png" alt="Custom Multilayer Perceptron">
        <p>
            According to the heat map analysis results, we can observe that petal length (PetalLengthCm) and petal width (PetalWidthCm) have a high correlation with the target variable "Species_encoded", with correlation coefficients of 0.96 and 0.95 respectively, which indicates that these two features are useful in distinguishing different species of daffodils (Iris) and play a key role.
        </p>
        <img class="image" src="../assets/image3.png" alt="heat map">
        <p>
            By comparing the scores of algorithms that use feature selection or not, we can observe that feature selection can significantly improve the performance of some algorithms. For example, the score of random forest (random_forest) increased from 0.95 to 0.9666666666666667 after using feature selection, while the score of gradient boosting (gradient_boosting) did not change due to feature selection.
        </p>
        
        <p>
            Based on the running results of the given custom multilayer perceptron (multilayer_perceptron), we can see the prediction results and accuracy obtained after training. The accuracy is 0.7111111111111111. Compared to the multi-layer perceptron version in Scikit-Learn, the performance of this custom version of the multi-layer perceptron on the RFID data set has declined.
        </p>
    </div>
  </template>
  
<style>
.container {
            display: flex;
            flex-direction: column;
            max-width: 800px;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
        }
        .image {
            max-width: 100%;
            height: auto;
            margin-top: 20px;
        }

</style>