# api_detector/url_patterns.py

def identify_api_url_patterns(url):
    """
    Identify API-related URL patterns.

    Args:
        url (str): The URL to analyze.

    Returns:
        bool: True if the URL matches an API pattern, False otherwise.
    """
    common_api_keywords = ["api", "v1", "endpoint", "rest"]
    url_lower = url.lower()

    # Check if any common API keyword is present in the URL
    for keyword in common_api_keywords:
        if keyword in url_lower:
            return True

    # Add additional conditions or patterns as needed

    return False

# Example Usage:
if __name__ == "__main__":
    example_url = "https://example.com/api/v1/data"
    result = identify_api_url_patterns(example_url)
    print(f"Is API URL: {result}")
