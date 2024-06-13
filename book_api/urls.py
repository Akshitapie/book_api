from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.signout, name="signout"),
    path("details/<int:id>", views.details, name="details"),
    path("cart/", views.view_cart, name="view_cart"),
    path("add/<int:book_id_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("latestbook", views.latestbook, name="latestbook"),
    path("payment_success/", views.payment_success, name="payment_success"),
    path("add_book", views.add_book, name="add_book"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
