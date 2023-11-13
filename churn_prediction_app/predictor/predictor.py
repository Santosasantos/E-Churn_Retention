# predictor/predictor.py
import pickle

def load_model_and_scaler():
    with open('path_to_saved_model.pkl', 'rb') as model_file:
        loaded_model,  scaler = pickle.load(model_file)
    return loaded_model, scaler


def predict_churn(age, gender, tenure, support_calls, payment_delay, subscription_type, contract_length):
    loaded_model, scaler = load_model_and_scaler()

    input_data = [[age, gender, tenure, support_calls, payment_delay, subscription_type, contract_length]]
    scaled_input = scaler.transform(input_data)  # Scale input data using the scaler
    prediction = loaded_model.predict(scaled_input)
    
    return prediction[0]
