from settings.models import Info



def get_footer(request):
    myfooter = Info.objects.last()
    return {'myfooter': myfooter}