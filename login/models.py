from django.db import models
class userlogin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    rpassword=models.CharField(max_length=200,default=password)
    def __str__(self) :
      return self.username;

class Userdetail(models.Model):
    username=models.CharField(default="darshu",max_length=200)
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    cweight=models.FloatField()
    dweight=models.FloatField()
    height=models.FloatField()
    birthday=models.DateField()
    city=models.CharField(max_length=200)
    pincode=models.IntegerField()
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    dateofjoining=models.DateField()
    trainer=models.CharField(max_length=200)
    gymbefore=models.CharField(max_length=200)
    membership=models.CharField(max_length=200)
    def __str__(self):
        return self.firstName;
def filepath(filename):
    oldname=filename;
class Trainer(models.Model):
    FullName=models.CharField(max_length=200);
    Pic=models.ImageField(upload_to='pictures');
    Email=models.EmailField();
    Contact=models.IntegerField();
    JoinDate=models.DateField();
    BirthDate=models.DateField();
    Status=models.CharField(default="Active",max_length=20);
    def __str__(self):
        return self.FullName;
class Package(models.Model):
      PackageName=models.CharField(max_length=200);
      Pic=models.ImageField(upload_to='pictures');
      Price=models.IntegerField();
      Details=models.CharField(max_length=200);
      def __str__(self):
          return self.PackageName;
