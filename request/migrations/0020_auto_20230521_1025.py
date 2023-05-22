# Generated by Django 3.2 on 2023-05-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0019_auto_20230521_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectmeetings',
            name='meetingsLink',
            field=models.URLField(verbose_name='رابط الاجتماع'),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('شراء ', 'شراء'), ('بناء', 'بناء'), ('ترميم', 'ترميم')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[('مرحلة البناء', 'مرحلة البناء'), ('مرحلة التشطيبات', 'مرحلة التشطيبات'), ('مرحلة تنظيف الأرض', 'مرحلة تنظيف الأرض'), ('مرحلة حفر الأساس', 'مرحلة حفر الأساس'), ('مرحلة وضع البنية التحتية', 'مرحلة وضع البنية التحتية'), ('مرحلة تسليح الأساس', 'مرحلة تسليح الأساس'), ('مرحلة إختيار الأرض', 'مرحلة إختيار الأرض'), ('تسليم العمل', 'تسليم العمل'), ('الإنتهاء من البناء', 'الإنتهاء من البناء')], max_length=150, verbose_name='حالة المرحلة '),
        ),
    ]