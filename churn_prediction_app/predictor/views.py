from django.shortcuts import render
from django.http import HttpResponse
from .forms import PredictionForm
import joblib
import pandas as pd 
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_model_and_scaler():
    with open('../saved_model.pkl', 'rb') as model_file:
        loaded_model, scaler = pickle.load(model_file)
    return loaded_model, scaler

def predict_churn(age, gender, tenure, support_calls, payment_delay, subscription_type, contract_length):
    loaded_model, scaler = load_model_and_scaler()

    input_data = [[age, gender, tenure, support_calls, payment_delay, subscription_type, contract_length]]
    # scaled_input = scaler.fit_transform(input_data)
    prediction = loaded_model.predict(input_data)
    
    return prediction[0]

def home(request):
    return HttpResponse("<h1>It's worked</h1>")
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get user input from the form
            age = form.cleaned_data['Age']
            gender = form.cleaned_data['Gender']
            tenure = form.cleaned_data['Tenure']
            support_calls = form.cleaned_data['Support_Calls']
            payment_delay = form.cleaned_data['Payment_Delay']
            subscription_type = form.cleaned_data['Subscription_Type']
            contract_length = form.cleaned_data['Contract_Length']
            # churn = form.cleaned_data['Churn']
            
            # Load the saved model using pickle
            # loaded_model = load_model_and_scaler()
            
            # Encoding for Gender and Subscription Type
          
            # gender_encoded = gender.factorize()[0]
            # subscription_encoded = subscription_type.factorize()[0]
            # contract_length_encoded = contract_length.factorize()[0]


            # Encoding for Gender and Subscription Type
            encoder = LabelEncoder()
            # subscription_encoder = LabelEncoder()
            gender_encoded = encoder.fit_transform([gender])[0]
            subscription_encoded = encoder.fit_transform([subscription_type])[0]
            contract_length_encoded = encoder.fit_transform([contract_length])[0]

            prediction = predict_churn(age, gender_encoded, tenure, support_calls, payment_delay, subscription_encoded, contract_length_encoded)
            
        

            if prediction == 0:
                prediction = 'Will not Churn'
            else:
                prediction = "Will Churn"

            print(prediction)
            context = {'form': form, 'prediction': prediction}
            return render(request, 'predictor/home.html', context)
    else:
        form = PredictionForm()
    
    context = {'form': form}
    return render(request, 'predictor/home.html', context)
    
    