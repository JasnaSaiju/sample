from django.contrib import admin


# Register your models here.
from .models import Student
admin.site.register(Student)

from .models import Department
admin.site.register(Department)

from .models import Hod
admin.site.register(Hod)

from .models import Subject
admin.site.register(Subject)

from .models import Faculty
admin.site.register(Faculty)

from .models import Person,State,Dist
admin.site.register(Person)
admin.site.register(State)
admin.site.register(Dist)
