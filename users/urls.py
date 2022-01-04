from django.urls import path
from .views import * #memanggil semua fungsi yang ada didalam

urlpatterns = [

   # User
    path('',users, name='tabel_users'),
    path('detail/<int:id>', user_detail, name='user_detail'),
    path('edit/<int:id>', user_edit, name='user_edit'),
    path('hapus/<int:id>', user_hapus, name='user_hapus'),
    
]
