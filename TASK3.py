# =========================================================
# ADVANCED AI SEO BLOG & CONTENT CLUSTER GENERATOR
# =========================================================

from datetime import datetime


class SEOContentGenerator:

    def __init__(
        self,
        business_name,
        service,
        city,
        target_keyword,
        audience="General Audience"
    ):

        self.business_name = business_name
        self.service = service
        self.city = city
        self.target_keyword = target_keyword
        self.audience = audience

    # =====================================================
    # Generate SEO Meta Title
    # =====================================================

    def generate_meta_title(self):

        return f"Best {self.service} in {self.city} | {self.business_name}"

    # =====================================================
    # Generate Meta Description
    # =====================================================

    def generate_meta_description(self):

        return (
            f"Looking for professional {self.service} in {self.city}? "
            f"{self.business_name} offers affordable and reliable solutions "
            f"tailored to your needs."
        )

    # =====================================================
    # Generate SEO Blog Outline
    # =====================================================

    def generate_outline(self):

        return {
            "H1": f"Complete Guide to {self.target_keyword} in {self.city}",

            "H2": [
                f"Why {self.target_keyword} Matters",
                f"Benefits of Professional {self.service}",
                f"Common Mistakes to Avoid",
                f"How to Choose the Best {self.service}",
                f"Why Choose {self.business_name}"
            ],

            "H3": [
                "Affordable Pricing",
                "Expert Team",
                "Customer Support",
                "Latest Technology",
                "Long-Term Benefits"
            ]
        }

    # =====================================================
    # Generate Long-Form SEO Blog
    # =====================================================

    def generate_blog(self):

        blog = f"""
============================================================
SEO BLOG ARTICLE
============================================================

Title:
{self.generate_meta_title()}

Meta Description:
{self.generate_meta_description()}

------------------------------------------------------------
INTRODUCTION
------------------------------------------------------------

If you are searching for reliable {self.service} in {self.city},
you are not alone.

Many businesses and customers struggle to find trustworthy
solutions that deliver real value.

At {self.business_name}, we specialize in helping clients with
professional {self.service} designed for long-term success.

------------------------------------------------------------
WHY THIS SERVICE MATTERS
------------------------------------------------------------

Choosing the right {self.service} can improve efficiency,
save money, and help businesses grow faster.

Professional services also reduce common mistakes and
improve customer satisfaction.

------------------------------------------------------------
COMMON CUSTOMER PROBLEMS
------------------------------------------------------------

✔ Poor service quality
✔ High pricing
✔ Lack of support
✔ Delayed results
✔ Limited expertise

------------------------------------------------------------
HOW {self.business_name.upper()} HELPS
------------------------------------------------------------

Our team focuses on:

✔ Customized solutions
✔ Affordable pricing
✔ Expert support
✔ Fast delivery
✔ High-quality service

------------------------------------------------------------
LOCAL SEO ADVANTAGE
------------------------------------------------------------

Businesses in {self.city} benefit from local expertise,
better communication, and faster support.

Local SEO also improves online visibility for nearby customers.

------------------------------------------------------------
CONCLUSION
------------------------------------------------------------

If you want professional {self.service} in {self.city},
{self.business_name} is here to help.

Contact us today to learn more about our services.
"""

        return blog

    # =====================================================
    # Generate Content Clusters
    # =====================================================

    def generate_content_clusters(self):

        clusters = {

            "Pillar Topic":
                f"{self.service} in {self.city}",

            "Cluster Topics": [

                f"Top Benefits of {self.service}",
                f"How to Choose the Best {self.service}",
                f"Beginner Guide to {self.service}",
                f"Affordable {self.service} Tips",
                f"Common Mistakes in {self.service}",
                f"Latest Trends in {self.service}",
                f"Best Tools for {self.service}",
                f"Why Local Businesses Need {self.service}"
            ]
        }

        return clusters

    # =====================================================
    # Generate Internal Linking Ideas
    # =====================================================

    def generate_internal_links(self):

        links = [

            "Homepage",
            "About Us",
            "Services Page",
            "Pricing Page",
            "Case Studies",
            "Testimonials",
            "Contact Page",
            "FAQ Section"
        ]

        return links

    # =====================================================
    # Generate SEO Keywords
    # =====================================================

    def generate_keywords(self):

        keywords = [

            self.target_keyword,
            f"Best {self.service} in {self.city}",
            f"Affordable {self.service}",
            f"Professional {self.service}",
            f"{self.service} near me",
            f"Top-rated {self.service}",
            f"Local {self.service} company"
        ]

        return keywords

    # =====================================================
    # Generate CTA Variations
    # =====================================================

    def generate_ctas(self):

        return [

            "Contact Us Today",
            "Book a Free Consultation",
            "Get Started Now",
            "Request a Quote",
            "Talk to Our Experts"
        ]

    # =====================================================
    # Generate Complete SEO Pack
    # =====================================================

    def generate_complete_pack(self):

        print("\n================================================")
        print("AI SEO BLOG PACK")
        print("================================================")

        print("\nMETA TITLE:")
        print(self.generate_meta_title())

        print("\nMETA DESCRIPTION:")
        print(self.generate_meta_description())

        print("\nSEO BLOG OUTLINE:")
        outline = self.generate_outline()

        for heading, values in outline.items():

            if isinstance(values, list):

                print(f"\n{heading}")
                for item in values:
                    print("-", item)

            else:
                print(f"\n{heading}")
                print(values)

        print("\nCONTENT CLUSTERS:")
        clusters = self.generate_content_clusters()

        print("\nPillar Topic:")
        print(clusters["Pillar Topic"])

        print("\nCluster Topics:")
        for topic in clusters["Cluster Topics"]:
            print("-", topic)

        print("\nSEO KEYWORDS:")
        for keyword in self.generate_keywords():
            print("-", keyword)

        print("\nINTERNAL LINKS:")
        for link in self.generate_internal_links():
            print("-", link)

        print("\nCTA OPTIONS:")
        for cta in self.generate_ctas():
            print("-", cta)

        print("\nFULL BLOG ARTICLE:")
        print(self.generate_blog())

        print("\nGenerated On:", datetime.now())


# =========================================================
# Example Usage
# =========================================================

seo = SEOContentGenerator(
    business_name="Bright Digital Solutions",
    service="SEO Services",
    city="Hyderabad",
    target_keyword="SEO Services Hyderabad",
    audience="Small Businesses"
)

seo.generate_complete_pack()