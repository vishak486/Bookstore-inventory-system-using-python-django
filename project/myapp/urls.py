from . import views
from django.urls import path

urlpatterns=[
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("book", views.book, name="book"),
    path("author", views.author, name="author"),
    path("top_seller", views.top_seller, name="top_seller"),

    path("customer_details_add", views.customer_details_add, name="customer_details_add"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("admin_logout", views.admin_logout, name="admin_logout"),
    path("admin_home", views.admin_home, name="admin_home"),
    path("admin_customer_details_view", views.admin_customer_details_view, name="admin_customer_details_view"),
    path("admin_customer_details_delete", views.admin_customer_details_delete, name="admin_customer_details_delete"),
    path("admin_changepassword", views.admin_changepassword, name="admin_changepassword"),
    path("admin_category_details_add", views.admin_category_details_add, name="admin_category_details_add"),
    path("admin_category_details_view", views.admin_category_details_view, name="admin_category_details_view"),
    path("admin_category_details_edit", views.admin_category_details_edit, name="admin_category_details_edit"),
    path("admin_category_details_delete", views.admin_category_details_delete, name="admin_category_details_delete"),

    path("admin_book_master_view", views.admin_book_master_view, name="admin_book_master_view"),
    path("admin_book_master_add", views.admin_book_master_add, name="admin_book_master_add"),
    path("admin_book_master_delete", views.admin_book_master_delete, name="admin_book_master_delete"),
    path("admin_book_master_stock_edit", views.admin_book_master_stock_edit, name="admin_book_master_stock_edit"),
    path("admin_book_master_edit", views.admin_book_master_edit, name="admin_book_master_edit"),
    path("admin_bill_view", views.admin_bill_view, name="admin_bill_view"),
    path("admin_bill_details_view", views.admin_bill_details_view, name="admin_bill_details_view"),


    path("customer_login", views.customer_login, name="customer_login"),
    path("customer_home", views.customer_home, name="customer_home"),
    path("customer_logout", views.customer_logout, name="customer_logout"),
    path("customer_changepassword", views.customer_changepassword, name="customer_changepassword"),
    path("customer_contact_us", views.customer_contact_us, name="customer_contact_us"),
    path("customer_about", views.customer_about, name="customer_about"),
    path("customer_view_more_details", views.customer_view_more_details, name="customer_view_more_details"),
    path("customer_book_search", views.customer_book_search, name="customer_book_search"),
    path("customer_cart_add", views.customer_cart_add, name="customer_cart_add"),
    path("customer_cart_view", views.customer_cart_view, name="customer_cart_view"),
    path("customer_cart_delete", views.customer_cart_delete, name="customer_cart_delete"),
    path("customer_cart_quantity_edit", views.customer_cart_quantity_edit, name="customer_cart_quantity_edit"),
    path("customer_payment_add", views.customer_payment_add, name="customer_payment_add"),
    path("customer_payment_view", views.customer_payment_view, name="customer_payment_view"),
    path("customer_bill_view", views.customer_bill_view, name="customer_bill_view"),
    path("customer_bill_details_view", views.customer_bill_details_view, name="customer_bill_details_view"),
     



]