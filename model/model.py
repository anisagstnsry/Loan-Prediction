import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.preprocessing import OneHotEncoder

#ignoring all warnings
import warnings
warnings.filterwarnings('ignore')

training_data  = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_train.csv" )
test_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_test.csv')
test_data.head()

#fill missing value
training_data = training_data.fillna(method="ffill")
test_data = test_data.fillna(method="ffill")
training_data

data_Y = training_data["Loan_Status"]
data_X = training_data.drop(columns = ["Unnamed: 0", "Loan_ID", "Loan_Status"])
test_data = test_data.drop(columns = ["Loan_ID"])

#Replace
data_X['Dependents'] = data_X['Dependents'].replace("3+", 3)
test_data['Dependents'] = test_data['Dependents'].replace("3+", 3)

#OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore')
training_data_dummy = pd.DataFrame(enc.fit_transform(data_X.loc[:, ["Gender", "Married", "Education", "Self_Employed","Property_Area"]]).toarray())
training_data_dummy.columns = enc.get_feature_names(["Gender", "Married", "Education", "Self_Employed","Property_Area"])
test_data_dummy = pd.DataFrame(enc.transform(test_data.loc[:, ["Gender", "Married", "Education", "Self_Employed","Property_Area"]]).toarray())
test_data_dummy.columns = enc.get_feature_names(["Gender", "Married", "Education", "Self_Employed","Property_Area"])
training_data_num = data_X.loc[:, ["Dependents", "ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]]
test_data_num = test_data.loc[:, ["Dependents", "ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]]
training_data = training_data_num.join(training_data_dummy)
test_data = test_data_num.join(test_data_dummy)

#Split Training and Test Data
X_train, X_test, Y_train, Y_test = train_test_split(training_data, data_Y, test_size = 0.2, random_state = 0)
print(X_train.shape, X_test.shape)
X_train.head()

#Logistic Regression
clf = LogisticRegression(random_state=0, solver = 'liblinear', penalty = 'l2')
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
#confusion matrix
print("confusion matrix:") 
print(confusion_matrix(Y_test, Y_pred))

#classification report
print("classification report:")
report = classification_report(Y_test, Y_pred, output_dict = True)
print(classification_report(Y_test, Y_pred))

# Calculating the F1 Score by comparing the actual and predicted values
f_score = f1_score(Y_test ,Y_pred)
print("f1 score test", f_score)

predictions = clf.predict(test_data)
res = pd.DataFrame(predictions) #predictions are nothing but the final predictions of your model on input features of your new unseen test data
res.index = test_data.index # its important for comparison. Here "test_new" is your new test dataset
res.columns = ["prediction"]

import pickle
pkl_filename = "pickle_loan_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(clf, file)
    
import json
columns = {
    'data_columns' : [col.lower() for col in training_data.columns]
}
with open("columns.json","w") as f:
    f.write(json.dumps(columns))

