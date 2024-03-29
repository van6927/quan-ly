# Generated by Django 5.0.1 on 2024-01-20 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_project_trang_thai'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tap_chi_dien_tu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Ho_ten', models.CharField(max_length=10)),
                ('Ngay_sinh', models.DateField()),
                ('Ten_y_tuong', models.CharField(max_length=800)),
                ('Giang_vien_huong_dan', models.CharField(max_length=800)),
                ('Ghi_chu', models.CharField(max_length=800)),
                ('Doi_tuong', models.CharField(choices=[('sinh viên', 'Sinh viên'), ('giảng viên', 'Giảng viên')], default='sinh viên', max_length=20)),
            ],
        ),
    ]
