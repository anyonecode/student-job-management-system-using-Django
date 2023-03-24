# Generated by Django 4.1.7 on 2023-02-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_application_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='company',
            field=models.CharField(blank=True, choices=[('TCS', 'TCS'), ('IBM', 'IBM'), ('Wipro', 'Wipro'), ('Facebook', 'Facebook'), ('Microsoft', 'Microsoft'), ('Google', 'Google'), ('Tesla', 'Tesla'), ('Honda', 'Honda')], default='company', max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='qualification',
            field=models.CharField(blank=True, choices=[('Master', 'Master'), ('Btech', 'Btech'), ('Degree', 'Degree'), ('Diploma', 'Diploma'), ('Other', 'Other')], default='qualification', max_length=200),
        ),
    ]
