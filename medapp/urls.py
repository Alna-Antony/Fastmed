from django.urls import path
from medapp import views

urlpatterns = [
    path('medpg/',views.medpg,name="medpg"),
    path('addcat/',views.addcat,name="addcat"),
    path('savedata/',views.savedata,name="savedata"),
    path('catdisplay/',views.catdisplay,name="catdisplay"),
    path('catedit/<int:catid>/',views.catedit,name="catedit"),
    path('catupdate/<int:catid>/',views.catupdate,name="catupdate"),
    path('catdelete/<int:catid>/', views.catdelete, name="catdelete"),
    path('addpro/',views.addpro,name="addpro"),
    path('savesprod/', views.savesprod, name="savesprod"),
    path('prodisplay/', views.prodisplay, name="prodisplay"),
    path('proedit/<int:proid>/', views.proedit, name="proedit"),
    path('proupdate/<int:proid>/', views.proupdate, name="proupdate"),
    path('prodelete/<int:proid>/', views.prodelete, name="prodelete"),

    path('admins/', views.admins, name="admins"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('contactdis/', views.contactdis, name="contactdis"),
    path('cartdis/', views.cartdis, name="cartdis"),


]