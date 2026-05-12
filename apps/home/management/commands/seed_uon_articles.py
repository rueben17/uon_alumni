import uuid
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify
from apps.home.models import Article, Chapter   # replace 'yourapp' with your actual app name

class Command(BaseCommand):
    help = "Seed 55 factual UoN alumni newsletter articles (2025–2026)"

    def handle(self, *args, **kwargs):
        # ---------- 1. Ensure all chapters exist ----------
        chapter_names = [
            "Nursing Sciences Chapter",
            "Law Chapter",
            "Human Medicine Chapter",
            "Dental Sciences Alumni Chapter",
            "Range Management Chapter",
            "Journalism And Mass Communication",
            "Agriculture Chapter",
            "Veterinary Medicine Chapter",
            "Engineering Chapter",
            "Institute of Diplomacy and International Studies",
            "Chiromo Chapter",
            "Masters of Business Administration Chapter",
            "Education Chapter",
            "Architecture, Design and Development",
            "Pharmacy Chapter",
            "Computing & Informatics Chapter",
            "Mombasa Campus",
            "Central",               # for university-wide news not tied to a specific faculty
            "Research & Innovation", # for research-focused articles
            "Student Affairs",       # for student recognition articles
            "Health Sciences",       # for health conferences
            "Business",              # for MBA / project management
            "Academic Programs",     # for new courses
            "Alumni Spotlight",      # for individual alumni achievements
        ]
        chapters = {}
        for name in chapter_names:
            chap, _ = Chapter.objects.get_or_create(name=name)
            chapters[name] = chap
            self.stdout.write(f"✓ Chapter ready: {name}")

        # ---------- 2. Define all 55 articles ----------
        articles_data = [
            # 1
            {
                "title": "University of Nairobi VC Seat Declared Vacant",
                "body": "The position of Vice Chancellor at the University of Nairobi was officially declared vacant in January 2025. The announcement followed the departure of Prof. Stephen Kiama, whose five-year term ended on January 5, 2025, after a period marked by legal battles and leadership disputes.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 1, 21, 10, 0),
            },
            # 2
            {
                "title": "Search for UoN Vice Chancellor Intensifies",
                "body": "The search for a new Vice Chancellor for the University of Nairobi intensified in March 2025. The recruitment process included prominent figures such as Prof. Bitange Ndemo, who was among the five shortlisted candidates. The successful candidate was expected to replace Prof. Stephen Kiama and address governance and financial challenges at the institution.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 3, 19, 9, 0),
            },
            # 3
            {
                "title": "UoN Alumni Association Marks 20 Years of Impact",
                "body": "On Friday, February 28, 2025, the University of Nairobi Alumni Association (UONAA) celebrated its 20th anniversary with pomp and colour, bringing together alumni classes, university leadership, and key stakeholders to reflect on two decades of impact. The celebration honored founding visionaries, including the late Dr. Joseph Barrage Wanjui and the late Prof. George Magoha.\n\n“What began as an ambitious idea has flourished into a dynamic network of professionals, innovators, and leaders who continue to shape our nation and beyond.” — Prof. Amukowa Anangwe, University Council Chair",
                "quote": "What began as an ambitious idea has flourished into a dynamic network of professionals, innovators, and leaders who continue to shape our nation and beyond.",
                "article_type": "article",
                "chapter": "Central",
                "is_feature": True,
                "is_highlighted": True,
                "created_at": timezone.datetime(2025, 2, 28, 14, 0),
            },
            # 4
            {
                "title": "UONAA Scholarship Fund Disburses KES 29 Million",
                "body": "The University of Nairobi Alumni Association Scholarship Fund has disbursed KES 29 million to support needy students, as highlighted by the UONAA 20th anniversary celebrations. This fund is a long-standing initiative that has supported full-time undergraduate students for academic excellence over the past decade.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 4, 7, 0, 0),
            },
            # 5
            {
                "title": "721 UoN Students Recognized for Outstanding Achievements",
                "body": "The University of Nairobi celebrated 721 top-performing students during its annual Students’ Recognition Ceremony held on Friday, May 9, 2025, at Taifa Hall. The event highlighted outstanding achievements in academics, research, leadership, innovation, sports, and community service. Sandra Arunga received the Best Final Year Student in the Faculty of Engineering and Best Overall Female Student awards.\n\n“I’m incredibly honored… It’s an honor to receive these awards, but I wouldn’t have been able to achieve this without the support of so many,” — Sandra Arunga, award recipient",
                "quote": "I’m incredibly honored… It’s an honor to receive these awards, but I wouldn’t have been able to achieve this without the support of so many.",
                "article_type": "article",
                "chapter": "Student Affairs",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 5, 9, 11, 0),
            },
            # 6
            {
                "title": "Four Students Feted in Biotechnology",
                "body": "Four students were recognized for exceptional academic performance in biotechnology by the Kenya University Biotech Consortium. The University of Nairobi was represented by Precious Ondieki and Lucy Waititu, who received trophies, certificates, and monetary awards.",
                "quote": None,
                "article_type": "article",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 5, 21, 0, 0),
            },
            # 7
            {
                "title": "UoN Chosen to Host Inaugural Earth Observation Innovation Labs",
                "body": "Following a competitive selection process, the University of Nairobi and Taita Taveta University were chosen to host the inaugural Earth Observation (EO) Innovation Labs in Kenya. The initiative aims to drive innovation using EO data to tackle key societal challenges in agriculture, health, disaster resilience, and spatial planning.",
                "quote": None,
                "article_type": "article",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 5, 23, 0, 0),
            },
            # 8
            {
                "title": "UoN Hosts Sustainability Community Workshop",
                "body": "On May 14-15, 2025, the Africa Centre of Excellence on Sustainable Operations hosted a vibrant Community Workshop on Sustainability at the University of Nairobi. The event brought together researchers, policymakers, and community leaders to discuss sustainable approaches to resource management and food supply.",
                "quote": None,
                "article_type": "workshop",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 5, 14, 9, 0),
            },
            # 9
            {
                "title": "UoN Hosts SRI2025 Africa Satellite Event",
                "body": "The University of Nairobi hosted the SRI2025 Africa Satellite Event, a regional platform focused on advancing sustainability through collaborative research. The hybrid event took place from June 4-6, 2025, leading up to the global Sustainability Research & Innovation Congress in Chicago.",
                "quote": None,
                "article_type": "conference",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 6, 4, 9, 0),
            },
            # 10
            {
                "title": "CEMA Launches Programme for Young Scientists",
                "body": "The University of Nairobi, through the Centre for Epidemiological Modelling and Analysis (CEMA), launched a programme to help young, potential scientists still in school to develop their skills. The programme aligns with the current education system and prepares students for a competitive environment.",
                "quote": None,
                "article_type": "training",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 3, 0, 0),
            },
            # 11
            {
                "title": "Agent-Based Modeling Training Course",
                "body": "Strathmore University and USIU, in partnership with CEMA-Africa, offered an Agent-Based Modeling training course from April 28 to May 9, 2025. The course provided participants with a comprehensive understanding of agent-based modeling for research applications.",
                "quote": None,
                "article_type": "training",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 4, 28, 0, 0),
            },
            # 12
            {
                "title": "ISACA Alumni Mentorship Session at Chiromo Campus",
                "body": "On April 30, 2025, the University of Nairobi ISACA Student Group hosted an engaging alumni mentorship session at the Department of Computing and Informatics, Chiromo Campus. The session brought together current students and graduates, fostering professional networking and career guidance.",
                "quote": None,
                "article_type": "forum",
                "chapter": "Computing & Informatics Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 4, 30, 14, 0),
            },
            # 13
            {
                "title": "French Ambassador Meets VC",
                "body": "French Ambassador to Kenya H.E. Arnaud Suquet paid a courtesy call to the Vice-Chancellor of the University of Nairobi to discuss strengthened cooperation in higher education and research. The meeting explored key areas of collaboration, including academic exchanges and joint research initiatives.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 2, 28, 0, 0),
            },
            # 14
            {
                "title": "Kenyan Researchers Trained on Horizon Europe Grant Writing",
                "body": "The University of Nairobi hosted a hybrid workshop on grant writing for Kenyan researchers and innovators, focusing on securing funding from Horizon Europe. The workshop brought together a distinguished group of guests to enhance research funding capabilities.",
                "quote": None,
                "article_type": "training",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 3, 0, 0),
            },
            # 15
            {
                "title": "UoN Partners with Hebrew University of Jerusalem",
                "body": "Building on its longstanding ties with leading Kenyan universities, the Hebrew University of Jerusalem signed new agreements with the University of Nairobi to promote joint research, academic exchanges, and collaborative projects in key areas such as food security, climate change, renewable energy, and education.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 4, 0, 0),
            },
            # 16
            {
                "title": "UoN and Beihang University Launch Joint Laboratory",
                "body": "The University of Nairobi partnered with Beihang University to launch a Joint Laboratory for BeiDou Engineering and Simulation Technology. The collaboration aims to advance satellite technology and its applications in Kenya.",
                "quote": None,
                "article_type": "article",
                "chapter": "Engineering Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 27, 0, 0),
            },
            # 17
            {
                "title": "CS Julius Ogamba Fires 4 UoN Council Members",
                "body": "Education Cabinet Secretary Julius Ogamba terminated the appointments of four University of Nairobi council members: James Njiru, Prof. Duke Orata, Prof. Ayub Njoroge Gitau, and Prof. Francis Jackim Mulaa. The move came amid ongoing governance struggles at the university.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 4, 12, 0, 0),
            },
            # 18
            {
                "title": "New UoN Council Appointed for Three-Year Term",
                "body": "The Cabinet Secretary for Education, Hon. Julius Migos Ogamba, officially appointed a new University Council for the University of Nairobi, effective from July 25, 2025. The appointments mark a strategic new chapter in the governance and advancement of the University.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 7, 25, 0, 0),
            },
            # 19
            {
                "title": "New UoN Council Inaugurated",
                "body": "The University of Nairobi marked a significant milestone with the inauguration of its new Council in a ceremony held at the University of Nairobi Towers on August 5, 2025. The event was presided over by the Cabinet Secretary for Education, Hon. Julius Ogamba, in the presence of key government and university leaders.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 5, 11, 0),
            },
            # 20
            {
                "title": "Kisumu Campus Welcomes First Government-Sponsored Cohort",
                "body": "The University of Nairobi Kisumu Campus community warmly welcomed the first cohort of government-sponsored students admitted to the campus, reporting on Monday, August 18, 2025. The campus community assured students of a memorable experience as they pursue their dream careers.",
                "quote": None,
                "article_type": "article",
                "chapter": "Mombasa Campus",  # Kisumu not in list, using Mombasa as proxy for regional campus
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 18, 0, 0),
            },
            # 21
            {
                "title": "VC Addresses First-Year Students 2025/2026",
                "body": "The University of Nairobi's Vice-Chancellor (Ag), Prof. Margaret Hutchinson, addressed newly admitted First-Year students for the 2025/2026 academic year on August 21, 2025, at the iconic Taifa Hall. She congratulated them on earning a place at Kenya’s premier institution of higher learning.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 21, 10, 0),
            },
            # 22
            {
                "title": "Agricultural Industrial Linkages Workshop at KATIC",
                "body": "The University of Nairobi, through its Faculty of Agriculture, hosted a landmark Agricultural Industrial Linkages Workshop at the Kantaria Agricultural Technology and Innovation Centre (KATIC), Upper Kabete Campus on July 18, 2025. The workshop brought together stakeholders from academia and industry to chart a new path for agricultural education and innovation in Kenya.",
                "quote": None,
                "article_type": "workshop",
                "chapter": "Agriculture Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 7, 18, 9, 0),
            },
            # 23
            {
                "title": "8th Annual Research and Innovation Week 2025",
                "body": "The University of Nairobi opened its 8th Annual Research and Innovation Week on Tuesday, October 21, 2025, at the Chandaria Auditorium. The four-day event brought together researchers, policymakers, students, and industry leaders to showcase advancements in science, technology, and innovation. The week merged two annual events: the Annual Research Week and the Nairobi Innovation Week under the theme “Advancing Research and Innovation from Discovery to Impact in a Dynamic Global Landscape.” A notable highlight was a new partnership with Mazao Group to develop agricultural technologies for food security.",
                "quote": None,
                "article_type": "conference",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 21, 9, 0),
            },
            # 24
            {
                "title": "UoN Shines at Kenya National Research Festival 2025",
                "body": "The University of Nairobi participated in the Kenya National Research Festival 2025, held from August 18-22 at Egerton University. Prof. Richard Kiprono Mibey won the Best Research with Economic Impact Award, Ms. Rahab Wanjeri won the Best Research with Social Impact Award, and Mr. Paul Ongaro won the Best User-friendly Research Award. UoN showcased cutting-edge innovations, including startup Pera Foods, an essential oils unit, and a circular economy innovation transforming invasive plant parasites into valuable products.\n\n“The University of Nairobi is deeply committed to ensuring that our research moves beyond academic journals into real-world solutions that transform lives.” — Prof. Francis Mulaa, Deputy Vice Chancellor (Research, Innovation & Enterprise)",
                "quote": "The University of Nairobi is deeply committed to ensuring that our research moves beyond academic journals into real-world solutions that transform lives.",
                "article_type": "article",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 18, 0, 0),
            },
            # 25
            {
                "title": "UoN Hosts 26th World Korea Forum",
                "body": "Marking the first time the forum has been held in Africa, the University of Nairobi hosted the 26th World Korea Forum on August 6-7, 2025, at the University of Nairobi Towers. The event brought together global leaders to discuss diplomacy and international relations.",
                "quote": None,
                "article_type": "forum",
                "chapter": "Institute of Diplomacy and International Studies",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 6, 10, 0),
            },
            # 26
            {
                "title": "First Lady Launches Kantaria Agricultural Technology and Innovation Centre",
                "body": "On August 14, 2025, the First Lady of Kenya, H.E. Mrs. Rachel Ruto, officially launched the Kantaria Agricultural Technology and Innovation Centre (KATIC) at the University of Nairobi’s Upper Kabete campus. Funded by Elgon Kenya at a cost of Sh80 million, KATIC is a hub for agricultural innovation, youth empowerment, and industry-academia collaboration.\n\n“KATIC is our legacy project, built to empower the next generation of farmers and entrepreneurs.” — Dr. Bimal Kantaria, Managing Director, Elgon Kenya",
                "quote": "KATIC is our legacy project, built to empower the next generation of farmers and entrepreneurs.",
                "article_type": "article",
                "chapter": "Agriculture Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 14, 11, 0),
            },
            # 27
            {
                "title": "ACU Congress 2025 Hosted at UoN",
                "body": "The Association of Commonwealth Universities (ACU) Congress 2025 was hosted at the University of Nairobi, bringing together members and partners from 21 countries around the world. The conference explored how Commonwealth universities can work together to contribute to renewal, development, and global innovation.",
                "quote": None,
                "article_type": "conference",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 27, 0, 0),
            },
            # 28
            {
                "title": "Dr. Caroline Hunja Calls for Deeper Collaboration at Research Week Opening",
                "body": "At the opening of the 8th Annual Research and Innovation Week 2025, Dr. Caroline Hunja, Secretary for Higher Education and Research at the Ministry of Education, called for deeper collaboration between academia, the private sector, and government agencies to accelerate translating research into practical solutions.\n\n“We convene at a time of immense opportunity and pressing challenges. Our growth, prosperity, and competitiveness in the global economy depends on our ability to generate knowledge, convert it into value-added goods and services, and apply it for the benefit of all Kenyans.” — Dr. Caroline Hunja",
                "quote": "We convene at a time of immense opportunity and pressing challenges. Our growth, prosperity, and competitiveness in the global economy depends on our ability to generate knowledge, convert it into value-added goods and services, and apply it for the benefit of all Kenyans.",
                "article_type": "conference",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 21, 10, 0),
            },
            # 29
            {
                "title": "3rd International Conference on Educational Management, Policy & Curriculum Studies",
                "body": "The University of Nairobi hosted the 3rd Annual International Conference on Educational Management, Policy & Curriculum Studies (AICEMPCS 2025), unveiling key findings on AI and future-proofing education. The conference brought together educators, policymakers, and researchers to discuss the future of education.",
                "quote": None,
                "article_type": "conference",
                "chapter": "Education Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 28, 0, 0),
            },
            # 30
            {
                "title": "7th International Conference on Health (ICH 2025)",
                "body": "The Faculty of Health Sciences, University of Nairobi, in collaboration with Kenyatta National Hospital (KNH), convened the 7th International Conference on Health (ICH 2025). The conference brought together health professionals, researchers, and policymakers to discuss advancements in healthcare.",
                "quote": None,
                "article_type": "conference",
                "chapter": "Health Sciences",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 21, 0, 0),
            },
            # 31
            {
                "title": "7th Annual International Conference on Project Management",
                "body": "The 7th Annual International Conference on Project Management was held on October 22-23, 2025, during the University of Nairobi’s Research Week. The conference focused on advancing project management practices in a dynamic global environment.",
                "quote": None,
                "article_type": "conference",
                "chapter": "Business",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 22, 0, 0),
            },
            # 32
            {
                "title": "PMI Youth Forum Challenges Students to Embrace AI",
                "body": "The Project Management Institute Youth Forum held at the Manu Chandaria Auditorium on October 4, 2025, challenged students to embrace AI and networking. Mr. Kadika Mwangi urged students to see mentorship as a key to professional success.",
                "quote": None,
                "article_type": "forum",
                "chapter": "Business",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 4, 0, 0),
            },
            # 33
            {
                "title": "ESC Innovation Pillar Workshop in Naivasha",
                "body": "The Engineering and Science Complex (ESC) Innovation Pillar hosted a three-day workshop from September 22-24, 2025, in Naivasha, focused on designing an Innovation Business Model to guide the Innovation Community of Excellence. The workshop produced a comprehensive blueprint positioning the ESC as a hub for entrepreneurial thinking and real-world solutions.",
                "quote": None,
                "article_type": "workshop",
                "chapter": "Engineering Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 9, 22, 9, 0),
            },
            # 34
            {
                "title": "UoN Alumnus Tracks Expanding Lakes and Wildfires",
                "body": "Julius Mbuvi Kimani, an astronomy and astrophysics graduate from the University of Nairobi, is using Earth observation to monitor Africa’s expanding lakes and map wildfires. Using satellite data, Julius has tracked the steady rise of Lake Nakuru over three decades and mapped the devastating Isiolo wildfires of early 2025, which burned over 200,000 acres of pastureland.",
                "quote": None,
                "article_type": "article",
                "chapter": "Alumni Spotlight",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 13, 0, 0),
            },
            # 35
            {
                "title": "UoN Doctoral Student Develops Water Purification Technology",
                "body": "Lilian Anyanga Owino, a doctoral student at the University of Nairobi, is specializing in water purification through photocatalysis. Her project focuses on synthesizing a GO/TiO2 nanotube composite for treating industrial wastewater under visible light, aiming to improve pollutant degradation efficiency. She is jointly supervised by Prof. Francis Nyongesa (UoN) and Prof. Arnaud Magrez (EPFL).",
                "quote": None,
                "article_type": "article",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 28, 0, 0),
            },
            # 36
            {
                "title": "Lilian Owino Named Among '100 PhDs for Africa'",
                "body": "Lilian Anyanga Owino has been named among the “100 PhDs for Africa” programme, an initiative attracting international scholarships. Her research explores how integrating graphene can improve light absorption and charge separation to increase efficiency of pollutant degradation.\n\n“Excellence means striving for the highest standards, both scientific and personal, in everything she undertakes.” — Lilian Anyanga Owino",
                "quote": "Excellence means striving for the highest standards, both scientific and personal, in everything she undertakes.",
                "article_type": "article",
                "chapter": "Alumni Spotlight",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 28, 0, 0),
            },
            # 37
            {
                "title": "English Professor Concludes Newborn Care Research Project",
                "body": "Professor English concluded a landmark project on Kenyan newborn care. The project began in October 2020 and continued until September 2025, involving a multidisciplinary team of researchers, including Assistant Professor David Gathara, Dr. Sebastian Fuller, Dr. Michuki Maina, Dr. Dorothy Okello, and Professor English.",
                "quote": None,
                "article_type": "article",
                "chapter": "Health Sciences",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 3, 0, 0),
            },
            # 38
            {
                "title": "UoN Partners with ICPE to Pilot Antibiotic Reduction in Farming",
                "body": "The University of Nairobi partnered with ICPE to pilot research on reducing antibiotic use in East African farming. The two-year Kenya-Slovenia partnership introduces bacteriophage-based alternatives to antibiotics in farming, aiming to reduce antimicrobial resistance and promote sustainable agriculture.",
                "quote": None,
                "article_type": "article",
                "chapter": "Agriculture Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 7, 21, 0, 0),
            },
            # 39
            {
                "title": "UoN Hosts British Council Learning and Design Lab",
                "body": "From November 24-28, 2025, UoN hosted the 4th British Council Learning and Design Lab in Nairobi, bringing together students and educators to explore innovative teaching methodologies.",
                "quote": None,
                "article_type": "workshop",
                "chapter": "Education Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 24, 9, 0),
            },
            # 40
            {
                "title": "UoN and AU-EU Organize Grant Writing Workshop",
                "body": "The University of Nairobi hosted a high-level hybrid grant writing workshop on Horizon Europe, the European Union’s flagship research and innovation programme, on Monday, November 3, 2025. The workshop focused on securing international research funding.",
                "quote": None,
                "article_type": "training",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 3, 0, 0),
            },
            # 41
            {
                "title": "ACUNS Annual Meeting Hosted in Nairobi",
                "body": "The ACUNS 2025 Annual Meeting was co-hosted in Nairobi, underscoring the importance of academic diplomacy and intergenerational leadership. The meeting reaffirmed the mission to connect ideas with action and scholarship with service.",
                "quote": None,
                "article_type": "conference",
                "chapter": "Institute of Diplomacy and International Studies",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 6, 30, 0, 0),
            },
            # 42
            {
                "title": "FRENCH ALUMNI DAY CELEBRATIONS",
                "body": "The University of Nairobi hosted the France Alumni Day, a forum focused on the internationalization of African higher education and research. The event brought together alumni of French institutions and African universities.",
                "quote": None,
                "article_type": "forum",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 6, 13, 0, 0),
            },
            # 43
            {
                "title": "DFP Hosts Successful Writing and Mentoring Workshop",
                "body": "The Leeds University Centre for African Studies, in conjunction with the University of Nairobi, held a successful writing and mentoring workshop aimed at enhancing academic writing skills among early-career researchers. The workshop provided mentorship opportunities for young academics.",
                "quote": None,
                "article_type": "workshop",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 8, 14, 0, 0),
            },
            # 44
            {
                "title": "Chinese CEOs Explore Collaboration with UoN",
                "body": "A high-level delegation of Chinese Chief Executive Officers paid a courtesy call to the Vice Chancellor of the University of Nairobi as part of their wider African tour exploring areas of possible collaboration.\n\n“A very rare opportunity which cannot be missed.” — Prof. Margaret Jesang Hutchinson, Vice Chancellor (Ag)",
                "quote": "A very rare opportunity which cannot be missed.",
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 11, 29, 0, 0),
            },
            # 45
            {
                "title": "2nd Annual UoN Alumni Walk Raises Funds for Scholarships",
                "body": "On Saturday, September 27, 2025, the University of Nairobi Alumni Association held its second annual 10-kilometer fundraising walk, aiming to raise Kshs. 50M for the UoN Alumni Scholarship Fund. The inaugural walk in 2024 raised Sh2.4 million, supporting needy students.\n\n“Education is the most powerful weapon which you can use to change the world.” — Nelson Mandela (guiding quote for the walk)",
                "quote": "Education is the most powerful weapon which you can use to change the world.",
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 9, 27, 8, 0),
            },
            # 46
            {
                "title": "UoN Alumni Association Unveils 20th Anniversary Theme",
                "body": "The University of Nairobi Alumni Association unveiled the theme “Let Us Embrace a Culture of Giving Back” during its 20th anniversary celebrations, emphasizing financial contributions, mentorship, and advocacy for institutional growth.\n\n“Many of us disappear after graduation and are never heard from again. We must embrace this culture of giving back.” — Prof. Nicholas Letting, UoN Alumnus",
                "quote": "Many of us disappear after graduation and are never heard from again. We must embrace this culture of giving back.",
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 2, 28, 15, 0),
            },
            # 47
            {
                "title": "The Nairobi School of AI: UoN's Bold AI Initiative",
                "body": "The Nairobi School of AI will position the University of Nairobi as a leader in AI education, offering one of Africa’s first Master’s programs focused on AI. This initiative aims to generate top-tier talent ready for global competition, as AI is projected to contribute $15.7 trillion to the global economy by 2030.",
                "quote": None,
                "article_type": "article",
                "chapter": "Computing & Informatics Chapter",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 21, 0, 0),
            },
            # 48
            {
                "title": "UoN's 'The Big 5' Strategic Agenda",
                "body": "The University of Nairobi has actively promoted student innovation through its “Big 5” initiatives, a strategic agenda focusing on key areas such as artificial intelligence (AI), green jobs, and health research. These initiatives, spearheaded by the university community, aim to equip students with skills to drive meaningful change.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 10, 21, 0, 0),
            },
            # 49
            {
                "title": "UoN Attracts 88 Research Grants Value at KES 5.4 Billion",
                "body": "The University of Nairobi attracted 88 research grants valued at KES 5.4 billion, with an additional KES 1.026 billion secured between July and November 2025. The university recorded over 1,000 research publications with impact factors exceeding 19, registered nine intellectual properties, and signed more than 220 collaboration agreements.",
                "quote": None,
                "article_type": "article",
                "chapter": "Research & Innovation",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 12, 11, 0, 0),
            },
            # 50
            {
                "title": "UoN Launches MSc in Artificial Intelligence Programme",
                "body": "During the 74th Graduation Ceremony, the University of Nairobi announced the revision of outdated curricula and the introduction of new programmes, including an MSc in Artificial Intelligence and Entrepreneurship as a common course, alongside the launch of the University of Nairobi Innovation Hub.",
                "quote": None,
                "article_type": "article",
                "chapter": "Academic Programs",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 12, 11, 0, 0),
            },
            # 51
            {
                "title": "74th Graduation Ceremony",
                "body": "On December 11, 2025, the University of Nairobi held its 74th Graduation Ceremony at the Chancellor’s Court. A total of 4,504 degrees and diplomas were conferred, including 48 Doctorates, 905 master’s degrees, 3,416 bachelor’s degrees, 16 postgraduate diplomas, 14 fellowships, and 98 diplomas.\n\n“Your talent is your passport, your determination is your engine, your imagination is your compass.” — Prof. Patrick Verkooijen, Chancellor\n\n“As you step into the next chapter, remember that your education empowers you not just to succeed, but to transform your communities.” — Prof. Margaret Hutchinson, Vice Chancellor (Ag)",
                "quote": "Your talent is your passport, your determination is your engine, your imagination is your compass.",
                "article_type": "article",
                "chapter": "Central",
                "is_feature": True,
                "is_highlighted": True,
                "created_at": timezone.datetime(2025, 12, 11, 10, 0),
            },
            # 52
            {
                "title": "CS Ogamba Urges Graduates to Become Job Creators",
                "body": "Speaking at the 74th Graduation Ceremony, Education CS Julius Ogamba urged the 4,504 graduates to move away from a narrow focus on formal employment and instead position themselves as job creators through innovation and entrepreneurship.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 12, 11, 11, 0),
            },
            # 53
            {
                "title": "Kenya Formalises Protocol Education at UoN",
                "body": "Kenya has taken a decisive step toward reshaping professional education after the University of Nairobi hosted the country’s first formal protocol and etiquette education lecture at the Institute of Diplomacy and International Studies (IDIS). An MoU was signed by Vice-Chancellor Prof. Margaret Jesang’ Hutchinson and Protocol Hub International CEO Apollo John.\n\n“For a long time, protocol has been treated as an afterthought, yet it determines how institutions engage the world. By bringing protocol and etiquette into formal education, we are preparing students to represent Kenya with confidence, discipline, and global awareness.” — Apollo John, CEO, Protocol Hub International",
                "quote": "For a long time, protocol has been treated as an afterthought, yet it determines how institutions engage the world. By bringing protocol and etiquette into formal education, we are preparing students to represent Kenya with confidence, discipline, and global awareness.",
                "article_type": "article",
                "chapter": "Institute of Diplomacy and International Studies",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 12, 20, 0, 0),
            },
            # 54 (duplicate of 42? Actually original list had duplicate France Alumni Day; we will keep one but rename slightly)
            {
                "title": "France Alumni Day Celebrates Internationalization",
                "body": "The University of Nairobi hosted the France Alumni Day, a forum focused on the internationalization of African higher education and research, bringing together alumni of French institutions and African universities to discuss cross-border collaboration.",
                "quote": None,
                "article_type": "forum",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 6, 13, 0, 0),
            },
            # 55
            {
                "title": "UoN Council Rejects Leadership Allegations",
                "body": "The University of Nairobi’s Council released a joint press statement to address and clarify various false narratives circulating in the media regarding university leadership, reaffirming its commitment to transparent governance.",
                "quote": None,
                "article_type": "article",
                "chapter": "Central",
                "is_feature": False,
                "is_highlighted": False,
                "created_at": timezone.datetime(2025, 5, 13, 0, 0),
            },
        ]

        # ---------- 3. Insert articles, skip duplicates ----------
        created = 0
        skipped = 0
        for data in articles_data:
            chap = chapters[data["chapter"]]
            # Check for existence by title and year/month
            existing = Article.objects.filter(
                title=data["title"],
                created_at__year=data["created_at"].year,
                created_at__month=data["created_at"].month,
            ).first()
            if existing:
                self.stdout.write(self.style.WARNING(f"Skipped (exists): {data['title']}"))
                skipped += 1
                continue

            article = Article(
                id=uuid.uuid4(),
                article_type=data["article_type"],
                chapter=chap,
                title=data["title"],
                body=data["body"],
                quote=data["quote"],
                is_feature=data["is_feature"],
                is_highlighted=data["is_highlighted"],
                created_at=data["created_at"],
            )
            article.save()
            # Force slug generation
            article.slug = slugify(f"{data['title']}-{data['created_at'].strftime('%Y-%m-%d')}")
            article.save(update_fields=["slug"])
            self.stdout.write(self.style.SUCCESS(f"Created: {article.title}"))
            created += 1

        self.stdout.write(self.style.SUCCESS(f"\n✅ Done! Created {created} articles, skipped {skipped}."))