# from django.forms import ModelForm
from django import forms
from django.forms import ModelForm
# from .models import AbcModel
from .models import Student, EducationProgram, ManagementMember, FellowStudent

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class EducationProgramForm(forms.ModelForm):
    class Meta:
        model = EducationProgram
        fields = '__all__'

class ManagementMemberForm(forms.ModelForm):
    class Meta:
        model = ManagementMember
        fields = '__all__'

class FellowStudentForm(forms.ModelForm):
    class Meta:
        model = FellowStudent
        fields = '__all__'












        
# class AbcForm(forms.Form):
#     task = forms.CharField(initial = "Равна ли С сумме A и B ?")
#     a = forms.IntegerField(initial=1, min_value=0)
#     b = forms.IntegerField(initial=1,required=False)
#     c = forms.IntegerField(initial=1, label="c_lable")


# class AbcModelForm(ModelForm):
#     # task = forms.CharField(widget=forms.Textarea({'cols': '60', 'rows': "3"}))
#     # task.widget.attrs.update({'cols': '40', 'rows': "2"})
#     class Meta:
#         model = AbcModel
#         fields = '__all__'
#         # fields = ['task', 'a', 'b','c']
#         print('\nfields: ', fields)
