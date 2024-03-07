from django.shortcuts import redirect

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='Admin').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')  # Chuyển hướng đến trang chủ hoặc trang khác tùy ý
    return _wrapped_view