from django.urls import path

from apps.home.views import  (
    CoreValuesListView,
    uon_alumni_membership_success,
    uon_alumni_membership_status,
    # uon_alumni_simulate_payment_processing,
    get_tier_details,
    uon_alumni_home,
    uon_alumni_history,
    uon_alumni_exec_committee,
    uon_alumni_secretariat,
    uon_alumni_chapters,
    uon_alumni_chapter_detail,
    # uon_alumni_core,
    uon_alumni_partners,
    uon_alumni_notable,
    uon_alumni_contact_us,
    uon_alumni_register,
    uon_alumni_profile_creation,
    uon_alumni_register_membership,
    uon_alumni_agm,
    uon_alumni_categories_benefits,
    uon_alumni_walk,
    uon_alumni_donate,
    uon_alumni_scholarship,
    uon_alumni_shop,
    uon_alumni_downloads,

    #other links
    date_timer,
    uon_alumni_all_news,
    uon_alumni_article_detail,
    uon_alumni_gallery,
    uon_alumni_gallery_filter,
    # uon_alumni_uploads, 
    uon_alumni_consultancy_training  
)

app_name = "home"

urlpatterns = [

    path("", uon_alumni_home, name="uon_alumni_home"),
    path("history/", uon_alumni_history, name="uon_alumni_history"),
    path("executive-committee/", uon_alumni_exec_committee, name="uon_alumni_exec_committee"),
    path("the-secretariat/", uon_alumni_secretariat, name="uon_alumni_secretariat"),
    path("chapters/", uon_alumni_chapters, name="uon_alumni_chapters"),
    path("chapter/<slug:chapter_slug>/", uon_alumni_chapter_detail, name='uon_alumni_chapter_detail'),
    path('chapter-detail/<slug:faculty_slug>/<slug:chapter_slug>/', uon_alumni_chapter_detail, name='uon_alumni_chapter_detail'),
    # path("our-core/", uon_alumni_core, name="uon_alumni_core"),
    path('our-core/', CoreValuesListView.as_view(), name='uon_alumni_core'),
    path("notable-alumni/", uon_alumni_notable, name="uon_alumni_notable"),
    path("partners/", uon_alumni_partners, name="uon_alumni_partners"),
    path("uon-alumni-annual-general-meeting/", uon_alumni_agm, name="uon_alumni_agm"),
    path("uon-alumni-consultancy-training/", uon_alumni_consultancy_training, name="uon_alumni_consultancy_training"),
    path("contact-us/", uon_alumni_contact_us, name="uon_alumni_contact_us"),
    path("uon-alumni-register/", uon_alumni_register, name="uon_alumni_register"),
    path("uon-alumni-profile-creation/", uon_alumni_profile_creation, name="uon_alumni_profile_creation"),
    path("uon-alumni-membership/<int:alumni_id>/", uon_alumni_register_membership, name="uon_alumni_register_membership"),
    # path('uon-alumni-membership/<int:alumni_id>/payment/', uon_alumni_simulate_payment_processing, name='uon_alumni_simulate_payment_processing'),
    path('uon-alumni-membership/<int:alumni_id>/success/', uon_alumni_membership_success, name='uon_alumni_membership_success'),
    path('uon-alumni-membership/<int:alumni_id>/status/', uon_alumni_membership_status, name='uon_alumni_membership_status'),
    path("uon-alumni-categories-benefits/", uon_alumni_categories_benefits, name="uon_alumni_categories_benefits"),
    path("uon-alumni-walk/", uon_alumni_walk, name="uon_alumni_walk"),
    path("donate/", uon_alumni_donate, name="uon_alumni_donate"),
    path("uon-alumni-scholarship/", uon_alumni_scholarship, name="uon_alumni_scholarship"),
    path("uon-alumni-shop/", uon_alumni_shop, name="uon_alumni_shop"),
    path("uon-alumni-downloads/", uon_alumni_downloads, name="uon_alumni_downloads"),
    


    # #Other links
    path("date_timer/", date_timer, name="date_timer"),
    path('get-tier-details/', get_tier_details, name='get_tier_details'),
    # path('uon-alumni-uploads/<uuid:event_id>/', uon_alumni_uploads, name="uon_alumni_uploads" ),
    path("uon-alumni-news/", uon_alumni_all_news, name="uon_alumni_all_news"),
    path("article-detail/<slug:article_slug>/", uon_alumni_article_detail, name="uon_alumni_article_detail"),
    path("uon-alumni-gallery/", uon_alumni_gallery, name="uon_alumni_gallery"),
    path("chapter-gallery/<slug:chapter_slug>/", uon_alumni_gallery_filter, name="uon_alumni_gallery_filter"),
    
]