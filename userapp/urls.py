
from django.urls import path
from . import views

urlpatterns = [

    path("",views.User_listbook,name='booklist_userview'),
    path("detailsview_userview/<int:book_id>/",views.User_bookdetailsView,name="bookdetails_userview"),
    path('search_userview/',views.User_Search_Book,name='search_userview'),
    path('add_to_cart/<int:book_id>/',views.add_to_cart,name='addtocart'),
    path("view-cart/", views.view_cart,name='viewcart'),
    path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease_quantity'),
    path('remove-from-cart/<int:item_id>/',views.remove_from_cart,name='remove_cart'),
    path('create-checkout-session/',views.create_chekout_session,name='create-checkout-session'),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel,name='cancel'),

]
