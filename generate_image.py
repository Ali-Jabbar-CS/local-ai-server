import requests

# Example prompt
prompt = "cinematic cyberpunk city at night, ultra realistic, rain reflections"

url = "http://127.0.0.1:8188/prompt"

payload = {
    "prompt": prompt
}

try:
    response = requests.post(url, json=payload)
    print("Image generation request sent.")
    print(response.text)
except Exception as e:
    print("Error:", e)
