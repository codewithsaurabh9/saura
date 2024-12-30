from django.shortcuts import render

# Create your views here.
from .models import first_display,about,aboutproject,My_Skills,My_Skills2,My_Skills1,Resume,Services,MyServices,MyPortfolio,PortfolioCategory,MyPortfolio,education,experience,Contact_us             
from django.contrib import messages


def index1(request):
    if request.method =="POST":
        contact =Contact_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
                )
        contact.save()
        messages.success(request, 'Subscription Successful')




    dis = first_display.objects.all()

    abo = about.objects.all()
    
    abopro = aboutproject.objects.all()
    skills = My_Skills.objects.all()
    Skills1 = My_Skills1.objects.all()
    Skills2 = My_Skills2.objects.all()
    resume = Resume.objects.all()
    Education = education.objects.all()

    Experience = experience.objects.all()
    services = Services.objects.all()
    myservices = MyServices.objects.all()
    Portfolio = MyPortfolio.objects.all()
    category = PortfolioCategory.objects.all()
    category = PortfolioCategory.objects.get()
    categoryId = request.GET.get('category')
    if categoryId:
        Products = MyPortfolio.objects.filter(category = categoryId)
    else:
        Products = MyPortfolio.objects.all()    
    
   
    # myPortfolio = MyPortfolio.objects.all()
    # myservices = MyServices.objects.all()
    # Contact_info = contact_info.objects.all()
    # contact_detail = Contact_detail.objects.all()
    # Social_media = social_media.objects.all()
    # abo = about.objects.all()
   
    # category = Category.objects.all()
    # categoryId = request.GET.get('category')
    # if categoryId:
    #     Products = MyPortfolio.objects.filter(category = categoryId)
    # else:
    #     Products = MyPortfolio.objects.all()    
    auto1 = {
        'dis': dis,
        'abo': abo,
        'abopro': abopro,
        'skills': skills,
        'Skills2': Skills2,
        'Skills1': Skills1,
        'resume' : resume,
        'services' : services,
        'Portfolio' : Portfolio,
        # 'resume' : resume,
        'category':category,
        'Products':Products,
        'myservices':myservices,

        'Education':Education,
        'Experience':Experience,
        # 'Contact_info':Contact_info,
        # 'contact_detail':contact_detail,
        # 'Social_media':Social_media,
        # 'okk':okk,
        # 'contact_detail':contact_detail,
    }

    return render(request,'index.html',auto1)




# def base(request):
#     dis = first_display.objects.all()
#     auto1 = {
#         'dis': dis,
#        }
    
#     return render(request,'base.html',auto1)




# def appp(request):

#     # print(slug)
#     # Portfolio = MyPortfolio.objects.all()
#     category = PortfolioCategory.objects.all()
#     categoryId = request.GET.get('category')
#     if categoryId:
#         Products = MyPortfolio.objects.filter(category = categoryId)
#     else:
#         Products = MyPortfolio.objects.all()    
#     auto1 = {
#         # category
#         'category':category,
#         'Products':Products,
#         # 'Portfolio':Portfolio,
#     }


#     return render(request,'index.html',auto1)


def index(request):
    if request.method =="POST":
        contact =Contact_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
                )
        contact.save()
        messages.success(request, 'Subscription Successful')




    dis = first_display.objects.all()

    abo = about.objects.all()
    
    abopro = aboutproject.objects.all()
    skills = My_Skills.objects.all()
    Skills1 = My_Skills1.objects.all()
    Skills2 = My_Skills2.objects.all()
    resume = Resume.objects.all()
    Education = education.objects.all()

    Experience = experience.objects.all()
    services = Services.objects.all()
    myservices = MyServices.objects.all()
    Portfolio = MyPortfolio.objects.all()
    category = PortfolioCategory.objects.all()
    # category = PortfolioCategory.objects.get(id=slug)
    # Products = MyPortfolio.objects.filter(category = categoryId)

    categoryId = request.GET.get('category')
    if categoryId:
        Products = MyPortfolio.objects.filter(category = categoryId)
    else:
        Products = MyPortfolio.objects.all()    
    
   
    # myPortfolio = MyPortfolio.objects.all()
    # myservices = MyServices.objects.all()
    # Contact_info = contact_info.objects.all()
    # contact_detail = Contact_detail.objects.all()
    # Social_media = social_media.objects.all()
    # abo = about.objects.all()
   
    # category = Category.objects.all()
    # categoryId = request.GET.get('category')
    # if categoryId:
    #     Products = MyPortfolio.objects.filter(category = categoryId)
    # else:
    #     Products = MyPortfolio.objects.all()    
    auto1 = {
        'dis': dis,
        'abo': abo,
        'abopro': abopro,
        'skills': skills,
        'Skills2': Skills2,
        'Skills1': Skills1,
        'resume' : resume,
        'services' : services,
        'Portfolio' : Portfolio,
        # 'resume' : resume,
        'category':category,
        'Products':Products,
        'myservices':myservices,

        'Education':Education,
        'Experience':Experience,
        # 'Contact_info':Contact_info,
        # 'contact_detail':contact_detail,
        # 'Social_media':Social_media,
        # 'okk':okk,
        # 'contact_detail':contact_detail,
    }

    return render(request,'index.html',auto1)


