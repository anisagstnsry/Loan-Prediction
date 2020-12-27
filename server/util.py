import pickle
import json
import numpy as np
import os

__data_columns = None
__model = None

def get_loan(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
    try:
        gender = "Gender_{}".format(Gender)
        loc_index1 = __data_columns.index(gender.lower())
    except:
        loc_index1 = -1
    try:
        married = "Married_{}".format(Married)
        loc_index2 = __data_columns.index(married.lower())
    except:
        loc_index2 = -1
    try:
        education = "Education_{}".format(Education)
        loc_index3 = __data_columns.index(education.lower())
    except:
        loc_index3 = -1
    try:
        self_employed = "Self_Employed_{}".format(Self_Employed)
        loc_index4 = __data_columns.index(self_employed.lower())
    except:
        loc_index4 = -1
    try:
        property_area = "Property_Area_{}".format(Property_Area)
        loc_index5 = __data_columns.index(property_area.lower())
    except:
        loc_index5 = -1
        
    x = np.zeros(len(__data_columns))
    x[0] = Dependents
    x[1] = ApplicantIncome
    x[2] = CoapplicantIncome
    x[3] = LoanAmount
    x[4] = Loan_Amount_Term
    x[5] = Credit_History
    if loc_index1>=0:
        x[loc_index1] = 1
    if loc_index2>=0:
        x[loc_index2] = 1
    if loc_index3>=0:
        x[loc_index3] = 1
    if loc_index4>=0:
        x[loc_index4] = 1
    if loc_index5>=0:
        x[loc_index5] = 1
        
    result = __model.predict([x])
    if result == 0:
        return "Rejected"
    elif result == 1:
        return "Approved"


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns

    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artifacts"),

    with open(artifacts[0]+"/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open(artifacts[0]+"/pickle_loan_model.pkl", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_data_columns():
    return __data_columns

load_saved_artifacts()