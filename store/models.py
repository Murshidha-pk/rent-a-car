from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=10,unique=True)

    is_verified=models.BooleanField(default=False)

    otp=models.CharField(max_length=6,null=True,blank=True)


class BaseModel(models.Model):

    creaed_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=False)

class Brand(BaseModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Category(BaseModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BodyType(BaseModel):

    name=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Car(BaseModel):

    title=models.CharField(max_length=200)

    category_object=models.ForeignKey(Category,on_delete=models.CASCADE)

    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE)

    body=models.ForeignKey(BodyType,on_delete=models.CASCADE)

    year=models.PositiveIntegerField()

    CONDITION_CHOICES=(
        ("New","New"),
        ("Used","Used"),
    )

    condition=models.CharField(max_length=20,choices=CONDITION_CHOICES,default="used")

    gear_type=models.CharField(max_length=100)

    fuel_choices=(
        ("petrol","Petrol"),
        ("diesel","Diesel"),
        ("Electric","Electric"),
        ("Hybrid","Hybrid")
    )

    fuel_type=models.CharField(max_length=100,choices=fuel_choices,default="petrol")

    mileage=models.CharField(max_length=200)

    color=models.CharField(max_length=100)

    seats=models.PositiveIntegerField()

    picture=models.ImageField(upload_to="car_images",null=True,blank=True)

    price_per_day=models.DecimalField(max_digits=10,decimal_places=2)

    price_per_week=models.DecimalField(max_digits=10,decimal_places=2)

    price_per_month=models.DecimalField(max_digits=10,decimal_places=2)

    free_km_per_day=models.PositiveIntegerField(default=250)

    availability=models.BooleanField(default=True)

    vehicle_no=models.CharField(max_length=100,unique=True)

    description=models.TextField()





