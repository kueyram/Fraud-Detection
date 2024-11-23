#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# loading the testing dataset
test_data = pd.read_csv('./data/fraudTest.csv', sep=',')

# Feature Engineering
test_data['trans_date_trans_time'] = pd.to_datetime(test_data['trans_date_trans_time'])
test_data['hour'] = test_data['trans_date_trans_time'].dt.hour
test_data['day'] = test_data['trans_date_trans_time'].dt.day
test_data['month'] = test_data['trans_date_trans_time'].dt.month
test_data['year'] = test_data['trans_date_trans_time'].dt.year

# Dropping unnecessary columns
columns_to_drop = ['Unnamed: 0','trans_date_trans_time', 'cc_num', 'first', 'last', 'street', 
                   'city', 'zip', 'trans_num', 'dob', 'unix_time']
test_data = test_data.drop(columns=columns_to_drop, axis=1)


# In[ ]:


# Loading the label_encoders dictionary
with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

# Label Encoding

for col in categorical_columns:
    label_encoder = label_encoders[col]
    test_data[col] = label_encoder.transform(test_data[col])

# Scaling
scaled_test_data = scaler.transform(test_data)

# Making predictions on the test data
new_predictions = model.predict(scaled_test_data)

# let's add the  predictions to the test data
test_data['is_fraud_prediction'] = new_predictions

# Display results
print("\nNew Data Predictions:")
print(new_data[['is_fraud_prediction']])


# In[ ]:


# Save predictions to a CSV
ntest_data.to_csv("predicted_results.csv", index=False)
print("\nPredictions saved to 'predicted_results.csv'")

