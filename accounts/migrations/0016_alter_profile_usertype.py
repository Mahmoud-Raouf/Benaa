# Generated by Django 3.2 on 2023-05-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_profile_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userType',
            field=models.CharField(blank=True, choices=[('عميل', 'عميل'), ('شركة', 'شركة')], default='عميل', max_length=50, null=True),
        ),
    ]
