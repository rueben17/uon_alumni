from django.urls import path

from apps.home.views import  (
    # uon_alumni_home,
    uon_alumni_history,
    uon_alumni_exec_committee,
    uon_alumni_secretariat,
    uon_alumni_chapters,
    # uon_alumni_chapter_detail,
    uon_alumni_core,
    uon_alumni_partners,
    uon_alumni_notable,
    uon_alumni_contact_us,
    uon_alumni_register,
    # uon_alumni_membership_categories,
    uon_alumni_walk,
    uon_alumni_donate,
    uon_alumni_scholarship,
    uon_alumni_shop,
    uon_alumni_downloads,

    #other links
    # date_timer,
    # uon_alumni_all_news,
    # uon_alumni_article_detail,
    uon_alumni_gallery,
    # uon_alumni_gallery_filter,
    # uon_alumni_uploads, 
    uon_alumni_consultancy_training  
)

app_name = "home"

urlpatterns = [

    # path("", uon_alumni_home, name="uon_alumni_home"),
    path("history/", uon_alumni_history, name="uon_alumni_history"),
    path("executive-committee/", uon_alumni_exec_committee, name="uon_alumni_exec_committee"),
    path("the-secretariat/", uon_alumni_secretariat, name="uon_alumni_secretariat"),
    path("chapters/", uon_alumni_chapters, name="uon_alumni_chapters"),
    # # path("chapter/<slug:chapter_slug>/", uon_alumni_chapter_detail, name='uon_alumni_chapter_detail'),
    # path('chapter-detail/<slug:faculty_slug>/<slug:chapter_slug>/', uon_alumni_chapter_detail, name='uon_alumni_chapter_detail'),
    path("our-core/", uon_alumni_core, name="uon_alumni_core"),
    path("notable-alumni/", uon_alumni_notable, name="uon_alumni_notable"),
    path("partners/", uon_alumni_partners, name="uon_alumni_partners"),
    path("uon-alumni-consultancy-training/", uon_alumni_consultancy_training, name="uon_alumni_consultancy_training"),
    path("contact-us/", uon_alumni_contact_us, name="uon_alumni_contact_us"),
    path("uon-alumni-register/", uon_alumni_register, name="uon_alumni_register"),
    # path("membership-categories/", uon_alumni_membership_categories, name="uon_alumni_membership_categories"),
    path("uon-alumni-walk/", uon_alumni_walk, name="uon_alumni_walk"),
    path("donate/", uon_alumni_donate, name="uon_alumni_donate"),
    path("uon-alumni-scholarship/", uon_alumni_scholarship, name="uon_alumni_scholarship"),
    path("uon-alumni-shop/", uon_alumni_shop, name="uon_alumni_shop"),
    path("uon-alumni-downloads/", uon_alumni_downloads, name="uon_alumni_downloads"),
    


    # #Other links
    # path("date_timer/", date_timer, name="date_timer"),
    # path('uon-alumni-uploads/<uuid:event_id>/', uon_alumni_uploads, name="uon_alumni_uploads" ),
    # path("all-news/", uon_alumni_all_news, name="uon_alumni_all_news"),
    # path("article-detail/<slug:article_slug>/", uon_alumni_article_detail, name="uon_alumni_article_detail"),
    path("uon-alumni-gallery/", uon_alumni_gallery, name="uon_alumni_gallery"),
    # path("chapter-gallery/<slug:chapter_slug>/", uon_alumni_gallery_filter, name="uon_alumni_gallery_filter"),
    
]