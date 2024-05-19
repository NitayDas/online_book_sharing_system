from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
from profileapp import views as profileview

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='home'),
    path('signup',views.signuppage,name='signup'),
    path('login/',views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('delete_user/<str:username>/',views.delete_user,name='delete_user'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name='password_reset_complete'),
    path('profile/<str:username>/',profileview.profile, name='profile'),
    path('edit_profile/',profileview.EditProfile, name='edit_profile'),
    path('readers/',profileview.readers, name='readers'),
    path('about/' ,profileview.about, name='about'),
    path('booklist/<str:username>/',profileview.booklist, name='booklist'),
    path('update_book/<int:id>/',profileview.update_book, name='update_book'),
    path('add_book/',profileview.add_book, name='add_book'),
    path('books/',profileview.books,name='books'),
    path('delete_book/<int:id>/',profileview.delete_book,name='delete_book'),
    path('book_request/<int:book_id>/', profileview.book_request, name='book_request'),
    path('see_book_request/', profileview.see_book_request, name='see_book_request'), 
    path('confirm_request/<int:book_id>/', profileview.confirm_request, name='confirm_request'),
    path('reject_request/<int:book_id>/', profileview.reject_request, name='reject_request'),
    path('borrowing_history/', profileview.borrowing_history, name='borrowing_history'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 