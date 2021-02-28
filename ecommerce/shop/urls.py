from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product_details/<int:pk>/', views.product_details, name='details'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('my_wishlist', views.my_wishlist, name='whishlist'),
    path('add_to_wishlist/<int:pk>', views.add_to_wishlist, name='add-to-whishlist')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
