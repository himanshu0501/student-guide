from django.shortcuts import render , redirect , get_object_or_404
from .forms import UserRegisterForm , ExtenededuserForm# this is the form that we have created in the forms.py file using the usercreation form
from django.contrib import messages # we are importing it to show the flash messages.
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView                                     # We will now show the blogs in listview
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# different type of messages that this library have
# message.debug
# message.info
# message.error
# message.success
# message.warning
# django already have some forms which is used as user creation form
# these forms are classes which will be converted into html later

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # if form is having some data then we are retrieving that data using the POST request "which we say bound state of the form"
        user_detailform = ExtenededuserForm(request.POST)
        if form.is_valid() and user_detailform.is_valid(): # here we are checking is our form is valid  or not  
            user = form.save()
            user_details = user_detailform.save(commit=False) # it will create a userdetail object but won't save it and give it to us.
            user_details.user=user
            user_details.save()
            username = form.cleaned_data.get('username') # here we are retrieving the username from the form that input the data #Any data the user submits through a form will be passed to the server as strings. It doesn't matter which type of form field was used to create the form. Eventually, the browser would will everything as strings. When Django cleans the data it automatically converts data to the appropriate type. For example IntegerField data would be converted to an integer, CharField data would be converted to a string, BooleanField data would be converted to a bool i.e True or False and so on. In Django, this cleaned and validated data is commonly known as cleaned data. We can access cleaned data via cleaned_data dictionary:
            messages.success(request,f'Account created for {username},Now you can login!')
            return redirect('login')
    else: #You must never access the data directly using self.field_name as it may not be safe.
        user_detailform = ExtenededuserForm()
        form = UserRegisterForm() # this is the unbound state when form is empty shown at first time and data is there to retrieve from it.
    return render(request,'placement/registeration.html',{'user_detailform':user_detailform,'form':form})



 # this function is returing the base view of the placement app
def home(request):
    posts = Post.objects.all()
    context ={ 'posts':posts}
    return render(request,'placement/home.html',context)




# by default class based view search for a template named as <app>/<model>_<viewtype>.html
class PostListView(ListView):
    model = Post
    template_name = 'placement/home.html'
    context_object_name = 'posts' # here we are defining that for the context of this view we will use the posts
    ordering = ['-date_posted'] # here we are saying that the order of our posts sould be new -> older ..... if we will remove the minus sign 
    # in [-date_posted] then it will show the list with order older -> new 
    paginate_by = 2 # when we will have many posts then we want to show only assume 2 posts per page so here we are dividing the posts and making the page





class PostDetailView(DetailView):  # it will provide the detail of our post 
    model = Post # so it will be looking for a template with url <app>/<model>_<viewtype>.html






# to create a post a user must be logged in and we can do that using the decoartor @login_required but here it is class based view so we can't use that 
class PostCreateView(LoginRequiredMixin,CreateView): # its a view where we will create a new post it will give us a form 
    model = Post                 # these view are strong we don't even need to make form.py  we only have to tell with which model we have to work
    fields = ['title','content']    # here we are setting the fields that a form will contain two fields title and content 
    # we will get integrity error bcoz right now we haven't fill the author field and that can be null so we have to tell django that our current user is our author
    # so here we will override the form valid method to tell django that current user is author
    def form_valid(self,form):
        form.instance.author = self.request.user # hey the form you are trying to submit before you that take the instance and set the author equal to current user logged in
        return super().form_valid(form)  
        # now if we will submit post will be created but django doesn't know about the redirect link





class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # this function will check is the person updating the post is same who created it.
        post = self.get_object() # it will give us the current post we are updating
        if self.request.user == post.author:  # this is checking if the user is same as the author of the post
            return True
        return False






# it will used to delete the post 
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/home/placement'

    def test_func(self): # this function will check is the person updating the post is same who created it.
        post = self.get_object() # it will give us the current post we are updating
        if self.request.user == post.author:  # this is checking if the user is same as the author of the post
            return True
        return False





class UserPostListView(ListView):  #  here we are creating the page where all the personally uploaded post by any user will be displayed
    model = Post
    template_name = 'placement/user_posts.html'
    context_object_name = 'posts' # here we are defining that for the context of this view we will use the posts
    paginate_by = 2 # when we will have many posts then we want to show only assume 2 posts per page so here we are dividing the posts and making the page


    def get_queryset(self):  # we will modify the List by overloading this function and only show the current user posts 
        user = get_object_or_404(User,username=self.kwargs.get('username'))  # here we are capturing the username and store it in the user otherwise we will show 404 error.
        return Post.objects.filter(author=user).order_by('-date_posted') # this will restrict the page to show the post only related to that user and order them by latest->old.
