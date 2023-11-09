from django import forms
class StudentForm(forms.Form):
    Name=forms.CharField(max_length=50)
    Roll_No=forms.IntegerField()
    percentage=forms.IntegerField()
    