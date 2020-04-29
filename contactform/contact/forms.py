from django  import forms
from .models import Contact
from django.forms import ModelForm 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","subject","password","message"]

def clean(self): 
  
        # data from the form is fetched using super function 
        super(ContactForm, self).clean() 
          
        # extract the username and text field from the data 
        name = self.cleaned_data.get('name') 
        email = self.cleaned_data.get('emil') 
        subject = self.cleaned_data.get('subject') 
        password = self.cleaned_data.get('password') 
        message = self.cleaned_data.get('message') 
        # text = self.cleaned_data.get('text') 
  
        # conditions to be met for the username length 
        if len(name) == 'null': 
            self._errors['name'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(password) <8: 
            self._errors['password'] = self.error_class([ 
                'Post Should Contain minimum 8 characters']) 
        if len(email) == 'null': 
            self._errors['email'] = self.error_class([ 
                'Minimum  characters required']) 
        if len(message) =='null': 
            self._errors['message'] = self.error_class([ 
                'Post Should Contain minimum 8 characters']) 
  
        # return any errors if found 
        return self.cleaned_data 

        