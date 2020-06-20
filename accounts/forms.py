from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.ModelForm):
    username = forms.CharField(label="اسم المستخدم :")
    password = forms.CharField(label="كلمة المرور :" , widget=forms.PasswordInput())
    class Meta:
        model = User  
        fields = ("username", "password")


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label = "الاسم الأول :")
    last_name = forms.CharField(label = "الاسم الأخير :")
    email = forms.EmailField(label = "البريد الالكتروني :")
    class Meta():
        model = User
        fields = ('email',)


class UpdateProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ('branchs','sub_branch' , 'point' , 'nation_num' , 'name' , 'father_name' , 'mother_name' ,
        'type_of_person' , 'birth_place' , 'birth_date' , 'social_status' , 'mobile' , 'phone' , 'education' , 'education_detail' , 
        'sarc_adjective' , 'position' , 'volunteer_date' , 'employment_date' , 'blood_type' , 'name_e' , 'position_e' , 'shoce_size' , 
        'waist_size' , 'shoulder_size' , 'rank_in_team' , 'advanced_date' , 'training_postion' , 'tot_date' , 'center' , 'image' )

