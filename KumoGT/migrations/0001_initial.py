# Generated by Django 2.2.6 on 2019-11-14 00:09

import KumoGT.crypt_fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deg_type', models.CharField(choices=[('phd', 'PhDCS'), ('ms', 'MSCS'), ('meng', 'MEngCS')], default='none', max_length=255)),
                ('first_reg_year', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(-32768)], verbose_name='First Registered Year')),
                ('first_reg_sem', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer')], default='fall', max_length=255, verbose_name='First Registered Semester')),
                ('last_reg_year', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(-32768)], verbose_name='Last Registered Year')),
                ('last_reg_sem', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer')], default='fall', max_length=255, verbose_name='Last Registered Semester')),
                ('deg_recv_year', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(-32768)], verbose_name='Degree Received Year')),
                ('deg_recv_sem', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer')], default='fall', max_length=255, verbose_name='Degree Received Semester')),
            ],
        ),
        migrations.CreateModel(
            name='T_D_Prop_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not sel', 'Not Selected'), ('title page', 'Thesis/Dissertation Proposal Title Page'), ('prop', 'Thesis/Dissertation Proposal')], default='not sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='T_D_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField()),
                ('degree', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='T_D_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not sel', 'Not Selected'), ('approval', 'Thesis/Dissertation Approval Page'), ('t_d', 'Thesis/Dissertation')], default='not sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('uin', models.CharField(max_length=255, unique=True, verbose_name='UIN')),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('not sel', 'Not Selected'), ('male', 'Male'), ('female', 'Female')], default='not sel', max_length=255)),
                ('cur_degree', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='KumoGT.Degree', verbose_name='Current Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Pre_Exam_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Prelim Date')),
                ('result', models.CharField(choices=[('none', '----'), ('pass', 'Pass'), ('fail', 'Fail')], default='none', max_length=255)),
                ('degree', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Pre_Exam_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not sel', 'Not Selected'), ('checklist', 'Preliminary Exam Checklist'), ('report', 'Preliminary Exam Report'), ('written', 'Preliminary Exam Written')], default='not sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fin_Exam_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('result', models.CharField(choices=[('none', '----'), ('pass', 'Pass'), ('fail', 'Fail')], default='none', max_length=255)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('room', models.CharField(blank=True, max_length=255)),
                ('abstract', models.CharField(blank=True, max_length=1023)),
                ('degree', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Exam_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not sel', 'Not Selected'), ('request', 'Request for Final Examination'), ('req for exemp', 'Request for exemption from Final Examination'), ('report', 'Report of Final Exam')], default='not sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='degree',
            name='stu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student', verbose_name='Student'),
        ),
        migrations.CreateModel(
            name='Deg_Plan_Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', KumoGT.crypt_fields.EncryptedFileField(upload_to='documents/', verbose_name='Document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appr_cs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved CS')),
                ('appr_ogs_date', models.DateField(blank=True, null=True, verbose_name='Aprroved OGS')),
                ('notes', models.CharField(blank=True, max_length=511, verbose_name='Notes')),
                ('doc_type', models.CharField(choices=[('not sel', 'Not Selected'), ('deg plan', 'Degree Plan'), ('P. change commitee', 'Petition for change of committee'), ('P. course change', 'Petition for course change'), ('P. extension of time limits', 'Petition for extension of time limits'), ('P. waivers of exceptions', 'Petition for waivers of exceptions'), ('mdd', 'MDD'), ('other', 'Other')], default='not sel', max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Degree')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
