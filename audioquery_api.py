from fastapi import FastAPI, UploadFile, File, HTTPException
from audioquery import AudioQuery
import pandas as pd
import os

app = FastAPI()

@app.post("/transcribe_audio")
async def transcribe_audio(audio_file: UploadFile = File(...)):
    if audio_file.filename.endswith((".mp3", ".wav")):
        file_name = os.path.splitext(os.path.basename(audio_file.filename))[0]
        audio_query = AudioQuery(audio_file, file_name)
        
        transcript_text = audio_query.transcribe()
        return {"transcript": transcript_text}
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a .mp3 or .wav file")

@app.post("/classify_call")
async def classify_call(audio_file: UploadFile = File(...)):
    if audio_file.filename.endswith((".mp3", ".wav")):
        file_name = os.path.splitext(os.path.basename(audio_file.filename))[0]
        audio_query = AudioQuery(audio_file, file_name)
        
        classification = audio_query.classify_call()
        return {"classification": classification}
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a .mp3 or .wav file")

@app.post("/extract_data")
async def extract_data(audio_file: UploadFile = File(...)):
    if audio_file.filename.endswith((".mp3", ".wav")):
        file_name = os.path.splitext(os.path.basename(audio_file.filename))[0]
        audio_query = AudioQuery(audio_file, file_name)
        
        data = audio_query.extract_data()
        return {"data": data}
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a .mp3 or .wav file")
