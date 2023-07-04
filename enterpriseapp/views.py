from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
# Create your views here.

from django.template.defaulttags import register

@register.filter(name='split')
def split(value, key): 
 
    value.split("key")
    return value.split(key)

def header_footer_data():
    post = Post.objects.select_related('category_id').select_related('author').all().order_by('created_on')[:4]
    print(post)
    home = Home.objects.first()
    # contactaddress = Companycontactaddress.objects.all()
    service = Service_publisher.objects.all()[:8]
    return {
        'home': home,
        # 'footer': footer,
        # 'contactaddress': contactaddress,
        'service':service,
        'post':post,
    }

def Homepage(request):
        home = Home.objects.all()
        sliders = Slider.objects.all()
        Projects = Project_publisher.objects.all()
        services = Service_publisher.objects.all()
        homeservice = Homeserviceshow.objects.all()[:4]
        context = {'home':home, 'sliders':sliders, 'Projects':Projects, 'services':services, 'homeservice':homeservice}
        print(context)
        if request.method == "POST":
            name = request.POST['name']
            email  = request.POST['email']
            phone  = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            print(name)
            if len(name) > 4:
                contact = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
                contact.save()
                messages.success(request,'Successfully Form Submit')
                return redirect('/')
            else:
                messages.error(request,'First Name Should Be more then 4 chars')
                return redirect('/')        
        return render(request, 'frontend/index.html', context)

def About(request):
    about = Aboutus.objects.first()
    services = Service_publisher.objects.all()
    context = {'about':about, 'services':services}
    return render(request, 'frontend/about.html', context)

def Service(request):
    services = Service_publisher.objects.all()
    context = {'services':services}
    return render(request, 'frontend/services.html', context)

def Projects(request):
    Projects = Project_publisher.objects.all()
    context = {'Projects':Projects}
    return render(request, 'frontend/projects.html', context)

def Farm(request):
    return render(request, 'frontend/farm.html')

def Contact_view(request):
        if request.method == "POST":
            name = request.POST['name']
            email  = request.POST['email']
            phone  = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            print(name)
            if len(name) > 4:
                contact = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
                contact.save()
                messages.success(request,'Successfully Form Submit')
                return redirect('/contact')
            else:
                messages.error(request,'First Name Should Be more then 4 chars')
                return redirect('/contact')    

        return render(request, 'frontend/contact.html')

def Attractive(request):
    attractiondata = Attractive_location.objects.all()
    context = {'attractiondata':attractiondata}
    return render(request, 'frontend/attractive.html',context )

def Project(request):
    Projects = Project_publisher.objects.all()
    context = {'Projects':Projects}
    return render(request, 'frontend/project.html', context)

def Project_details(request, slug):
    Projects = Project_publisher.objects.all()
    projectdata = Project_publisher.objects.select_related('Service_publisher_id').select_related('category_id').filter(slug = slug)
    context = {'projectdata':projectdata, 'Projects':Projects}
    return render(request, 'frontend/project-details.html', context)

def Service_details(request, slug):
    service = Service_publisher.objects.get(slug=slug)
    context = {'service':service}
    return render(request, 'frontend/service-details.html', context)

def Single(request, slug):
    home = Home.objects.all()
    singlepost = Post.objects.select_related('category_id').select_related('author').filter(slug = slug)
    for x in singlepost:
        x.read_count = x.read_count + 1
        x.save()
    popularpost = Post.objects.all().order_by('-read_count')[:8]
    category = Category.objects.all().order_by('id')[:8]
    if request.method == 'POST':
        post = x.id
        body = request.POST.get('body')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        try:
            # id integer e.g. 15
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        # if parent_id has been submitted get parent_obj id
        # if parent_id:
        #     parent_obj = Comment.objects.get(id=parent_id)
        #     # if parent object exist
        #     if parent_obj:
        #         # create replay comment object
        #         replay_comment = comment_form.save(commit=False)
        #         # assign parent_obj to replay comment
        #         replay_comment.parent = parent_obj
        new_comment = Comment(
            post=post, body=body, name=name, email=email, phone=phone, subject=subject)
        new_comment.save()
        messages.success(request, 'Comment Submitted successfully')
    comments = Comment.objects.filter(post=x.id)
    category = Category.objects.all().order_by('id')[:8]
    context = {'home':home,'singlepost':singlepost,'category':category, 'comments':comments, 'popularpost':popularpost, }
    return render(request, 'frontend/blog-details.html', context)

def Ser(request):
    return render(request, 'frontend/ser.html')

def Recentproject(request):
    Ongoingprojects = Ongoingproject.objects.all()[:20]
    context = {'Ongoingprojects':Ongoingprojects}
    return render(request, 'frontend/recent-projects.html', context)

def Search(request):
    if request.method == 'GET':
      query = request.GET['query']
      posts = Post.objects.filter(title__icontains = query)
      context = {'posts':posts}
      print(posts)
      if not posts.exists():
         messages.error(request, 'No data Found')
         return render(request, 'frontend/search.html', context)
    return render(request, 'frontend/search.html', context)