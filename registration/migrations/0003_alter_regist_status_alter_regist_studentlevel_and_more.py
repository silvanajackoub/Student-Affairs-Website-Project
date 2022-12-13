# Generated by Django 4.0.4 on 2022-05-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_regist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regist',
            name='Status',
            field=models.CharField(choices=[('Active', 'Active'), ('InActive', 'InActive')], default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='regist',
            name='StudentLevel',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='regist',
            name='System',
            field=models.CharField(choices=[('MainStream', 'MainStream'), ('Credit', 'Credit')], default='MainStream', max_length=20),
        ),
    ]
