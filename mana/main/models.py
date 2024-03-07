from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from django import forms
# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name_plural = "Quản lý đề tài nghiên cứu khoa học"
    id = models.AutoField(primary_key=True)
    Ma_de_tai = models.CharField(max_length=10, verbose_name="Mã đề tài")
    Ten_de_tai = models.CharField(max_length=200, verbose_name="Tên đề tài")
    level_CHOICES = [
        ('cấp nhà nước', 'Cấp nhà nước'),
        ('cấp bộ', 'Cấp bộ'),
        ('cấp tỉnh', 'Cấp tỉnh'),
        ('cấp cơ sở', 'Cấp cơ sở'),
    ]

    level = models.CharField(
        max_length=20,
        choices=level_CHOICES,
        default='Cấp cơ sở',  # Chọn giá trị mặc định nếu cần
        verbose_name="Cấp độ đề tài"
    )
    field_CHOICES = [
        ('công nghệ', 'Công nghệ'),
        ('sinh học', 'Sinh học'),
        ('kinh tế', 'Kinh tế'),
        ('khoa học', 'Khoa học'),
        ('văn hóa', 'Văn hóa'),
        ('vịch sử', 'Lịch sử'),
    ]

    field = models.CharField(
        max_length=20,
        choices=field_CHOICES,
        default='Công nghệ',  # Chọn giá trị mặc định nếu cần
        verbose_name="Lĩnh vực"
    )
    Chu_nhiem = models.CharField(max_length=800, verbose_name="Chủ nhiệm")
    Thanh_vien = models.CharField(max_length=800, verbose_name="Thành viên")
    Kinh_phi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Kinh phí")
    Loai_san_pham = models.CharField(max_length=200, verbose_name="Loại sản phẩm")
    Ngay_bat_dau = models.DateField(verbose_name="Ngày bắt đầu")
    Ngay_ket_thuc = models.DateField(verbose_name="Ngày kết thúc")


    Trang_thai_CHOICES = [
        ('đã duyệt', 'Đã duyệt'),
        ('yêu cầu sửa đổi', 'Yêu cầu sửa đổi'),
        ('đã hủy', 'Đã hủy'),
        ('đang thực hiện', 'Đang thực hiện'),
        ('hoàn tất nghiệm thu', 'Hoàn tất nghiệm thu'),

    ]

    Trang_thai = models.CharField(
        max_length=20,
        choices=Trang_thai_CHOICES,
        default='yêu cầu sửa đổi',  # Chọn giá trị mặc định nếu cần
        verbose_name="Trạng thái"
    )

    def __str__(self):
            return self.Ten_de_tai


class Tap_chi_dien_tu(models.Model):
    class Meta:
        verbose_name_plural = "Quản lý tạp chí điện tử"
    id = models.AutoField(primary_key=True)
    Ho_ten = models.CharField(max_length=80, verbose_name="Họ và tên")
    Ngay_sinh = models.DateField(verbose_name="Ngày sinh")
    Ten_y_tuong = models.CharField(max_length=800, verbose_name="Tên ý tưởng")
    Giang_vien_huong_dan = models.CharField(max_length=800, verbose_name="Giảng viên hướng dẫn")
    Ghi_chu = models.CharField(max_length=800, verbose_name="Ghi chú")
    Doi_tuong_CHOICES = [
            ('sinh viên', 'Sinh viên'),
            ('giảng viên', 'Giảng viên'),

        ]

    Doi_tuong = models.CharField(
            max_length=20,
            choices=Doi_tuong_CHOICES,
            default='sinh viên',  # Chọn giá trị mặc định nếu cần
            verbose_name = "Đối tượng"
        )

    def __str__(self):
            return self.Ten_y_tuong
class Hoi_nghi_hoi_thao(models.Model):
    class Meta:
        verbose_name_plural = "Quản lý hội nghị hội thảo"
    id = models.AutoField(primary_key=True)
    Ten_hoi_thao = models.CharField(max_length=100000000000, verbose_name="Tên hội thảo")
    Muc_dich = models.CharField(max_length=100000000000, verbose_name="Mục đích")
    Yeu_cau = models.CharField(max_length=100000000000, verbose_name="Yêu cầu")
    Thanh_phan_tham_du = models.CharField(max_length=100000000000, verbose_name="Thành phần tham dự")
    So_luong_tham_du = models.CharField(max_length=800, verbose_name="Số lượng tham dự")
    Noi_dung_chi_tiet = HTMLField(verbose_name="Nội dung chi tiết")
    Ngay_du_kien = models.DateField(verbose_name="Ngày dự kiến")
    Ngay_ket_thuc = models.DateField(verbose_name="Ngày kết thúc")
    Dia_diem = models.CharField(max_length=100000000000, verbose_name="Địa điểm")
    file = models.FileField(upload_to='uploads/', verbose_name="File đính kèm")
    def __str__(self):
            return self.Ten_hoi_thao