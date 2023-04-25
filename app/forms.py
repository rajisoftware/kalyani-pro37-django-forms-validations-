from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[['PYTHON','python'],('SQL','sql'),['JAVA','java']]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateTimeField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #Course=forms.MultipleChoiceField(choices=c)
    Course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
