from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("tracker/",views.tracker,name="tracker"),
    path("search/",views.search,name="search"),
    path("products/<int:id>",views.productView,name="ProdView"),
    path("checkout/",views.checkout,name="checkout"),
]