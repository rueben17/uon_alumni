from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from functools import reduce
from operator import or_
from django.views.generic import ListView
from django.contrib import messages
import random
from datetime import datetime
from apps.home.models import (
    Article, Chapter, Faculty, CoreValue, Executive, Secretariat, Images,
    MembershipTier, Banner
)
from apps.home.forms import AlumniRegistrationForm
# Create your views here.



def uon_alumni_home(request):
    articles = Article.objects.all().order_by('-date_updated')[:6]
    # ads = Ad.objects.all()
    
    featured_articles = Article.objects.filter(is_feature=True).order_by('-created_at')[:1]
    highlighted_articles = Article.objects.filter(is_highlighted=True).order_by('-created_at')[:6]
    
    context = {
        "articles": articles,
        "featured_articles": featured_articles,
        "highlighted_articles": highlighted_articles,
        # "ads": ads
    }
    return render(request, "home/alumni_home.html", context)


def uon_alumni_history(request):
    return render(request, 'home/uon_alumni_history.html')


def uon_alumni_gallery(request):
    images = Images.objects.all().order_by('-created_at')[:38]

    context = {
        "images": images,
        # "ads": ads
    }
    return render(request, 'home/uon_alumni_gallery.html', context)

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
    
    faculty = None
    if faculty_slug:
        faculty = get_object_or_404(Faculty, slug=faculty_slug)

    context = {
        "chapter": chapter,
        "faculty": faculty,
    }
    return render(request, 'home/uon_alumni_chapter_detail.html', context)





def uon_alumni_partners(request):
    # partners = Partner.objects.all().order_by('created_at')

    context = {
        # "partners": partners
    }
    return render(request, 'home/uon_alumni_partners.html', context)


def uon_alumni_register(request):
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST)
        if form.is_valid():
            alumni = form.save(commit=False)
            # Payment integration will go here later
            alumni.save()
            messages.success(request, 'Registration successful! Complete your payment to activate membership.')
            return redirect('home:uon_alumni_register')
    else:
        form = AlumniRegistrationForm()

    context = {
        'form': form,
        'membership_tiers': MembershipTier.objects.filter(is_active=True),
    }
    return render(request, 'home/uon_alumni_register.html', context)



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





def uon_alumni_shop(request):
    return render(request, 'home/uon_alumni_shop.html')

def uon_alumni_contact_us(request):
    return render(request, 'home/uon_alumni_contact_us.html')



def date_timer(request):
    date = datetime.now().strftime(" %B %d, %Y at %I:%M%p ")
    context = {"date": date,}
    return render(request, 'snippets/date_time.html', context)



BLOG_POSTS_PER_PAGE = 6

def get_articles_queryset(query=None):
    if query is None:
        return Article.objects.none()

    queries = query.split(" ")
    query_filter = reduce(or_, (Q(title__icontains=q) | Q(body__icontains=q) for q in queries))
    return Article.objects.filter(query_filter).order_by('-date_updated').distinct()


def uon_alumni_all_news(request, *args, **kwargs):
    query = request.GET.get('q', '')
    articles_qs = get_articles_queryset(query)
    
    page = request.GET.get('page', 1) 
    blog_posts_paginator = Paginator(articles_qs, BLOG_POSTS_PER_PAGE)
    
    try:
        articles = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        articles = blog_posts_paginator.page(1)
    except EmptyPage:
        articles = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context = {
        "articles": articles,
        "page_obj": articles,  
        "query": query or ""
    }
    return render(request, 'home/uon_alumni_all_news.html', context)


def uon_alumni_article_detail(request, article_slug=None):
    article = get_object_or_404(Article, slug=article_slug)
    
    # Get related articles from the same chapter if chapter exists
    similar_articles = []
    related_articles = []
    if article.chapter:
        random_chapter_articles = list(article.chapter.articles.exclude(id=article.id))
        similar_articles = random.sample(random_chapter_articles, min(4, len(random_chapter_articles)))
        related_articles = random_chapter_articles[:5]
    
    images = article.images.all()
    context = {
        "article": article,
        "similar_articles": similar_articles,
        "related_articles": related_articles,
        "images": images,
    }
    return render(request, 'home/uon_alumni_article_detail.html', context)
