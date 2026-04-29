from django.shortcuts import render, redirect, get_object_or_404
from apps.home.models import*
from django.views.generic import ListView
# Create your views here.



def uon_alumni_home(request):
    articles = Article.objects.all().order_by('-date_updated')[:6]
    # ads = Ad.objects.all()
    images = Images.objects.all().order_by('-created_at')[:19]
    featured_articles = Article.objects.filter(is_feature=True).order_by('-created_at')[:1]
    highlighted_articles = Article.objects.filter(is_highlighted=True).order_by('-created_at')[:6]
    
    context = {
        "articles": articles,
        "featured_articles": featured_articles,
        "highlighted_articles": highlighted_articles,
        "images": images,
        # "ads": ads
    }
    return render(request, "home/alumni_home.html", context)


def uon_alumni_history(request):
    return render(request, 'home/uon_alumni_history.html')


# def uon_alumni_core(request):
#     return render(request, 'home/uon_alumni_core.html')


class CoreValuesListView(ListView):
    model = CoreValue
    template_name = 'home/uon_alumni_core.html'  # Update with your template path
    context_object_name = 'core_values'
    paginate_by = 12  # Optional: paginate if needed
    
    def get_queryset(self):
        return CoreValue.objects.filter(is_active=True).order_by('order')


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
    chapters = Chapter.objects.all().order_by('-year_launched')
    context = {
        "chapters": chapters
    }
    return render(request, 'home/uon_alumni_chapters.html', context)


def uon_alumni_chapter_detail(request, chapter_slug=None, faculty_slug=None):
    chapter = get_object_or_404(Chapter, slug=chapter_slug)
    
    if faculty_slug:
        faculty = get_object_or_404(Faculty, slug=faculty_slug)

    context = {
        "chapter": chapter,
    }
    return render(request, 'home/uon_alumni_chapter_detail.html', context)





def uon_alumni_partners(request):
    # partners = Partner.objects.all().order_by('created_at')

    context = {
        # "partners": partners
    }
    return render(request, 'home/uon_alumni_partners.html', context)


def uon_alumni_register(request):
    return render(request, 'home/uon_alumni_register.html')



def uon_alumni_categories_benefits(request):
    return render(request, 'home/uon_alumni_categories_benefits.html')


def uon_alumni_agm(request):
    return render(request, 'home/uon_alumni_agm.html')


def uon_alumni_consultancy_training(request):
    articles = Article.objects.filter(article_type__in=['training', 'workshop', 'conference'])
    
    return render(request, 'home/uon_alumni_consultancy_training.html', {'articles': articles})


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



#Membership views

