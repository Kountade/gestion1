from django.urls import path
from dashbord import views


urlpatterns = [
    path("dash",views.index, name="dash-index"),
    path("staff", views.staff, name="dash-staff"),
    path("staff/detail/<int:pk>/",views.staff_detail, name="dash-Staff-detail"),
    path("product", views.product, name="dash-product"),
    path('product/delete/<int:pk>/', views.product_delete,
         name='dash-product-delete'),
     path('product/edit/<int:pk>/', views.product_edit,
         name='dash-product-edit'),
    path("order", views.order, name="dash-order"),
    path("profil", views.profil, name="dash-profil"),
    path('order/', views.order, name='dash-order'),
    
    
]


