from . models import Settings


def Sapphire_Settings(request):
    settings = Settings.objects.all()
    return {'settings' : settings}