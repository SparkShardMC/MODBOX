def process_google_oauth(email, provider_id, profile_icon):
    return {
        "provider": "google",
        "email": email,
        "provider_id": provider_id,
        "icon": profile_icon
    }

def process_microsoft_oauth(email, provider_id, profile_icon):
    return {
        "provider": "microsoft",
        "email": email,
        "provider_id": provider_id,
        "icon": profile_icon
    }

def process_apple_oauth(email, provider_id, profile_icon):
    return {
        "provider": "apple",
        "email": email,
        "provider_id": provider_id,
        "icon": profile_icon
    }
