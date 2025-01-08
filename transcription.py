import asyncio
from deepgram import Deepgram

# Replace with your Deepgram API key
DEEPGRAM_API_KEY = ''

# Initialize the Deepgram SDK
dg_client = Deepgram(DEEPGRAM_API_KEY)

async def transcribe_audio(file_path):
    # Open the audio file in binary mode
    with open(file_path, 'rb') as audio_file:
        audio_source = {'buffer': audio_file, 'mimetype': 'audio/mp3'}
        response = await dg_client.transcription.prerecorded(audio_source, {'punctuate': True})
        # Extract and return the transcription
        return response['results']['channels'][0]['alternatives'][0]['transcript']

# Path to your audio file
audio_file_path = r"C:\Users\ROG STRIX\OneDrive\Desktop\common_voice_en_41236242.mp3"

# Run the transcription (directly await the coroutine here instead of using asyncio.run)
async def main():
    transcription = await transcribe_audio(audio_file_path)
    print(transcription)

# If you're running this script standalone, use asyncio.run(main()) to kick off the main coroutine
if __name__ == "__main__":
    asyncio.run(main())

