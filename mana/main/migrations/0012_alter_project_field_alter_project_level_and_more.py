# Generated by Django 5.0.1 on 2024-03-07 02:13

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='field',
            field=models.CharField(choices=[('công nghệ', 'Công nghệ'), ('sinh học', 'Sinh học'), ('kinh tế', 'Kinh tế'), ('khoa học', 'Khoa học'), ('văn hóa', 'Văn hóa'), ('vịch sử', 'Lịch sử')], default='Công nghệ', max_length=20, verbose_name='Lĩnh vực'),
        ),
        migrations.AlterField(
            model_name='project',
            name='level',
            field=models.CharField(choices=[('cấp nhà nước', 'Cấp nhà nước'), ('cấp bộ', 'Cấp bộ'), ('cấp tỉnh', 'Cấp tỉnh'), ('cấp cơ sở', 'Cấp cơ sở')], default='Cấp cơ sở', max_length=20, verbose_name='Cấp độ đề tài'),
        ),
        migrations.DeleteModel(
            name='Project_Profile',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
        migrations.AlterModelOptions(
            name='hoi_nghi_hoi_thao',
            options={'verbose_name_plural': 'Quản lý hội nghị hội thảo'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': 'Quản lý đề tài nghiên cứu khoa học'},
        ),
        migrations.AlterModelOptions(
            name='tap_chi_dien_tu',
            options={'verbose_name_plural': 'Quản lý tạp chí điện tử'},
        ),
        migrations.AlterField(
            model_name='hoi_nghi_hoi_thao',
            name='Dia_diem',
            field=models.CharField(max_length=100000000000, verbose_name='Địa điểm'),
        ),
        migrations.AlterField(
            model_name='hoi_nghi_hoi_thao',
            name='Muc_dich',
            field=models.CharField(max_length=100000000000, verbose_name='Mục đích'),
        ),
        migrations.AlterField(
            model_name='hoi_nghi_hoi_thao',
            name='Noi_dung_chi_tiet',
            field=tinymce.models.HTMLField(verbose_name='Nội dung chi tiết'),
        ),
        migrations.AlterField(
            model_name='hoi_nghi_hoi_thao',
            name='Ten_hoi_thao',
            field=models.CharField(max_length=100000000000, verbose_name='Tên hội thảo'),
        ),
        migrations.AlterField(
            model_name='hoi_nghi_hoi_thao',
            name='Thanh_phan_tham_du',
            field=models.CharField(max_length=100000000000, verbose_name='Thành phần tham dự'),
        ),
        migrations.AlterField(
            model_name='hoi_nghi_hoi_thao',
            name='Yeu_cau',
            field=models.CharField(max_length=100000000000, verbose_name='Yêu cầu'),
        ),
        migrations.AlterField(
            model_name='tap_chi_dien_tu',
            name='Ho_ten',
            field=models.CharField(max_length=80, verbose_name='Họ và tên'),
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]