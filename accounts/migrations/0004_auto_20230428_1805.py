# Generated by Django 2.2.7 on 2023-04-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_company_company_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='founding_date',
            field=models.CharField(default=1, max_length=150, verbose_name='تاريخ التأسيس'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='number_projects',
            field=models.CharField(default=1, max_length=150, verbose_name='عدد المشاريع'),
            preserve_default=False,
        ),
    ]
