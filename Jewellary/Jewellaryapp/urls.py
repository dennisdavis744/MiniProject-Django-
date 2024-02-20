from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer_rg/',views.customer_rg,name='customer_rg'),
    path('custom_login/',views.custom_login,name='custom_login'),
    path('custom_dashboard/',views.custom_dashboard,name="custom_dashboard"),
    path('custom_update/<str:pk>', views.custom_update, name='custom_update'),
    path('reg_staff/', views.reg_staff, name='reg_staff'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('product_delete/<str:pk>', views.product_delete, name='product_delete'),
    path('product_update/<str:pk>', views.product_update, name='product_update'),
    path('staff_logout/', views.staff_logout, name='staff_logout'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('lalu/', views.lalu, name='lalu'),
    path('about/',views.about,name='about'),
    path('contacts/',views.contacts,name='contacts'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('add_product/',views.add_product,name='add_product'),
    path('cart/',views.cart,name='cart'),
    path('cartel/',views.cartel,name='cartel'),
    path('detailedview/<str:pk>',views.detailedview,name="detailedview"),
]