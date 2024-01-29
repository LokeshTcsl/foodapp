
from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    # path("", views.index, name="index"),
    path("",views.IndexClassView.as_view(),name='index'),

    path("item/",views.item, name='item'),

    # path("<int:item_id>/",views.detail, name='detail'),
    path("<int:pk>/",views.FoodDetail.as_view(), name='detail'),

    #add item
    # path('create_item',views.create_item, name='create_item'),
    path('create_item',views.CreateItem.as_view(), name='create_item'),

    #edit
    path('update/<int:id>',views.update_item,name='update_item'),

    #delete
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]
