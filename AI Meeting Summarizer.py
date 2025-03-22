from flask import Flask, request, jsonify
import whisper
import openai
import os
import tempfile
import shutil

app = Flask(__name__)

# Load Whisper model (gunakan model kecil agar cepat)
model = whisper.load_model("small")

# Set API Key OpenAI (pastikan Anda menyetel ini dari environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/upload", methods=["POST"])
def upload_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    # Simpan file ke folder sementara
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, file.filename)
        file.save(file_path)
        
        # Transkripsi audio ke teks
        result = model.transcribe(file_path)
        transcript = result["text"]
        
        # Meringkas teks menggunakan GPT
        summary = summarize_text(transcript)
        
        # Buat analisis tambahan
        keywords = extract_keywords(transcript)
        action_items = extract_action_items(transcript)
        
    return jsonify({
        "summary": summary,
        "keywords": keywords,
        "action_items": action_items
    })

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that summarizes meeting transcripts."},
            {"role": "user", "content": f"Ringkas rapat ini dalam 5 poin utama:\n{text}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

def extract_keywords(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Extract the main keywords from the meeting transcript."},
            {"role": "user", "content": f"Ambil kata kunci utama dari teks ini:\n{text}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

def extract_action_items(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Identify key action items from the meeting transcript."},
            {"role": "user", "content": f"Identifikasi item tindakan dari teks ini:\n{text}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    app.run(debug=True)
