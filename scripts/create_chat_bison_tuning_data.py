import json
import random

corpus = []

with open("embeddings_dataset_corpus.jsonl", "r") as corpus_file:
    for line in corpus_file.readlines():
        if "https://alorica.com/careers/" in line:
            continue
        corpus.append(json.loads(line))

print("Read", len(corpus), "lines.")

standard_instructions = """
You are an Alorica chat support agent for the alorica.com website.
Guide the user to the most relevant page from the listed pages, asking follow-up questions if needed.
Don't answer with /careers/ pages unless the user is asking about a job or careers.
The list of pages is:
/outcomes/continuity/workforce-optimization
/outcomes/loyalty-and-engagement/subscription-management
/outcomes/loyalty-and-engagement
/careers/latin-america-the-caribbean
/outcomes/community/content-management
/industries/public-sector
/outcomes/products/content-moderation
/outcomes/actionable-insights
/outcomes/efficiency-and-optimization/speed-to-proficiency
/careers/china
/outcomes/community/trust-and-safety
/home
/terms-of-use
/careers/jamaica
/industries/fintech
/outcomes/loyalty-and-engagement/omnichannel
/outcomes/actionable-insights/alorica-analytics
/philippine-alorica-group-privacy-statement
/careers/asia-pacific
/careers/dominican-republic
/careers
/careers/guatemala
/outcomes/products/alorica-iq
/outcomes/efficiency-and-optimization/alorica-automation
/corporate-social-responsibility
/alorica-agent-resources
/sales-inquiries
/diversity-equity-and-inclusion
/outcomes/efficiency-and-optimization/contact-optimization
/outcomes/products/knowledge-management
/contact
/outcomes/growth/alorica-on-demand
/industries/online-community
/equal-employment-opportunity-employer
/industries
/careers/puebla
/outcomes/growth
/careers/india
/industries/technology
/procurement
/outcomes/products/virtual-assistant
/careers/philippines
/outcomes
/outcomes/community
/industries/online-marketplaces
/industries/subscription-services
/careers/uruguay
/outcomes/products/rpa-rda
/careers/panama
/outcomes/continuity
/outcomes/efficiency-and-optimization
/outcomes/continuity/geo-optimization
/outcomes/products/interaction-analytics
/industries/health-and-lifestyle
/outcomes/products/loan-servicing
/culture
/careers/guadalajara
/outcomes/products/Agent-Assist
/careers/leon
/careers/north-america
/awards-recognition
/outcomes/products/fraud-prevention
/industries/gaming
/careers/colombia
/news
/careers/japan
/careers/honduras
/privacy-policy
/outcomes/continuity/alorica-anywhere
/outcomes/growth/financial-solutions
/insights
/outcomes/products/journey-mapping
/careers/emea
/outcomes/products/automated-discovery
/outcomes/actionable-insights/alorica-experiences-practice
/our-leadership
/why-alorica
/outcomes/growth/revenue-generation
/careers/puebla/puebla---hear-from-team-2
/careers/leon
/careers/guatemala
/es/careers/mexico-city
/careers/jamaica/jamaica-hear-from-team-3
/careers/panama
/careers/uruguay
/careers/honduras
/careers
/careers/guadalajara/guadalajara-hear-from-team3
/careers/philippines/philippines---meet-bong
/careers/puebla/puebla---hear-from-team-5
/careers/guadalajara
/careers/puebla/puebla---hear-from-team-4
/careers/philippines/philippines---gregorio-inoc
/careers/jamaica/jamaica-hear-from-team-2
/careers/jamaica/jamaica-hear-from-team-1
/careers/jamaica
/careers/jamaica/jamaica-hear-from-team-5
/careers/dominican-republic
/careers/guadalajara/guadalajara-hear-from-team
/careers/puebla/puebla---hear-from-team-6
/careers/jamaica/jamaica-hear-from-team-6
/careers/philippines/philippines---meet-lucille-video
/careers/jamaica/jamaica-hear-from-team-4
/careers/puebla/puebla---hear-from-team-3
/careers/panama/panama-hear-from-team-3
/careers/india/india---our-insanely-great-video
/careers/panama/panama-hear-from-team-1
/careers/india/india---moving-up-video
/careers/panama/panama-hear-from-team-2
/careers/india/india---contact-centers
/careers/philippines/philippines---meet-ram-video
/careers/guadalajara/guadalajara-hear-from-team2
/careers/philippines/philippines---what-is-insanely-great
/careers/philippines/philippines---meet-gloria-video
/careers/puebla/puebla---hear-from-team-1
/home/mlba-banner
/home/2023-gold-stevie-winner
/home/recognized-industry-leader-(everest)-banner
/home/generative-ai-banner
/why-alorica/leader-yet-again
/awards-recognition
/careers/north-america-team
/careers/asia-pacific/philippines
/careers/EMEA-Team
/careers/latin-america-the-caribbean/jamaica
/careers/latin-america-the-caribbean/puebla-mexico
/careers/latin-america-the-caribbean/honduras
/careers/latin-america-the-caribbean/uruguay
/careers/asia-pacific/india
/careers/latin-america-the-caribbean/dominican-republic
/careers/latin-america-the-caribbean/colombia
/careers/asia-pacific-team
/careers/latin-america-the-caribbean/panama
/careers/asia-pacific/china
/careers/latin-america-the-caribbean/guatemala
/careers/latin-america-the-caribbean/leon-mexico
/careers/latin-america-the-caribbean/mexico
/careers/asia-pacific/japan
/careers/latam-caribbean-team
/careers/latin-america-the-caribbean/guadalajara-mexico
/careers/philippines/internships
/careers/china/operations-managers
/careers/china/customer-service-representatives-china
/careers/puebla/sales-representatives
/careers/india/corporate-support
/careers/employee-experience-(hr)-recruiting
/careers/puebla/customer-service-representatives-puebla
/careers/site-director
/careers/head-coaches-(operations-managers)---career
/careers/china/team-managers
/careers/india/digital-back-office-representative-(email-and-chat-support)
/careers/Don-t-see-a-role-that-fits--career
/careers/tech-support-team-players--career
/careers/philippines/front-line-agent
/careers/sales-retention-team-players---career
/careers/corporate-support---career
/careers/china/looking-for-something-different
/careers/india/it-support
/careers/puebla/want-to-learn-more-chat-career
/careers/site-director---career
/careers/india/intelligent-automation-support-and-maintenance
"""

dataset = []

for i in range(100):
    print("=====", i, "=====")
    idx = random.randint(0, len(corpus)-1)
    title = corpus[i]['title']
    text = corpus[i]['text']

    print(title)
    user_input = input("Provide a prompt that the user might say to get to this page: ")
    if user_input == "":
        print("Early exit")
        break

    input_text = "prompt: " + standard_instructions + "\nuser_text: Can you help me find the page for " + user_input
    output_text = "Certainly! That page is located at " + text.split("\n")[0] + ". It's called " + title
    dataset.append({'input_text': input_text, 'output_text': output_text})
    print("\n")

prefix = input('Provide a filename prefix: ')
with open(prefix + "_tuning_dataset.jsonl", "w") as output:
    for d in dataset:
        output.write(json.dumps(d))
        output.write("\n")