from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addadmin/',views.addadmin,name="addadmin"),
    path('saveadmin/',views.saveadmin,name="saveadmin"),
    path('admindisplay/',views.admindisplay,name="admindisplay"),
    path('editadminpage/<int:dataid>/', views.editadminpage, name="editadminpage"),
    path('updateadmin/<int:dataid>/', views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),
    path('category/',views.category,name="category"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('categorydisplay/',views.categorydisplay,name="categorydisplay"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),
    path('product/',views.product,name="product"),
    path('productsave/',views.productsave,name="productsave"),
    path('productdisplay/',views.productdisplay,name="productdisplay"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('displaymessage/',views.displaymessage,name="displaymessage"),
    path('deletemessage/<int:dataid>/',views.deletemessage,name="deletemessage"),
    path('orders/',views.orders,name="orders"),
    path('deleteorder/<int:dataid>/',views.deleteorder,name="deleteorder"),
]