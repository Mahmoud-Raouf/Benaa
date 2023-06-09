# Generated by Django 2.2.7 on 2023-05-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0012_auto_20230509_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultationcomment',
            old_name='product',
            new_name='consultationrequest',
        ),
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('مرفوض ', 'مرفوض'), ('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('مرفوض ', 'مرفوض'), ('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('بناء', 'بناء'), ('ترميم', 'ترميم'), ('شراء ', 'شراء')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
    ]
