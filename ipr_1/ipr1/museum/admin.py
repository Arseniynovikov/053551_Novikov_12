from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from museum.models import EmployeePost, Employee, FormOfArt, Author, Hall, Exposition, Exhibit, Excursion
from museum.views import expositions


class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_creation', 'author', 'employee', 'exposition', 'form')
    list_filter = ('exposition', 'form')

class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'square')
    list_filter = ('floor', )

class ExpositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'hall')
    list_filter = ('hall',)

class ExpositionFilter(SimpleListFilter):
    title = 'Expositions'
    parameter_name = 'expositions'

    def lookups(self, request, model_admin):
        return [(exposition.id, exposition.name) for exposition in Exposition.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(exposition__id=self.value())
        return queryset


class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_time', 'employee', 'get_expositions')
    list_filter =  ('employee', ExpositionFilter)

    def get_expositions(self, obj):
        return ", ".join([exposition.name for exposition in obj.exposition.all()])
    get_expositions.short_description = "Expositions"


class EmployeePostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'date_of_birth')

admin.site.register(EmployeePost, EmployeePostAdmin)
admin.site.register(Employee)
admin.site.register(FormOfArt)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Exposition, ExpositionAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Excursion, ExcursionAdmin)


