1:after initializing the project , first of all , if you have to use the imgs , then import os in settings.py
    import os
2:then add media configuration , at the bottom of the page
    MEDIA_URL=  '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
3:if you have to use the static files, then configure static files as well
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
4:to use static media , we have to change the urls.py as well and add some configuration there.
    i: import statments 
        from django.conf import settings
        from django.conf.urls.static import static
    ii: urlpatterns=[]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
5:now you can create django apps by this command
    python manage.py startapp "name_of_the_app"
        in this app you dont get "urls.py" so we have to crate it manually , and then setup the basic urls.py file like this
            from django.contrib import admin
            from django.urls import path
            from django.conf import settings
            from django.conf.urls.static import static

            urlpatterns = [
               # path('', admin.site.urls),
            ]
        this app is yet not recognized by the main django project so we have to tell the django that , we have created an app.  
            to do this , open setting.py file> find INSTALLED_APP> write the name of your app
            after this you have to configure templates folder as well.
                setting.py>find templates array>find dirs array >then paste this in dirs array
                    os.path.join(BASE_DIR,'templates')
                    now we can create a templates folder in our app folder 
        once we have created the app , most likely we would like to perform some specific functionalities from that app and , we need some routes for that app , to do this we have to tell our main urls.py file of our main django project folder that we have an app , 
            from django.urls import path,include
            path('name of the app/', include('name of the app .urls')),
            // we can use something else as well in the url , it will be the route eg. localhost:3000/nameoftheapp/tweet and etc , 
            // but the include should have the exact name of the app

