from django.urls import path
from frontend import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('homepg/', views.homepg, name="homepg"),
    path('storepg/', views.storepg, name="storepg"),
    path('filterpg/<cat_name>/', views.filterpg, name="filterpg"),
    path('singlepg/<int:proid>/', views.singlepg, name="singlepg"),
    path('aboutpg/', views.aboutpg, name="aboutpg"),
    path('contactpg/', views.contactpg, name="contactpg"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('reg/',views.reg, name="reg"),
    path('saves/', views.saves, name="saves"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cartpg/', views.cartpg, name="cartpg"),
    path('savecarts/',views.savecarts,name="savecarts"),
    path('med_search/',views.med_search,name="med_search"),
    path('cartdelete/<int:pro_id>/', views.cartdelete, name="cartdelete"),
    path('checkoutpg/', views.checkoutpg, name="checkoutpg"),
    path('apply_coupon/<int:total_price>/', views.apply_coupon, name='apply_coupon'),
    path('prescr/', views.prescr, name="prescr"),
    path('paymentpg/', views.paymentpg, name="paymentpg"),
    path('savepay/', views.savepay, name="savepay"),
    path('savecheck/', views.savecheck, name="savecheck"),
    path('thank/', views.thank, name="thank"),
    path('savepdf/', views.savepdf, name="savepdf"),
    path('generate_dynamic_pdf/', views.generate_dynamic_pdf, name="generate_dynamic_pdf"),
    path('thanks/', views.thanks, name="thanks"),
    path('deleteuser/', views.deleteuser, name="deleteuser"),

]



