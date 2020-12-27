from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")

@app.route('/predict_loan', methods=['POST'])
def predict_loan():
    Dependents = int(request.form['Dependents'])
    ApplicantIncome = int(request.form['ApplicantIncome'])
    CoapplicantIncome = float(request.form['CoapplicantIncome'])
    LoanAmount = float(request.form['LoanAmount'])
    Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
    Credit_History = float(request.form['Credit_History'])
    Gender = request.form['Gender']
    Married = request.form['Married']
    Education = request.form['Education']
    Self_Employed = request.form['Self_Employed']
    Property_Area = request.form['Property_Area']

    response = jsonify({
        'predicted_loan': util.get_loan(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print("predict successfully")

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Loan Prediction...")
    app.run(debug=True)