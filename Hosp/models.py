from django.db import models

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=16)
	repassword = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)

	
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Doctor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=16)
	repassword = models.CharField(max_length=16,default="temp")
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)
	specialization = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Appointment(models.Model):
	doctorname = models.CharField(max_length=50)
	patientname = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	patientemail = models.EmailField(max_length=50)
	appointmentdate = models.DateField(max_length=10)
	appointmenttime = models.TimeField(max_length=10)
	symptoms = models.CharField(max_length=100)
	status = models.BooleanField()
	
	gender = models.CharField(max_length=16,default="Male")
	def __str__(self):
		return self.username+" you have appointment with "+self.doctorname



class Prescription(models.Model):
	appid= models.IntegerField(max_length=50,default="null")
	name = models.CharField(max_length=50)
	age = models.CharField(max_length=10)
	weight = models.CharField(max_length=10)
	bp = models.CharField(max_length=50)
	phonenuumber = models.CharField(max_length=10)
	city = models.CharField(max_length=50)
	medname = models.CharField(max_length=50)
	medmg = models.CharField(max_length=50)
	dose = models.CharField(max_length=50)
	comment = models.CharField(max_length=200)
	gender = models.CharField(max_length=50)