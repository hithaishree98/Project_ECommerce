from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
    path('', views.main, name="index"),
	path('product/', views.product, name="Shop"),
	path('cart/', views.cart, name="cart"),
	path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('search/', views.search_products, name='search_products'),
    path('sp/', views.sp, name="product1"),
    path('sp1/', views.sp1, name="product2"),
    path('sp2/', views.sp2, name="product3"),
    path('sp3/', views.sp3, name="product4"),
    path('sp4/', views.sp4, name="product5"),
    path('sp5/', views.sp5, name="product6"),
    path('sp6/', views.sp6, name="product7"),
    path('sp7/', views.sp7, name="product8"),
    path('sp8/', views.sp8, name="product9"),
    path('sp9/', views.sp9, name="product10"),
    path('sp10/', views.sp10, name="product11"),
    path('sp11/', views.sp11, name="product12"),
    path('sp12/', views.sp12, name="product13"),
    path('sp13/', views.sp13, name="product14"),
    path('sp14/', views.sp14, name="product15"),
    path('update_item/', views.updateItem, name="update_item"),
]