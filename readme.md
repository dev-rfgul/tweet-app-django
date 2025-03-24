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
6:we have to make a static folder in the main django project to server the static files, imgs etc as well as we have to make a template folder in main django projec to place the base.html file for implementing DRY concept 
7:now we can run this cmd to test our app wether is running ok or not.
    python manage.py runserver 8000
8: if its running fine then we can make models in our django project like this,
    open app folder > models.py > and add this import statement
        from django.contrib.auth.models import User
    then we can make models like this 
        class Tweet(models.Model):
         user=models.ForeignKey(User,on_delete=models.CASCADE)
         text=models.TextField(max_length=240)
         photo=models.ImageField(upload_to='photos/', blank=True,null=True)
         created_at=models.DateTimeField(auto_now_add=True)
         updated_at=models.DateTimeField(auto_now=True)
         def __str__(self):
             return f'{self.user.username}-{self.text[:20]}'
        
    after this we have to register this model into the admin of our app folder 
        from .models import Tweet
        admin.site.register(Tweet)
    after this run these cmds to migrate db changes
        python manage.py makemigrations
        python manage.py migrate
    now access the admin route  , and it should show your created model 
9: Moving towards Forms now 
    make forms.py in app folder and paste this code into that file 
        from django import forms    
        from .models import model_name
        #models can be created like that
        class TweetForm(forms.ModelForm):
            class Meta:
                model:Tweet
                fields:['text','photo'] // these text and photo should always be matching with your names in model
10:Moving towards views now 
    import statements
        from .models import model_name
        from .forms import  form_name
        from django.shortcuts import get_object_or_404
        #views can be created as you want ,
        def home(request):
        return render(request, 'index.html')
