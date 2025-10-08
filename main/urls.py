from django.urls import path
from main.views import show_main, add_employee, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product, show_product, register, login_user, logout_user, add_car, edit_product, delete_product, add_product_ajax, get_categories_ajax, edit_product_ajax, delete_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('employee/', add_employee, name='add_employee'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('add-product/', add_product, name='add_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('car/new/', add_car, name='add_car'),
    path('product/<str:id>/edit/', edit_product, name='edit_product'),
    path('product/<str:id>/delete/', delete_product, name='delete_product'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit-product-ajax/<str:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<str:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('get-categories-ajax/', get_categories_ajax, name='get_categories_ajax'),
]