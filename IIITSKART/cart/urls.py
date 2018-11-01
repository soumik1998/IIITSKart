from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cart'
router = routers.DefaultRouter(views.CustomerViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'p_review', views.P_reviewViewSet)
router.register(r'C_review', views.C_reviewViewSet)
router.register(r'Category', views.CategoryViewSet)
# router.register(r'Superuser',views.Super_UserViewSet)
# router.register(r'Login',views.LoginViewSet)

urlpatterns = [
  path(r'dashboard/', views.dashboard, name='dashboard'),
  url(r'^', include(router.urls)),
  path('accounts/', include('django.contrib.auth.urls')),
  path('login-view/', views.login_page, name='login_page'),
  path(r'profilevalidation/', views.profile_val, name='profile_val'),
  path(r'profile/', views.profile_view, name='profile'),
  path(r'profile_photo_upload/', views.profile_photo_upload, name='profile_photo_upload'),
  path(r'profilevalidationapi/', views.profile_val_api, name='profile_val_api'),
  path(r'makeuser/', views.makeuser, name='makeuser'),
  path(r'receive/', views.receive, name='receive'),
  path(r'send/', views.send, name='send'),
  path(r'go-to-dashboard/', views.go_to_dashboard, name='go-to-dashboard'),
  # path(r'search/', views.search, name='search'),
  path(r'searchproduct/', views.search_product, name='search_product'),
  path(r'logout/', views.logout_view, name='logout'),
  path(r'receiveProduct/', views.receiveProduct, name='receiveProduct'),
  path(r'sellproduct/', views.add_product, name='add_product'),
  path(r'test/', views.test_api, name='test'),
  path(r'get_user/', views.get_userdetails, name='test'),
  path(r'get_pro/', views.get_products, name='Get_products'),
  path(r'buy_pro/', views.buy_product, name='buy_product'),
  path(r'sellerinfo/', views.seller_info, name='seller_info'),
  path(r'productdetail/', views.product_detail, name='product_detail'),
  path(r'profileupdatde/', views.update_profile, name='update_profile'),
  path(r'sellerreview/', views.seller_review, name='seller_review'),
  path(r'seller_reviewApi/', views.seller_review_api, name='seller_review'),
  path(r'reportseller/', views.report_seller, name='report_seller'),
  path(r'customeract/', views.customer_act, name='customer_act'),
  path(r'addpro/', views.customer_activity_sell, name='add_pro'),
  path(r'cactbuy/', views.customer_activity_buy, name='cact_buy'),
  path(r'addtowish/', views.add_to_wishlist, name='add_to_wishlist'),
  path(r'editwishlist/', views.edit_wishlist, name='edit_wishlist'),
  path(r'addacomment/', views.add_a_comment, name='add_a_comment'),
  url(r'^callback/(?P<token>.*)/$', views.register_with_iiits, name='register_with_iiits'),
  url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)