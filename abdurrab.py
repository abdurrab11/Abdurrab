import requests, json

def facebook_login(uid, password):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    url = f"https://b-api.facebook.com/method/auth.login?email={uid}&password={password}&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    
    try:
        session = requests.Session()
        response = session.get(url, headers=headers)
        print(response.text)  # Debugging purpose
        data = response.json()
        
        if "session_key" in data:
            print(f"[SUCCESS] {uid} | {password}")
        elif "www.facebook.com" in data.get("error_msg", ""):
            print(f"[CHECKPOINT] {uid} | {password}")
        else:
            print(f"[FAILED] {uid} | {password}")
            
    except json.JSONDecodeError:
        print("[ERROR] Invalid Response from API!")
    except requests.exceptions.ConnectionError:
        print("[ERROR] No Internet Connection!")

facebook_login("test@example.com", "password123")