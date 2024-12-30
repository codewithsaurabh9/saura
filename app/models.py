from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.
class first_display(models.Model):
    firstimage = models.ImageField(upload_to="profile" ,blank=True)
    displayname = models.CharField(max_length=150)
    nametitle = models.CharField(max_length=150)





class about(models.Model):
    aboutphoto = models.ImageField(upload_to="about/profile", blank=True)
    aboutheadline = models.CharField(max_length=150)

    aboutdetail = models.CharField(max_length=150 ,)
    # gender = models.CharField(max_length=150)
    # language = models.CharField(max_length=150)
    # work = models.CharField(max_length=150)
    
    
    # freelance = models.CharField(max_length=150)
    # freelance_project = models.CharField(max_length=150,blank=True)

    # freelance_num = models.CharField(max_length=150)
    
    
    
    # Experience = models.CharField(max_length=150)
    # Projects_Completed = models.CharField(max_length=150)
    # Happy_Clients = models.CharField(max_length=150)
    # Awards_Won = models.CharField(max_length=150)
    # age = models.CharField(max_length=150)
    

class aboutproject(models.Model): 
    icon = models.CharField(max_length=150,blank=True)


    num = models.IntegerField(max_length=150,blank=True)

    name = models.CharField(max_length=150,blank=True)
    detail = models.CharField(max_length=150,blank=True)




        #  My Skills
class My_Skills(models.Model):    
    Skillsdetail = models.CharField(max_length=150,blank=True)


class My_Skills1(models.Model):    
    MySkills = models.CharField(max_length=150,blank=True)
    percent = models.CharField(max_length=150,blank=True)
    width_percent = models.CharField(max_length=150,blank=True)

    
class My_Skills2(models.Model):    
    MySkills = models.CharField(max_length=150,blank=True)
    percent = models.CharField(max_length=150,blank=True)
    width_percent = models.CharField(max_length=150,blank=True)






class Resume(models.Model): 
    Resumedetail = models.CharField(max_length=150,blank=True)
   



                            # Qualification

class education(models.Model):    
    education_date = models.CharField(max_length=150,blank=True)
    education_name = models.CharField(max_length=150,blank=True)
    education_detail = RichTextField()
    # education_detail = models.CharField(max_length=150,blank=True)



#                             # Qualification experience


class experience(models.Model):    
    # experience_date = models.CharField(max_length=150,blank=True)
    # experience_name = models.CharField(max_length=150,blank=True)
    # experience_detail = models.CharField(max_length=150,blank=True)
    experience_detail = RichTextField()



                        # My 

class Services(models.Model): 
    Services_detail = models.CharField(max_length=150,blank=True)                        
                         

class MyServices(models.Model):    
    Servicespng = models.CharField(max_length=150,blank=True) 
    Services_name = models.CharField(max_length=150,blank=True)                        
    Services_detail = models.CharField(max_length=150,blank=True)                        
    


                        # My Portfolio

class Portfolio(models.Model): 
    Portfoliodetail = models.CharField(max_length=150,blank=True) 


class PortfolioCategory(models.Model): 
    Category_name = models.CharField(max_length=150,blank=True) 
    slug = AutoSlugField(populate_from='Category_name',unique=True, null=True,default=None)

    def __str__(self):
        return self.Category_name



class MyPortfolio(models.Model):    
    slug = AutoSlugField(populate_from='category',unique=True, null=True,default=None)

    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    Portfolio = models.ImageField(upload_to="Services/png")

    Services_name = models.CharField(max_length=150,blank=True) 







                        # Testimonials









                        # My Blog


















                        # Contact Me


# class contact_info(models.Model):
#     GetInTouch = models.CharField(max_length=100,blank=True) 
#     detail = models.CharField(max_length=100,blank=True) 


# class Contact_detail(models.Model):
#     name = models.CharField(max_length=100,blank=True) 
#     Contacticon = models.CharField(max_length=150,blank=True)  
#     Contact_social_mob = models.CharField(max_length=150,blank=True)  
#     Contactiadd = models.CharField(max_length=150,blank=True)  




#                         # Contact us

class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)







#                         # social media

# class social_media(models.Model):
#     social_icon = models.CharField(max_length=100,blank=True) 
#     social_media_link = models.CharField(max_length=150,blank=True) 




# class file(models.Model):
#     pdf = models.FileField(upload_to='staticmedia')

