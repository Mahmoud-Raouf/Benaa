# Generated by Django 2.2.7 on 2023-05-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0010_auto_20230509_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('ترميم', 'ترميم'), ('شراء ', 'شراء'), ('بناء', 'بناء')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
    ]