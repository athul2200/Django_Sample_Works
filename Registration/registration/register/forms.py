from django import forms

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        name=self.cleaned_data['name']
        if name=="":
            raise forms.ValidationError("Name Cannot be Empty")
        return name
    
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("Password must be atleast 8 characters")
        return password
    

