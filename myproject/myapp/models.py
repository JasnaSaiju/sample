from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=15)
    Age=models.IntegerField()
    Email=models.EmailField(max_length=20)
    class Meta:
        db_table='Student'

    def __str__(self):
        return self.Name
    
class Department(models.Model):
    name=models.CharField(max_length=50)
    class Meta:
         db_table='Dep'

    def __str__(self):
        return self.name
    
class Hod(models.Model):
    name=models.CharField(max_length=50)
    class Meta:
         db_table='Hod'

    def __str__(self):
         return self.name
    
department=models.OneToOneField(Department,on_delete=models.CASCADE,related_name='hod')
def __str__(self):
        return f"{self.name}-{self.department.name}"

class Subject(models.Model):
     name=models.CharField(max_length=50)

     class Meta:
          db_table='Sub'
     def __str__(self):
          return self.name
     
class Faculty(models.Model):
     name=models.CharField(max_length=50)

     class Meta:
          db_table='Faculty'
     def __str__(self):
          return self.name

     department_name=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='Faculties')
     subjects=models.ManyToManyField(Subject,related_name='Faculties')
     def __str__(self):
          return f"{self.name}-{self.department_name.name}"
     

class Person(models.Model):
     name=models.CharField(max_length=15)
     age=models.IntegerField()

     class meta:
          db_table='Person'
          def __str__(self):
               return self.name
          
class State(models.Model):
          state_name=models.CharField(max_length=25)
          def __str__(self):
               return self.state_name
          class meta:
               db_table='State'
     
class Dist(models.Model):
          dist_name=models.CharField(max_length=25)
          state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='districts')
          def __str__(self):
               return self.dist_name
          class meta:
               db_table='Dist'
               
