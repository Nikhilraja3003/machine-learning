import requests
import os

# Set your API key and endpoint
OPENROUTER_API_KEY = "OPENROUTER_API_KEY"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def translate_text(input_text):
    try:
        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are an expert in ancient Tamil manuscript interpretation."},
                {"role": "user", "content": f"""Please translate the following ancient Tamil text into:
1. Modern Tamil
2. English

Text:
\"\"\"{input_text}\"\"\""""}
            ]
        }

        response = requests.post(OPENROUTER_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        reply = response.json()
        output = reply["choices"][0]["message"]["content"]
        return output

    except Exception as e:
        print(f"[❌] Translation failed: {e}")
        return None


# Test (Optional)
if __name__ == "__main__":
    sample_text = "ம 21 ர வ ய பவ இஸ. ௧ டும்‌ ரா 0 2440 0 படி பிய பவி."
    result = translate_text(sample_text)
    if result:
        print("\n🔤 Translations:\n", result)
