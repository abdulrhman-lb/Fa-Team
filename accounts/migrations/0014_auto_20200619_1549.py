# Generated by Django 3.0.7 on 2020-06-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200619_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blood_type',
            field=models.CharField(choices=[('A-', 'A-'), ('AB+', 'AB+'), ('O-', 'O-'), ('B-', 'B-'), ('B+', 'B+'), ('A+', 'A+'), ('AB-', 'AB-'), ('O+', 'O+')], max_length=50, verbose_name='زمرة الدم'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('شهادة إعدادية', 'شهادة إعدادية'), ('معهد', 'معهد'), ('غير متعلم', 'غير متعلم'), ('دبلوم', 'دبلوم'), ('ماجستير', 'ماجستير'), ('طالب جامعي', 'طالب جامعي'), ('شهادة ثانوية', 'شهادة ثانوية'), ('شهادة جامعية', 'شهادة جامعية'), ('دكتوراه', 'دكتوراه'), ('شهادة ابتدائية', 'شهادة ابتدائية')], max_length=50, verbose_name='الشهادة العلمية '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education_detail',
            field=models.TextField(blank=True, null=True, verbose_name='تفاصيل التحصيل العلمي'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='employment_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ التوظيف'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, choices=[('مستخدم', 'مستخدم'), ('منسق التدريب', 'منسق التدريب'), ('مساعد منسق الإسعاف', 'مساعد منسق الإسعاف'), ('منسق فريق الإسعاف', 'منسق فريق الإسعاف'), ('مسؤول مركز', 'مسؤول مركز'), ('مستشار طبي', 'مستشار طبي'), ('سائق', 'سائق'), ('منسق عمليات الإسعاف', 'منسق عمليات الإسعاف'), ('لوجستي إسعاف', 'لوجستي إسعاف')], max_length=50, null=True, verbose_name='المنصب'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position_e',
            field=models.CharField(blank=True, choices=[('Ambulance Team Coordinator', 'Ambulance Team Coordinator'), ('Assistant Ambulance Coordinator', 'Assistant Ambulance Coordinator'), ('Training Coordinator', 'Training Coordinator'), ('Center Official', 'Center Official'), ('Driver', 'Driver'), ('Ambulance Logistic', 'Ambulance Logistic'), ('user', 'user'), ('Medical Advisor', 'Medical Advisor'), ('Ambulance Operations Coordinator', 'Ambulance Operations Coordinator')], max_length=50, null=True, verbose_name='المنصب بالانكليزي'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank_in_team',
            field=models.CharField(choices=[('مسعف تحت التدريب', 'مسعف تحت التدريب'), ('مسعف', 'مسعف'), ('كشاف', 'كشاف'), ('قائد قطاع تحت التدريب', 'قائد قطاع تحت التدريب'), ('قائد قطاع', 'قائد قطاع'), ('قائد فريق', 'قائد فريق')], max_length=50, verbose_name='الرتبة ضمن الفريق'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shoulder_size',
            field=models.CharField(choices=[('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('XXL', 'XXL'), ('S', 'S')], max_length=50, verbose_name='قياس الكتفين'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_status',
            field=models.CharField(choices=[('أعزب', 'أعزب'), ('متزوج', 'متزوج')], max_length=50, verbose_name='الحالة الاجتماعية'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_branch',
            field=models.CharField(choices=[('شعبة السقيلبية', 'شعبة السقيلبية'), ('شعبة مصياف', 'شعبة مصياف'), ('شعبة السلمية', 'شعبة السلمية'), ('فرع حماة', 'فرع حماة')], max_length=50, verbose_name='الشعبة'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tot_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ دورة تي او تي'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='training_postion',
            field=models.CharField(blank=True, choices=[('مدرب', 'مدرب'), ('مساعد مدرب', 'مساعد مدرب')], max_length=50, null=True, verbose_name='الصفة بالتدريب'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_person',
            field=models.CharField(choices=[('أنثى', 'أنثى'), ('ذكر', 'ذكر')], max_length=50, verbose_name='  الجنس'),
        ),
    ]
