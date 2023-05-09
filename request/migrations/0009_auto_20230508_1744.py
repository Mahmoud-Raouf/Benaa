# Generated by Django 2.2.7 on 2023-05-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0008_auto_20230508_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectrequest',
            name='city',
            field=models.CharField(default=1, max_length=50, verbose_name='المدينة '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('شراء ', 'شراء'), ('بناء', 'بناء'), ('ترميم', 'ترميم')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AddField(
            model_name='projectrequest',
            name='workname',
            field=models.CharField(default=1, max_length=50, verbose_name='إسم العميل'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('مرفوض ', 'مرفوض'), ('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='name',
            field=models.CharField(max_length=50, verbose_name='عنوان المشروع'),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('مرفوض ', 'مرفوض'), ('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
    ]