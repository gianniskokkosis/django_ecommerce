from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product_details/<int:pk>/', views.product_details, name='details'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name="add_to_cart"),
    path('mycart/', views.my_cart, name='mycart'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('buycart/<int:pk>/', views.buy_cart, name='buycart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
