from django import forms
from .models import Student
from .models import Department
from .models import Subject
from .models import Hod
from .models import Faculty
from .models import Person
from .models import State
from .models import Dist

class stud(forms.ModelForm):
    class Meta:
     model=Student
     fields='__all__'
    
class dep(forms.ModelForm):
   class Meta:
      model=Department
      fields='__all__'

class sub(forms.ModelForm):
   class meta:
      model=Subject
      fields='__all__'

class hod(forms.ModelForm):
   class meta:
      model=Hod
      fields='__all__'

class faculty(forms.ModelForm):
   class meta:
      model=Faculty
      fields='__all__'

class Person(forms.ModelForm):
   class meta:
      model=Person
      fields='__all__'

class State(forms.ModelForm):
   class meta:
      model=State
      fields='__all__'

class Dist(forms.ModelForm):
   class meta:
      model=Dist
      fields='__all__'

