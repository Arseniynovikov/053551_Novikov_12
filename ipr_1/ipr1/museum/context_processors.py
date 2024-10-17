from .models import FormOfArt

def forms_context_processor(request):
    forms_list = FormOfArt.objects.all()
    return {'forms_of_art': forms_list}