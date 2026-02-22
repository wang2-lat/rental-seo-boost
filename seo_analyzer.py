import requests
from bs4 import BeautifulSoup

def analyze_seo_health(url):
    """Analyze SEO health of a website"""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = {}
        recommendations = []
        
        # Check title tag
        title = soup.find('title')
        if title and len(title.text.strip()) > 0:
            title_length = len(title.text.strip())
            results["Title Tag"] = {
                "passed": 30 <= title_length <= 60,
                "message": f"Length: {title_length} chars (optimal: 30-60)"
            }
            if title_length < 30:
                recommendations.append("Title tag is too short. Include location and property type")
            elif title_length > 60:
                recommendations.append("Title tag is too long. Keep it under 60 characters")
        else:
            results["Title Tag"] = {"passed": False, "message": "Missing"}
            recommendations.append("Add a descriptive title tag with location and property type")
        
        # Check meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            desc_length = len(meta_desc['content'])
            results["Meta Description"] = {
                "passed": 120 <= desc_length <= 160,
                "message": f"Length: {desc_length} chars (optimal: 120-160)"
            }
            if desc_length < 120:
                recommendations.append("Meta description is too short. Add more details about amenities and location")
        else:
            results["Meta Description"] = {"passed": False, "message": "Missing"}
            recommendations.append("Add meta description highlighting unique features and location")
        
        # Check H1 tags
        h1_tags = soup.find_all('h1')
        results["H1 Tags"] = {
            "passed": len(h1_tags) == 1,
            "message": f"Found {len(h1_tags)} (optimal: 1)"
        }
        if len(h1_tags) == 0:
            recommendations.append("Add one H1 tag with main property description")
        elif len(h1_tags) > 1:
            recommendations.append("Use only one H1 tag per page")
        
        # Check mobile viewport
        viewport = soup.find('meta', attrs={'name': 'viewport'})
        results["Mobile Viewport"] = {
            "passed": viewport is not None,
            "message": "Present" if viewport else "Missing"
        }
        if not viewport:
            recommendations.append("Add viewport meta tag for mobile optimization")
        
        # Check images with alt text
        images = soup.find_all('img')
        images_with_alt = [img for img in images if img.get('alt')]
        alt_ratio = len(images_with_alt) / len(images) if images else 0
        results["Image Alt Text"] = {
            "passed": alt_ratio >= 0.8,
            "message": f"{len(images_with_alt)}/{len(images)} images have alt text"
        }
        if alt_ratio < 0.8:
            recommendations.append("Add descriptive alt text to all images for better SEO")
        
        results["recommendations"] = recommendations
        return results
        
    except requests.RequestException as e:
        return {"error": f"Failed to fetch URL: {str(e)}"}
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}
