from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    SUB = {
        ("فرع حماة" , "فرع حماة"),
        ("شعبة السلمية" , "شعبة السلمية"),
        ("شعبة السقيلبية" , "شعبة السقيلبية"),
        ("شعبة مصياف" , "شعبة مصياف"),
    }

    SEX = {
        ("ذكر" , "ذكر"),
        ("أنثى" , "أنثى"),
    }

    SOC = {
        ("أعزب" , "أعزب"),
        ("متزوج" , "متزوج"),
    }

    EDU = {
        ("غير متعلم" , "غير متعلم"),
        ("شهادة ابتدائية" , "شهادة ابتدائية"),
        ("شهادة إعدادية" , "شهادة إعدادية"),
        ("شهادة ثانوية" , "شهادة ثانوية"),
        ("طالب جامعي" , "طالب جامعي"),
        ("معهد" , "معهد"),
        ("شهادة جامعية" , "شهادة جامعية"),
        ("دبلوم" , "دبلوم"),
        ("ماجستير" , "ماجستير"),
        ("دكتوراه" , "دكتوراه"),
    }

    ADJ = {
        ("متطوع" , "متطوع"),
        ("موظف" , "موظف"),
    }

    POS = {
        ("منسق فريق الإسعاف" , "منسق فريق الإسعاف"),
        ("مساعد منسق الإسعاف" , "مساعد منسق الإسعاف"),
        ("منسق عمليات الإسعاف" , "منسق عمليات الإسعاف"),
        ("منسق التدريب" , "منسق التدريب"),
        ("مستشار طبي" , "مستشار طبي"),
        ("لوجستي إسعاف" , "لوجستي إسعاف"),
        ("مسؤول مركز" , "مسؤول مركز"),
        ("سائق" , "سائق"),
        ("مستخدم" , "مستخدم"),
    }

    POS_E = {
        ("Ambulance Team Coordinator" , "Ambulance Team Coordinator"),
        ("Assistant Ambulance Coordinator" , "Assistant Ambulance Coordinator"),
        ("Ambulance Operations Coordinator" , "Ambulance Operations Coordinator"),
        ("Training Coordinator" , "Training Coordinator"),
        ("Medical Advisor" , "Medical Advisor"),
        ("Ambulance Logistic" , "Ambulance Logistic"),
        ("Center Official" , "Center Official"),
        ("Driver" , "Driver"),
        ("user" , "user"),
    }

    BLOOD = {
        ("A+" , "A+"),
        ("A-" , "A-"),
        ("B+" , "B+"),
        ("B-" , "B-"),
        ("AB+" , "AB+"),
        ("AB-" , "AB-"),
        ("O+" , "O+"),
        ("O-" , "O-"),
    }

    SHOOULDER = {
        ("S" , "S"),
        ("M" , "M"),
        ("L" , "L"),
        ("XL" , "XL"),
        ("XXL" , "XXL"),
    }

    RANK = {
        ("قائد قطاع" , "قائد قطاع"),
        ("قائد قطاع تحت التدريب" , "قائد قطاع تحت التدريب"),
        ("قائد فريق" , "قائد فريق"),
        ("كشاف" , "كشاف"),
        ("مسعف" , "مسعف"),
        ("مسعف تحت التدريب" , "مسعف تحت التدريب"),
    }

    TRAINING = {
        ("مدرب" , "مدرب"),
        ("مساعد مدرب" , "مساعد مدرب"),
    }

    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    sub_branch      = models.CharField(_("الشعبة"), max_length=50 , choices=SUB)
    point           = models.CharField(_("النقطة"), max_length=50 , blank=True , null=True)
    nation_num      = models.IntegerField(_("الرقم الوطني") , validators=[MinValueValidator(10000000000),MaxValueValidator(99999999999)])
    name            = models.CharField(_("الاسم"), max_length=100)
    father_name     = models.CharField(_("اسم الأب"), max_length=50)
    mother_name     = models.CharField(_("اسم الأم"), max_length=50)
    type_of_person  = models.CharField(_("  الجنس"), max_length=50 , choices=SEX)
    birth_place     = models.CharField(_("مكان الولادة"), max_length=50)
    brith_date      = models.DateField(_("تاريخ الولادة"))
    social_status   = models.CharField(_("الحالة الاجتماعية"), max_length=50 , choices=SOC)
    mobile          = models.IntegerField(_("جوال") , validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])
    phone           = models.IntegerField(_("الهاتف") , validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    education       = models.CharField(_("الشهادة العلمية "), max_length=50 , choices=EDU)
    education_detail= models.TextField(_("تفاصيل التحيل العلمي"))
    sarc_adjective  = models.CharField(_("الصفة الهلالية"), max_length=50 , choices=ADJ)
    position        = models.CharField(_("المنصب"), max_length=50 , choices=POS)
    volunteer_date  = models.DateField(_("تاريخ التطوع"))
    employment_date = models.DateField(_("تاريخ التوظيف"))
    blood_type      = models.CharField(_("زمرة الدم"), max_length=50 , choices=BLOOD)
    name_e          = models.CharField(_("الاسم بالانكليزي"), max_length=50)
    position_e      = models.CharField(_("المنصب بالانكليزي"), max_length=50 , choices=POS_E)
    shoce_size      = models.IntegerField(_("قياس الحذاء"))
    waist_size      = models.IntegerField(_("قياس الخصر"))
    shoulder_size   = models.CharField(_("قياس الكتفين"), max_length=50 , choices=SHOOULDER)
    rank_in_team    = models.CharField(_("الرتبة ضمن الفريق"), max_length=50 , choices=RANK)
    advanced_date   = models.DateField(_("تاريخ دورة المتقدم"))
    training_postion= models.CharField(_("الصفة بالتدريب"), max_length=50 , choices=TRAINING)
    tot_date        = models.DateField(_("تاريخ دورة تي او تي"))


    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name



