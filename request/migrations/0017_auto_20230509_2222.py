# Generated by Django 2.2.7 on 2023-05-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0016_auto_20230509_2200'),
    ]

    operations = [
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
            field=models.CharField(choices=[('شراء ', 'شراء'), ('ترميم', 'ترميم'), ('بناء', 'بناء')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[('مرحلة حفر الأساس', 'مرحلة حفر الأساس'), ('مرحلة إختيار الأرض', 'مرحلة إختيار الأرض'), ('تسليم العمل', 'تسليم العمل'), ('مرحلة تسليح الأساس', 'مرحلة تسليح الأساس'), ('مرحلة تنظيف الأرض', 'مرحلة تنظيف الأرض'), ('مرحلة وضع البنية التحتية', 'مرحلة وضع البنية التحتية'), ('مرحلة التشطيبات', 'مرحلة التشطيبات'), ('الإنتهاء من البناء', 'الإنتهاء من البناء'), ('مرحلة البناء', 'مرحلة البناء')], max_length=150, verbose_name='حالة المرحلة '),
        ),
    ]