# Generated by Django 2.2.7 on 2023-05-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20230509_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userType',
            field=models.CharField(blank=True, choices=[('عميل', 'عميل'), ('شركة', 'شركة')], default='عميل', max_length=50, null=True),
        ),
    ]
