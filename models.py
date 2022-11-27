from django.db import models

# Create your models here.


class Employee(models.Model):
    regid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    phoneNo = models.CharField(max_length=10, null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.regid}'


class EmployeeAddress(models.Model):
    emp = models.OneToOneField(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeAddress')
    hno = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.emp.regid} {self.emp.name}'


class EmployeeWorkExperience(models.Model):
    emp = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeWorkExperience')
    companyName = models.CharField(max_length=100,  null=True, blank=True)
    fromDate = models.CharField(max_length=100, null=True, blank=True)
    toDate = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.emp.regid}'


class EmployeeQualification(models.Model):
    emp = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeQualification')
    qualificationName = models.CharField(max_length=100, null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.emp.regid}'


class EmployeeProjects(models.Model):
    emp = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeProjects')
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.emp.regid}'
