# Credit Card Fraud Detection

📖 This project uses machine learning to detect fraudulent credit card transactions. The model is trained using a dataset of credit card transactions, and the goal is to classify each transaction as either fraudulent or non-fraudulent. The project also includes data preprocessing, feature scaling, and evaluation metrics to assess model performance.

---

## 🗂️Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

---

## Overview

This project uses machine learning to identify fraudulent credit card transactions. The dataset includes information about transactions, such as the merchant, transaction time, and customer details.

We first prepare the data by converting categories into numbers, filling any missing values, and scaling the numerical features. Then, we train a Logistic Regression model to predict if a transaction is fraudulent or not.

---

## Requirements


Python 3.x
pandas - for handling data
scikit-learn - for machine learning
matplotlib - for visualization
seaborn - for creating visualizations
pickle - for saving models and encoders

To install the required libraries, you can use the following command:

```bash
pip install pandas scikit-learn matplotlib seaborn pickle-mixin
```

---

## 🛠️Setup

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
```

2. Navigate into the project directory

```bash
cd credit-card-fraud-detection
```

3. Once you've set up the project and installed the requirements, you can train the model and evaluate its performance by running:

```bash
python fraud_detection.py
```

---

## Usage

This project includes a script to preprocess the dataset, train the machine learning model, and evaluate its performance. Here's a breakdown of what the script does:

    Data Preprocessing:
        Handles missing values and unnecessary columns.
        Encodes categorical features using Label Encoding.
        Scales numerical features using StandardScaler.

    Model Training:
        Trains a Logistic Regression model to classify transactions as fraudulent or non-fraudulent.

    Model Evaluation:
        Evaluates model performance using accuracy, confusion matrix, and classification report.

    Visualization:
        Visualizes the distribution of fraudulent vs. non-fraudulent transactions, as well as the correlation heatmap of features.
---

## 📜 License

This project is licensed under the MIT License. See the LICENSE tab on the top for more details.

---