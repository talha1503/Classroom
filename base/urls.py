from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.login_view,name='login'),
    path('register/', views.register_view,name='register'),
    path('logout/', views.logout_view,name='logout'),
    path('home/', views.home,name='home'),
    # path('create_class/',views.create_class, name='create_class'),
    # path('join_class/',views.join_class,name='join_class'),
    path('class/<int:id>',views.render_class,name='render_class'),
    path('create_assignment/<int:classroom_id>',views.create_assignment,name='create_assignment'),
    path('assignment_summary/<int:assignment_id>',views.assignment_summary,name='assignment_summary'),
    path('delete_assignment/<int:assignment_id>',views.delete_assignment,name='delete_assignment'),
    path('unenroll_class/<int:classroom_id>',views.unenroll_class,name='unenroll_class'),
    path('delete_class/<int:classroom_id>',views.delete_class,name='delete_class'),
    path('submit_assignment/<int:assignment_id>',views.assignment_submission,name='submit_assignment'),
    path('create_class_request/',views.create_class_request,name='create_class_request'),
    path('join_class_request/',views.join_class_request,name='join_class_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)