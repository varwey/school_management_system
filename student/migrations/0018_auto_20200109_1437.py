# Generated by Django 3.0.2 on 2020-01-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20200109_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='status',
            field=models.CharField(choices=[('not enroll', 'Not Enroll'), ('enrolled', 'Enrolled'), ('regular', 'Regular'), ('irregular', 'Irregular'), ('passed', 'Passed')], default='not enroll', max_length=15),
        ),
    ]
