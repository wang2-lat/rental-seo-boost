def generate_local_seo_suggestions(location, business_name):
    """Generate local SEO optimization suggestions"""
    
    google_business = f"""1. Claim your Google Business Profile for '{business_name}'
2. Add complete business information:
   - Exact address in {location}
   - Phone number and website URL
   - Business hours and check-in times
3. Select category: 'Vacation Home Rental' or 'Holiday Apartment'
4. Upload high-quality photos (minimum 10):
   - Exterior shots
   - Each room
   - Amenities (pool, kitchen, etc.)
   - Local attractions nearby
5. Encourage guests to leave Google reviews after checkout
6. Respond to all reviews within 24 hours"""

    local_keywords = f"""Target these local keywords in your content:

Primary Keywords:
- "vacation rental in {location}"
- "{location} holiday home"
- "short term rental {location}"
- "vacation home {location}"

Long-tail Keywords:
- "pet friendly vacation rental {location}"
- "family vacation home {location}"
- "{location} rental with pool"
- "beachfront rental {location}" (if applicable)

Use these in:
- Page titles and H1 tags
- Meta descriptions
- Image alt text
- Blog post content
- URL slugs"""

    map_integration = f"""1. Embed Google Maps on your website:
   - Show exact property location
   - Highlight nearby attractions (beaches, restaurants, shopping)
   
2. Create location pages:
   - "Things to do in {location}"
   - "Best restaurants near our rental"
   - "Local events calendar"
   
3. Add structured data (Schema.org):
   - LocalBusiness schema
   - VacationRental schema
   - Include coordinates, address, ratings
   
4. Get listed on local directories:
   - TripAdvisor
   - Yelp
   - Local tourism board websites
   - {location} vacation rental associations"""

    return {
        "google_business": google_business,
        "local_keywords": local_keywords,
        "map_integration": map_integration
    }
