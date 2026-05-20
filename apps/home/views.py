from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.db.models import Q
from functools import reduce
from operator import or_
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db import transaction
import random
import uuid
from datetime import datetime, date
from apps.home.models import (
    Article, Chapter, Faculty, CoreValue, Executive, Secretariat, Images,
    MembershipTier, Banner, AlumniProfile
)
from apps.home.forms import*
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
    chapters = Chapter.objects.all().order_by('-year_launched')    
    context = {
        "images": images,
        "chapters": chapters,
    }
    return render(request, 'home/uon_alumni_gallery.html', context)


def uon_alumni_gallery_filter(request, chapter_slug=None):
    
    chapters = Chapter.objects.all().order_by('-year_launched')
    if request.htmx:
        chapter = get_object_or_404(Chapter, slug=chapter_slug)
        images = Images.objects.filter(chapter=chapter).order_by('-created_at')
        context = {
            "chapter": chapter,
            "images": images,
        }
        return render(request, 'snippets/chapter_gallery_snippet.html', context)
    else:
        return redirect("home:uon_alumni_gallery")


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
    if request.user.is_authenticated:
        return redirect('home:uon_alumni_profile_creation')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()  # Only creates Django User
            login(request, user)
            messages.success(request, 'Account created successfully! Please complete your profile.')
            return redirect('home:uon_alumni_profile_creation')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'home/uon_alumni_register.html', context)



# @login_required


def uon_alumni_profile_creation(request):
    # Check if profile already exists
    if hasattr(request.user, 'alumni_profile'):
        messages.info(request, 'Profile already exists. Please register for membership.')
        return redirect('home:uon_alumni_register_membership', alumni_id=request.user.alumni_profile.id)
    
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                alumni = form.save(commit=False)
                alumni.user = request.user
                alumni.email = request.user.email
                
                # Generate a unique temporary ID passport number
                if not alumni.id_passport_no:
                    alumni.id_passport_no = f"TEMP_{request.user.id}_{uuid.uuid4().hex[:8]}"
                
                # Set default date of birth if not provided
                if not alumni.date_of_birth:
                    alumni.date_of_birth = date(1956, 1, 1)
                
                # Set default phone if not provided
                if not alumni.phone_mobile:
                    alumni.phone_mobile = '+254700000000'
                
                alumni.save()
                
            messages.success(request, 'Profile completed successfully!')
            return redirect('home:uon_alumni_register_membership', alumni_id=alumni.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Pre-populate form with defaults
        initial_data = {
            'email': request.user.email,
            'first_name': request.user.first_name,
            'surname': request.user.last_name,
            'date_of_birth': date(1956, 1, 1),
            'phone_mobile': '+254700000000',
            'nationality': 'Kenyan',
        }
        form = AlumniRegistrationForm(initial=initial_data)
    
    return render(request, 'home/uon_alumni_profile_creation.html', {'form': form})



# @login_required

@transaction.atomic
def uon_alumni_register_membership(request, alumni_id):
    alumni = get_object_or_404(AlumniProfile, id=alumni_id, user=request.user)
    if hasattr(alumni, 'current_membership') and alumni.current_membership.is_active:
        messages.info(request, "You already have an active membership.")
        return redirect('home:uon_alumni_dashboard')

    if request.method == 'POST':
        form = MembershipPaymentForm(request.POST)
        if form.is_valid():
            selected_tier = form.cleaned_data['membership_tier']
            payment_method = form.cleaned_data['payment_method']

            # Build payment_data dict
            payment_data = {}
            if payment_method == 'mpesa':
                payment_data['mpesa_number'] = form.cleaned_data['mpesa_number']
            elif payment_method == 'credit_card':
                payment_data['card_number'] = form.cleaned_data['card_number']
                payment_data['expiry'] = form.cleaned_data['expiry']
                payment_data['cvv'] = form.cleaned_data['cvv']
                payment_data['card_last4'] = form.cleaned_data['card_number'][-4:] if form.cleaned_data['card_number'] else ''
            elif payment_method == 'bank_transfer':
                payment_data['transaction_ref'] = form.cleaned_data['transaction_ref']
                payment_data['bank_name'] = form.cleaned_data['bank_name']

            success, message, payment = uon_alumni_process_payment(
                alumni=alumni,
                selected_tier=selected_tier,
                payment_method=payment_method,
                request=request,
                payment_data=payment_data
            )

            if success:
                # Assign membership
                membership = alumni.assign_membership_tier(selected_tier)
                # Optionally link payment to membership if your Membership model has a ForeignKey to Payment
                # membership.payment = payment
                # membership.save()

                if payment.payment_status == 'pending_verification':
                    messages.warning(request, f"{message} Your membership will be activated after verification.")
                else:
                    messages.success(request, f"Successfully registered for {selected_tier.name}!")
                return redirect('home:uon_alumni_membership_success', alumni_id=alumni.id)
            else:
                messages.error(request, message)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MembershipPaymentForm()

    tiers = MembershipTier.objects.filter(is_active=True).order_by('order', 'fee')
    return render(request, 'home/membership/register_payment.html', {
        'form': form,
        'alumni': alumni,
        'tiers': tiers,
    })
# def uon_alumni_register_membership(request, alumni_id):
#     alumni = get_object_or_404(AlumniProfile, id=alumni_id, user=request.user)
#     available_tiers = MembershipTier.objects.filter(is_active=True).order_by('order', 'fee')
    
#     if request.method == 'POST':
#         # Get selected tier and payment details
#         tier_id = request.POST.get('membership_tier')
#         payment_method = request.POST.get('payment_method')
        
#         # Validate tier selection
#         if not tier_id:
#             messages.error(request, 'Please select a membership tier.')
#             return render(request, 'membership/register_payment.html', {
#                 'alumni': alumni,
#                 'tiers': available_tiers,
#                 'current_membership': alumni.current_membership_tier
#             })
        
#         try:
#             selected_tier = MembershipTier.objects.get(id=tier_id, is_active=True)
#         except MembershipTier.DoesNotExist:
#             messages.error(request, 'Invalid membership tier selected.')
#             return render(request, 'membership/register_payment.html', {
#                 'alumni': alumni,
#                 'tiers': available_tiers,
#                 'current_membership': alumni.current_membership_tier
#             })
        
#         # Process payment and membership
#         payment_successful, payment_message = uon_alumni_simulate_payment_processing(
#             alumni=alumni,
#             amount=selected_tier.fee,
#             payment_method=payment_method,
#             request=request
#         )
        
#         if payment_successful:
#             # Assign membership
#             alumni.assign_membership_tier(selected_tier)
            
#             messages.success(
#                 request, 
#                 f'Successfully registered for {selected_tier.name}! Your membership is now active.'
#             )
#             return redirect('home:uon_alumni_membership_success', alumni_id=alumni.id)
#         else:
#             messages.error(request, f'Payment failed: {payment_message}. Please try again.')
    
#     return render(request, 'home/membership/register_payment.html', {
#         'alumni': alumni,
#         'tiers': available_tiers,
#         'current_membership': alumni.current_membership_tier
#     })



# def uon_alumni_simulate_payment_processing(alumni, amount, payment_method, request):
#     """
#     Process payment based on selected method.
#     Returns (success: bool, message: str)
#     """
    
#     if payment_method == 'mpesa':
#         mpesa_number = request.POST.get('mpesa_number', '')
        
#         # Validate M-Pesa number
#         if not mpesa_number or len(mpesa_number) < 10:
#             return False, "Invalid M-Pesa number. Please enter a valid phone number."
        
#         # Simulate M-Pesa STK push
#         print(f"[M-Pesa] Sending STK push to {mpesa_number} for KES {amount}")
#         print(f"[M-Pesa] Payment for {alumni.full_name} - Amount: KES {amount}")
        
#         # Simulate successful payment
#         payment_ref = f"MPESA_{datetime.now().strftime('%Y%m%d%H%M%S')}_{alumni.id}"
        
#         # Store payment record (if you have a Payment model)
#         # Payment.objects.create(
#         #     alumni=alumni,
#         #     amount=amount,
#         #     method='MPESA',
#         #     reference=payment_ref,
#         #     status='COMPLETED'
#         # )
        
#         return True, "Payment processed successfully"
    
#     elif payment_method == 'credit_card':
#         card_number = request.POST.get('card_number', '')
#         card_expiry = request.POST.get('expiry', '')
#         card_cvv = request.POST.get('cvv', '')
        
#         # Validate card details
#         if not card_number or not card_expiry or not card_cvv:
#             return False, "Please enter complete card details."
        
#         # Basic card validation
#         if len(card_number.replace(' ', '')) < 15:
#             return False, "Invalid card number."
        
#         # Simulate card payment
#         print(f"[Credit Card] Processing payment of KES {amount} for card ending in {card_number[-4:]}")
#         print(f"[Credit Card] Payment for {alumni.full_name} - Amount: KES {amount}")
        
#         payment_ref = f"CC_{datetime.now().strftime('%Y%m%d%H%M%S')}_{alumni.id}"
        
#         return True, "Payment processed successfully"
    
#     elif payment_method == 'bank_transfer':
#         transaction_ref = request.POST.get('transaction_ref', '')
#         bank_name = request.POST.get('bank_name', '')
        
#         if not transaction_ref:
#             return False, "Please enter the transaction reference number."
        
#         # For bank transfers, we'll mark as pending verification
#         print(f"[Bank Transfer] Payment reference: {transaction_ref} from {bank_name}")
#         print(f"[Bank Transfer] Payment for {alumni.full_name} - Amount: KES {amount}")
        
#         # Store pending payment for admin verification
#         # Payment.objects.create(
#         #     alumni=alumni,
#         #     amount=amount,
#         #     method='BANK_TRANSFER',
#         #     reference=transaction_ref,
#         #     status='PENDING_VERIFICATION'
#         # )
        
#         # Don't activate membership yet - wait for admin verification
#         messages.info(request, 'Your bank transfer is pending verification. Your membership will be activated once payment is confirmed.')
#         return True, "Bank transfer recorded successfully"
    
#     else:
#         return False, "Please select a payment method."



def get_tier_details(request):
    tier_id = request.GET.get('membership_tier')
    if tier_id:
        try:
            tier = MembershipTier.objects.get(id=tier_id)
            html = render_to_string('home/membership/_tier_details.html', {'tier': tier})
            return HttpResponse(html)
        except MembershipTier.DoesNotExist:
            pass
    return HttpResponse('<p>Select a membership tier to see details.</p>')




def uon_alumni_membership_success(request, alumni_id):
    alumni = get_object_or_404(AlumniProfile, id=alumni_id, user=request.user)
    return render(request, 'home/membership/payment_success.html', {'alumni': alumni})


def uon_alumni_membership_status(request, alumni_id):
    alumni = get_object_or_404(AlumniProfile, id=alumni_id, user=request.user)
    return render(request, 'membership/status.html', {'alumni': alumni})


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
