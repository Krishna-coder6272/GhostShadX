# modules/public_ip.py

import requests

def get_public_ip_details():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        details = f"""
🔐 Public IP: {data.get('ip')}
🌍 City: {data.get('city')}
📍 Region: {data.get('region')}
🇺🇳 Country: {data.get('country')}
🛰️ Location: {data.get('loc')}
⏰ Timezone: {data.get('timezone')}
🏢 ISP/Org: {data.get('org')}
"""
        return details.strip()
    except Exception as e:
        return f"Error: {e}"
