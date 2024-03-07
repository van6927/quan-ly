from django.contrib import admin
from .models import Tap_chi_dien_tu, Hoi_nghi_hoi_thao, Project
# Register your models here.

    # Thêm các cài đặt tùy chọn khác nếu cần
class AdminTapChi(admin.ModelAdmin):
    list_display = ('id','Ten_y_tuong', 'Doi_tuong')
    search_fields = ('id','Ten_y_tuong', 'Doi_tuong')
    ordering = ('id',)
admin.site.register(Tap_chi_dien_tu, AdminTapChi)
class AdminHoiNghi(admin.ModelAdmin):
    list_display = ('id','Ten_hoi_thao', 'Ngay_du_kien')
    search_fields = ('id','Ten_hoi_thao', 'Ngay_du_kien')
    ordering = ('id',)
class AdminP(admin.ModelAdmin):
        list_display = ('id', 'Ten_de_tai', 'Trang_thai')
        search_fields = ('id', 'Ten_de_tai', 'Trang_thai')
        ordering = ('id',)

admin.site.register(Project, AdminP)
admin.site.register(Hoi_nghi_hoi_thao, AdminHoiNghi)
