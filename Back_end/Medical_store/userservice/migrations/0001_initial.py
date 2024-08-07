# Generated by Django 5.0.4 on 2024-06-26 06:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dropdown_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_type', models.CharField(max_length=60, null=True)),
                ('list_value', models.CharField(max_length=255, null=True)),
                ('filter_by', models.CharField(max_length=60, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'dropdown_table',
            },
        ),
        migrations.CreateModel(
            name='goods_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_type', models.CharField(max_length=75, null=True)),
                ('item_name', models.CharField(max_length=255, null=True)),
                ('item_brand', models.CharField(max_length=100, null=True)),
                ('item_description', models.CharField(max_length=255, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
                ('num_of_exp_date', models.IntegerField(null=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'goods_main',
            },
        ),
        migrations.CreateModel(
            name='person_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_type', models.CharField(max_length=45, null=True)),
                ('person_no', models.CharField(max_length=15, null=True)),
                ('first_name', models.CharField(max_length=75, null=True)),
                ('last_name', models.CharField(max_length=75, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('civil_status', models.CharField(max_length=30, null=True)),
                ('nic', models.CharField(max_length=15, null=True)),
                ('effect', models.CharField(max_length=45, null=True)),
                ('effect_type', models.CharField(max_length=45, null=True)),
                ('effect_status', models.CharField(max_length=45, null=True)),
                ('effect_reason', models.CharField(max_length=45, null=True)),
                ('effect_date', models.DateField(null=True)),
                ('is_bed_sore', models.BinaryField(null=True)),
                ('contact_number', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('district', models.CharField(max_length=60, null=True)),
                ('now_status', models.CharField(max_length=45, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'person_details',
            },
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_type', models.CharField(max_length=150, null=True)),
                ('supplier_name', models.CharField(max_length=255)),
                ('supplier_address', models.CharField(max_length=255, null=True)),
                ('contry', models.CharField(max_length=75, null=True)),
                ('contact_number', models.CharField(max_length=15, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, null=True)),
                ('userid', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('privilege', models.CharField(max_length=120, null=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2024, 6, 26, 12, 7, 2, 238489))),
                ('create_by', models.CharField(max_length=15, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
        migrations.CreateModel(
            name='in_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_quantity', models.FloatField(null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
                ('in_date', models.DateField(null=True)),
                ('exp_date', models.DateField(null=True)),
                ('in_type', models.CharField(max_length=120, null=True)),
                ('available_stock', models.FloatField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('goods_main', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userservice.goods_main')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userservice.supplier')),
            ],
            options={
                'db_table': 'in_details',
            },
        ),
        migrations.CreateModel(
            name='out_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_date', models.DateField(null=True)),
                ('out_type', models.CharField(max_length=120, null=True)),
                ('out_quantity', models.FloatField(null=True)),
                ('out_unit', models.CharField(max_length=20, null=True)),
                ('by_whom', models.CharField(max_length=120, null=True)),
                ('status', models.IntegerField(default=1)),
                ('in_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userservice.in_details')),
                ('person_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userservice.person_details')),
            ],
            options={
                'db_table': 'out_details',
            },
        ),
        migrations.CreateModel(
            name='nurse_duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('person_type', models.CharField(max_length=45, null=True)),
                ('duty_option', models.CharField(max_length=120, null=True)),
                ('status', models.IntegerField(default=1)),
                ('note', models.CharField(max_length=150, null=True)),
                ('designation', models.CharField(max_length=150, null=True)),
                ('by_whom', models.CharField(max_length=150, null=True)),
                ('person_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userservice.person_details')),
            ],
            options={
                'db_table': 'nurse_duty',
            },
        ),
        migrations.CreateModel(
            name='home_admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('if_new', models.SmallIntegerField(default=0, null=True)),
                ('disease', models.CharField(max_length=75, null=True)),
                ('admission_date', models.DateField(null=True)),
                ('room_no', models.CharField(max_length=15, null=True)),
                ('given_things', models.CharField(max_length=120, null=True)),
                ('is_go_clinic', models.SmallIntegerField(default=0, null=True)),
                ('hospital_name', models.CharField(max_length=255, null=True)),
                ('bed_sores_status', models.CharField(max_length=255, null=True)),
                ('act_independently', models.SmallIntegerField(default=0, null=True)),
                ('toilet_managing', models.CharField(max_length=255, null=True)),
                ('urine_managing', models.CharField(max_length=255, null=True)),
                ('work_in_uyirilai', models.CharField(max_length=75, null=True)),
                ('discharge_date', models.DateField(null=True)),
                ('discharge_reason', models.CharField(max_length=120, null=True)),
                ('note', models.CharField(max_length=250, null=True)),
                ('status', models.IntegerField(default=1)),
                ('person_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userservice.person_details')),
            ],
            options={
                'db_table': 'home_admission',
            },
        ),
        migrations.CreateModel(
            name='login_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=75)),
                ('log_date', models.DateField(null=True)),
                ('log_time', models.TimeField(null=True)),
                ('location', models.CharField(max_length=255)),
                ('log_out_time', models.TimeField(null=True)),
                ('num_of_attempt', models.IntegerField(null=True)),
                ('log_status', models.CharField(max_length=75)),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userservice.user_details')),
            ],
            options={
                'db_table': 'login_info',
            },
        ),
    ]
