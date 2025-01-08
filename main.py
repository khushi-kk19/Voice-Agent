from fastapi import FastAPI, UploadFile, File
from transcription import transcribe_audio  # Import your transcription module
from llm_task import generate_response  # Import your LLM response generation module
from tts import synthesize_voice  # Import your TTS synthesis module
from fastapi.responses import FileResponse
import os

# Initialize FastAPI app
app = FastAPI()

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    try:
        # Step 1: Transcription
        audio_data = await file.read()  # Read the uploaded file's content
        transcription = await transcribe_audio(audio_data)  # Get transcription from the audio

        # Step 2: LLM Response
        response_text = generate_response(transcription)  # Generate response from the transcription

        # Step 3: Text-to-Speech
        audio_response = synthesize_voice(response_text)  # Convert response text to speech

        # Save audio to a file
        output_file = "response_audio.wav"
        with open(output_file, "wb") as f:
            f.write(audio_response)  # Write the binary audio data to the file

        return FileResponse(output_file, media_type="audio/wav", filename="response_audio.wav")

    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "Welcome to the Real-Time Voice Agent API!"}


