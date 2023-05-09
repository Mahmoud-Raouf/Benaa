# Generated by Django 2.2.7 on 2023-05-09 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0013_auto_20230509_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationcomment',
            name='consultationrequest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='request.ConsultationRequest'),
        ),
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('مقبول', 'مقبول'), ('تحت المراجعة', 'تحت المراجعة'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('مقبول', 'مقبول'), ('تحت المراجعة', 'تحت المراجعة'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('بناء', 'بناء'), ('شراء ', 'شراء'), ('ترميم', 'ترميم')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
    ]