def generate_content_plan(property_type, location):
    """Generate content marketing plan"""
    
    location_suffix = f" in {location}" if location else ""
    
    blog_topics = f"""Monthly Blog Post Ideas:

Month 1-2: Educational Content
- "Ultimate Guide to Planning Your {property_type} Stay{location_suffix}"
- "10 Things to Pack for Your Vacation Rental"
- "How to Choose the Perfect Vacation Rental"

Month 3-4: Local Content
- "Hidden Gems: Local Attractions Near Our Property"
- "Best Restaurants and Cafes{location_suffix}"
- "Seasonal Events Calendar{location_suffix}"

Month 5-6: Guest Stories
- "Guest Spotlight: Family Reunion Success Story"
- "Why Guests Choose Direct Booking Over Airbnb"
- "Behind the Scenes: How We Prepare for Your Stay"

SEO Tips:
- Target 1,500+ words per post
- Include local keywords naturally
- Add internal links to booking page
- Use high-quality images with alt text"""

    social_media = f"""Platform Strategy:

Instagram (Post 3-4x/week):
- Property photos with local hashtags
- Guest testimonials (with permission)
- Local area highlights
- Behind-the-scenes content
- Stories: daily updates, polls, Q&A

Facebook (Post 2-3x/week):
- Share blog posts
- Local events and news
- Special offers for direct bookings
- Join local tourism groups
- Run targeted ads to travelers searching for {location}

Pinterest:
- Create boards: "Things to Do{location_suffix}", "Packing Tips", "Interior Design"
- Pin blog posts and property photos
- Use keywords in pin descriptions

Key Tactics:
- Offer 10% discount for direct bookings (mention in every post)
- Use location tags on all posts
- Engage with local businesses and tourism accounts
- Run seasonal promotions"""

    review_strategy = f"""Customer Review Generation Plan:

Pre-Stay:
- Send welcome email with property highlights
- Include link to Google Business Profile
- Set expectations for great experience

During Stay:
- Check in 24 hours after arrival
- Provide local recommendations guide
- Be responsive to any issues

Post-Stay (Critical for SEO):
Day 1: Send thank you email
Day 3: Request review with direct links:
  - Google Business Profile (highest priority)
  - TripAdvisor
  - Your website testimonials page

Email Template:
"Thank you for staying with us! We'd love to hear about your experience. 
Your review helps other travelers discover our property and supports our 
small business. As a thank you, we'll send you a 15% discount code for 
your next direct booking."

Review Response Strategy:
- Respond to ALL reviews within 24 hours
- Thank positive reviewers, mention specific details
- Address negative reviews professionally, offer solutions
- Include keywords naturally in responses

Goal: 20+ Google reviews in first 6 months"""

    return {
        "blog_topics": blog_topics,
        "social_media": social_media,
        "review_strategy": review_strategy
    }
