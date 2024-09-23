
from django.urls import path
from . import views

urlpatterns = [
    #  function based view
    path("createbook",views.createBook,name='createbook'),
    path("",views.listbook,name='booklist'),
    path("detailsview/<int:book_id>/",views.detailsView,name="details"),
    path("updateview/<int:book_id>/",views.updateBook,name="update"),
    path("deleteview/<int:book_id>/",views.deleteView,name="delete"),
    path("author/",views.Create_Author,name='author'),
    path('index',views.index),
    path('search/',views.Search_Book,name='search'),

]
