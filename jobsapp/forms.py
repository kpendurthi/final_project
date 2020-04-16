from django import forms
from .models import Employer, Job

class EmployerForm(forms.ModelForm):

    class Meta:
        model = Employer
        fields = ('Company_Name','Company_Address','Email',)

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('employer','title', 'description','location','type','category','last_date','company_name','company_description','website','image_url', 'created_at','filled', 'salary',)

 

