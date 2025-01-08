import requests

def synthesize_voice(text):
    url = "https://api.11labs.io/v1/speech"
    payload = {
        "text": text,
        "voice": "Alice",  # Replace with desired voice name
        "model_id": "standard"  # Optional, use "standard" or "enhanced"
    }
    headers = {
        "Authorization": "Bearer <Replace with your valid API key>",  
        "Content-Type": "application/json"
    }

    try:
        print("Sending request to the API...")
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Request successful, audio data received.")
            return response.content  # Binary audio data
        else:
            print(f"Failed to synthesize audio: {response.status_code}")
            print("Response Text:", response.text)  # Print the error message
            return None
    except Exception as e:
        print(f"Error occurred during the request: {e}")
        return None

if __name__ == "__main__":
    print("Starting synthesis...")
    audio_data = synthesize_voice("This is a test response.")
    
    if audio_data:
        with open("test_audio.wav", "wb") as f:
            f.write(audio_data)
        print("Audio file saved successfully.")
    else:
        print("Audio synthesis failed.")
