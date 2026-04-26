from django.shortcuts import render
from apps.home.models import*
# Create your views here.



def uon_alumni_history(request):
    return render(request, 'home/uon_alumni_history.html')


def uon_alumni_core(request):
    return render(request, 'home/uon_alumni_core.html')


def uon_alumni_exec_committee(request):
    executives = Executive.objects.all().order_by('rank')

    
    context = {
        "executives": executives,

    }
    # print(treasurer)
    return render(request, 'home/uon_alumni_exec_committee.html', context)


def uon_alumni_secretariat(request):
    
    secretariats = Secretariat.objects.all().order_by('rank')

    context = {
        "secretariats": secretariats,
    }
    return render(request, 'home/uon_alumni_secretariat.html', context)


def uon_alumni_notable(request):
    return render(request, 'home/uon_alumni_notable.html')


def uon_alumni_walk(request):
    # ads = Ad.objects.all()

    context =  {
        # "ads": ads,
    }
    return render(request, 'home/uon_alumni_walk.html', context)



def uon_alumni_chapters(request):
    # chapters = Chapter.objects.all().order_by('-year_launched')
    context = {
        # "chapters": chapters
    }
    return render(request, 'home/uon_alumni_chapters.html', context)


def uon_alumni_partners(request):
    # partners = Partner.objects.all().order_by('created_at')

    context = {
        # "partners": partners
    }
    return render(request, 'home/uon_alumni_partners.html', context)


def uon_alumni_register(request):
    return render(request, 'home/uon_alumni_register.html')


def uon_alumni_agm(request):
    return render(request, 'home/uon_alumni_agm.html')


def uon_alumni_consultancy_training(request):
    return render(request, 'home/uon_alumni_consultancy_training.html')


def uon_alumni_donate(request):
    return render(request, 'home/uon_alumni_donate.html')


def uon_alumni_scholarship(request):
    return render(request, 'home/uon_alumni_scholarship.html')


def uon_alumni_downloads(request):
    return render(request, 'home/uon_alumni_downloads.html')


def uon_alumni_gallery(request):
    return render(request, 'home/uon_alumni_gallery.html')


def uon_alumni_shop(request):
    return render(request, 'home/uon_alumni_shop.html')

def uon_alumni_contact_us(request):
    return render(request, 'home/uon_alumni_contact_us.html')