# Generated by Django 2.2.7 on 2023-04-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_auto_20230428_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_status',
            field=models.CharField(choices=[('مرفوض ', 'مرفوض'), ('مقبول', 'مقبول'), ('تحت المراجعة', 'تحت المراجعة')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
    ]
