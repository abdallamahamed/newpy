from django.db import models

# Create your models here.
# pcources data.

class category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class cources(models.Model):
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()
    img5 = models.ImageField()
    name = models.CharField(max_length=100)
    Descriptiontital = models.CharField(max_length=100)
    Description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    Status =models.CharField(max_length=100)
    teacher =models.CharField(max_length=100)
    location =models.CharField(max_length=100)
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

# posts data
class postcategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class post(models.Model):
    post_img = models.ImageField()
    post_name =models.CharField(max_length=100)
    post_tital =models.CharField(max_length=100)
    post = models.TextField()
    date_published=models.DateTimeField(auto_now_add=True)
    written_by =models.CharField(max_length=50)
    great_name =models.CharField(max_length=50)
    category=models.ForeignKey(postcategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.post_name


#home page models
class home_interface(models.Model):
    profile_name = models.CharField(max_length=100)
    profile_image = models.ImageField()
    name_tital = models.CharField(max_length=100)
    recidence = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    list_profile_1 = models.CharField(max_length=100)
    list_profile_2 = models.CharField(max_length=100)
    list_profile_3 = models.CharField(max_length=100)
    list_profile_4 = models.CharField(max_length=100)
    welcoming = models.CharField(max_length=100)
    welcom_name = models.CharField(max_length=100)
    Years_Experience = models.CharField(max_length=100)
    Completed_Projects = models.CharField(max_length=100)
    Happy_Customers = models.CharField(max_length=100)
    Awards = models.CharField(max_length=100)
    def __str__(self):
        return self.profile_name


# Price_Plans
class Price_Plans(models.Model):
    free_price_1 = models.CharField(max_length=100)
    free_price_2 = models.CharField(max_length=100)
    free_price_3 = models.CharField(max_length=100)
    free_price_4 = models.CharField(max_length=100)
    medium_price_5 = models.CharField(max_length=100)
    medium_price_1 = models.CharField(max_length=100)
    medium_price_2 = models.CharField(max_length=100)
    medium_price_3 = models.CharField(max_length=100)
    medium_price_4 = models.CharField(max_length=100)
    medium_price_5 = models.CharField(max_length=100)
    high_price_1 = models.CharField(max_length=100)
    high_price_2 = models.CharField(max_length=100)
    high_price_3 = models.CharField(max_length=100)
    high_price_4 = models.CharField(max_length=100)
    high_price_5 = models.CharField(max_length=100)
    def __str__(self):
        return self.free_price_1
    
#Recommendations

class Recommendations(models.Model):
    name = models.CharField(max_length=100)
    name_tita= models.CharField(max_length=100)
    name_text= models.TextField()
    name_image = models.ImageField()
    def __str__(self):
        return self.name

#home page models end

#cotact page models 

class contact_information(models.Model):
    Countery = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Streat= models.CharField(max_length=50)
    Email= models.CharField(max_length=50)
    Facebook= models.CharField(max_length=50)
    Telegram= models.CharField(max_length=50)
    spurt_sevice= models.CharField(max_length=50)
    ofice= models.CharField(max_length=50)
    personal= models.CharField(max_length=50)
    def __str__(self):
        return self.City
    
class contact_data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.email
    


class my_contact(models.Model):
    magac = models.CharField(max_length=100)
    iimel = models.EmailField(max_length=100)
    number = models.CharField(max_length=100)
    fikrad = models.TextField()
    def __str__(self):
        return self.magac

# history models



class educational_history(models.Model):
    tital = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    sub_tital = models.CharField(max_length=100)
    information = models.TextField()
    def __str__(self):
        return self.tital
    
class work_history(models.Model):
    tital = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    sub_tital = models.CharField(max_length=100)
    information = models.TextField()
    def __str__(self):
        return self.tital