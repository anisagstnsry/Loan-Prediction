function getGenderValue() {
  var uiGender = document.getElementsByName("uiGender");
  for (var i in uiGender) {
    if (uiGender[i].checked) {
      return uiGender[i].val();
    }
  }
  return -1; // Invalid Value
}

function getMarriedValue() {
  var uiMarried = document.getElementsByName("uiMarried");
  for (var i in uiMarried) {
    if (uiMarried[i].checked) {
      return uiMarried[1].val();
    }
  }
  return -1; // Invalid Value
}

function getDependentsValue() {
  var uiDependents = document.getElementsByName("uiDependents");
  for (var i in uiDependents) {
    if (uiDependents[i].checked) {
      return uiDependents[i].val();
    }
  }
  return -1; // Invalid Value
}

function getEducationValue() {
  var uiEducation = document.getElementsByName("uiEducation");
  for (var i in uiEducation) {
    if (uiEducation[i].checked) {
      return uiEducation[i].val();
    }
  }
  return -1; // Invalid Value
}

function getEmployedValue() {
  var uiEmployed = document.getElementsByName("uiEmployed");
  for (var i in uiEmployed) {
    if (uiEmployed[i].checked) {
      return uiEmployed[i].val();
    }
  }
  return -1; // Invalid Value
}

function getHistoryValue() {
  var uiHistory = document.getElementsByName("uiHistory");
  for (var i in uiHistory) {
    if (uiHistory[i].checked) {
      return uiHistory[i].val();
    }
  }
  return -1; // Invalid Value
}

function getPropertyValue() {
  var uiProperty = document.getElementsByName("uiProperty");
  for (var i in uiProperty) {
    if (uiProperty[i].checked) {
      return uiProperty[i].val();
    }
  }
  return -1; // Invalid Value
}

function onClickedLoanPrediction() {
  console.log("Loan prediction button clicked");
  var Gender = getGenderValue();
  var Married = getMarriedValue();
  var Dependents = getDependentsValue();
  var Education = getEducationValue();
  var Self_Employed = getEmployedValue();
  var ApplicantIncome = document.getElementById("income1");
  var CoapplicantIncome = document.getElementById("income2");
  var LoanAmount = document.getElementById("loanamount");
  var Loan_Amount_Term = document.getElementById("loanterm");
  var Credit_History = getHistoryvalue();
  var Property_Area = getPropertyValue();
  var estLoan = document.getElementById("uiPredictedLoan");
  var url = "/predict_loan"; 

  $.post(
    url,
    {
      Gender: Gender,
      Married: Married,
      Dependents: Dependents,
      Education: Education,
      Self_Employed: Self_Employed,
      ApplicantIncome: parseInt(ApplicantIncome.value),
      CoapplicantIncome: parseFloat(CoapplicantIncome.value),
      LoanAmount: parseFloat(LoanAmount.value),
      Loan_Amount_Term: parseFloat(Loan_Amount_Term.value),
      Credit_History: Credit_History,
      Property_Area: Property_Area,
    },
    function (data, status) {
      console.log(data.predicted_loan);
      estLoan.innerHTML =
        "<h2>" + data.predicted_loan + "</h2>";
      console.log(status);
    }
  );
}