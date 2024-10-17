from django.contrib import admin

from museum.models import EmployeePost, Employee, FormOfArt, Author, Hall, Exposition, Exhibit, Excursion

class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_creation', 'author', 'employee', 'exposition', 'form')
    list_filter = ('exposition', 'form')


admin.site.register(EmployeePost)
admin.site.register(Employee)
admin.site.register(FormOfArt)
admin.site.register(Author)
admin.site.register(Hall)
admin.site.register(Exposition)
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Excursion)


