from django.urls import path
from .views import update_item, delete_item, CreateItem, DetailItem, IndexClassView


urlpatterns = [
    path('', IndexClassView.as_view(), name='index'),
    path('food/<slug:slug>', DetailItem.as_view(), name='detail'),
    path('create-item/', CreateItem.as_view(), name='create-item'),
    path('update-item/<slug:item_slug>', update_item, name='update-item'),
    path('delete-item/<slug:item_slug>', delete_item, name='delete-item')

]