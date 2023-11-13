from django import forms

class PredictionForm(forms.Form):
    Age = forms.IntegerField(label='Age')
    Gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label='Gender')
    Tenure = forms.IntegerField(label='Tenure')
    
    Support_Calls = forms.IntegerField(label='Support Calls')
    Payment_Delay = forms.IntegerField(label='Payment Delay')
    Subscription_Type = forms.ChoiceField(choices=[('basic', 'Basic'), ('premium', 'Premium')], label='Subscription Type')
    Contract_Length = forms.ChoiceField(choices=[('monthly', 'Monthly'), ('annually', 'Annually'), ('quarterly', 'Quarterly')], label='Contract Length')
   