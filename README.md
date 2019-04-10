# Breast Cancer Wisconsin (Diagnostic) Prediction
*Predict whether the cancer is benign or malignant*

[![Status](https://img.shields.io/badge/status-maintained-brightgreen.svg?style=for-the-badge)]()
[![npm](https://img.shields.io/npm/l/express.svg?style=for-the-badge)]()


Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. n the 3-dimensional space is that described in: [K. P. Bennett and O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34].

This database is also available through the UW CS ftp server: ftp ftp.cs.wisc.edu cd math-prog/cpo-dataset/machine-learn/WDBC/

Also can be found on UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

**Attribute Information:**

*1) ID number 2) Diagnosis (M = malignant, B = benign) 3-32)*

<img src="text.png">

# Observation
<html>
<body>
    <br>
    <b>Here are the results of our Five Algorithm observation</b> 
<table>
  <tr>
    <th>Model</th>
    <th>Algorithm</th>
    <th>Test Accuracy</th>
  </tr>
  <tr>
    <td>Model 1</td>
    <td>Random Forest Algorithm</td>
    <td>95%</td>
  </tr>
  <tr>
    <td>Model 2</td>
    <td>SupportVector Machine Algorithm (SVM)</td>
    <td>90%</td>
  </tr>
  <tr>
    <td>Model 3</td>
    <td>Decision Tree Classifier Algorithm</td>
    <td>92%</td>
  </tr>
      <tr>
    <td>Model 4</td>
    <td>K-Nearest NeighborsClassifier Algorithm</td>
    <td>94.7%</td>
  </tr>
      <tr>
    <td>Model 5</td>
    <td>GaussianNB Algorithm</td>
    <td>93.8%</td>
  </tr>
</table>
</body>
</html>
