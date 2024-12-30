from django.contrib import admin
    # Register your models here.
from .models import first_display,about,aboutproject,My_Skills,My_Skills1,My_Skills2,Resume,Services,MyServices,MyPortfolio,PortfolioCategory,Portfolio,education,experience,Contact_us             
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Category_name', )
    
#  list_display = ('id', 'first_name', 'last_name', 'Country', 'address', 'city',
#                     'state', 'postcode', 'phone', 'email', 'additional_info', 'amount', 'payment_id',)
    


class first_displayAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstimage','displayname','nametitle' )
admin.site.register(first_display, first_displayAdmin)

class aboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'aboutphoto','aboutheadline','aboutdetail' )

admin.site.register(about,aboutAdmin)


class aboutprojectAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon','num','name','detail' )

admin.site.register(aboutproject,aboutprojectAdmin)


class My_SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Skillsdetail' )

admin.site.register(My_Skills,My_SkillsAdmin)


class My_Skills1Admin(admin.ModelAdmin):
    list_display = ('id', 'MySkills','percent','width_percent' )

admin.site.register(My_Skills1,My_Skills1Admin)


class My_Skills2Admin(admin.ModelAdmin):
    list_display = ('id', 'MySkills','percent','width_percent' )


admin.site.register(My_Skills2,My_Skills2Admin)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'Resumedetail', )

admin.site.register(Resume,ResumeAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Services_detail', )

admin.site.register(Services,ServicesAdmin)

class MyServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Servicespng','Services_name','Services_detail' )

admin.site.register(MyServices,MyServicesAdmin)

class MyPortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug','category','Portfolio', 'Services_name' )

admin.site.register(MyPortfolio,MyPortfolioAdmin)


admin.site.register(PortfolioCategory ,PortfolioCategoryAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'Portfoliodetail',)

admin.site.register(Portfolio,PortfolioAdmin)

class educationAdmin(admin.ModelAdmin):
    list_display = ('id', 'education_date','education_name','education_detail' )

admin.site.register(education,educationAdmin)


class experienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'experience_detail',)

admin.site.register(experience,experienceAdmin)


class Contact_usAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','message' )

admin.site.register(Contact_us,Contact_usAdmin)
# admin.site.register(first_display)
# admin.site.register(first_display)
# admin.site.register(first_display)
# admin.site.register(first_display)
