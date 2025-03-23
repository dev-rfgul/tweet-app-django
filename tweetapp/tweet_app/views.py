from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

def tweet_create(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES) # request.FILES is used to upload files
        if form.is_valid():
            tweet=form.save(commit=False) # commit=False is given when the data is not to be saved in the db 
            tweet.user=request.user
            tweet.save()    # now it will save the data in the db as commit false is not given 
            return redirect('tweet_list')
        
    else:
        form=TweetForm()
    return render(request,'tweet_create.html',{'form':form})


def tweet_edit(request, tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user=request.user)#1st parameter is for searching is to be made in which model and 2nd parameter is for what is to be searched, and 3rd parameter is for , that only the one who tweeted it could edit his own tweet.
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False) # commit=False is given when the data is not to be saved in the db 
            tweet.user=request.user
            tweet.save()    # now it will save the data in the db as commit false is not given 
            return redirect('tweet_list')
        
    else:
        form=TweetForm(instance=tweet) # instance is used to edit the data as to eidt we have to provide the prev data
    return render(request,'tweet_form.html',{'form':form})

def tweet_delete(request, tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html', {'tweet':tweet})