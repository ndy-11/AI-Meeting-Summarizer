#AI Meeting Summarizer

##Deskripsi

AI Meeting Summarizer adalah aplikasi yang secara otomatis mentranskripsi dan meringkas poin-poin penting dari rekaman rapat. Aplikasi ini menggunakan Whisper untuk transkripsi audio dan GPT-4 untuk menganalisis serta menampilkan ringkasan, kata kunci, dan item tindakan dari rapat.

###Fitur

- **Transkripsi Audio ke Teks**: Menggunakan model Whisper untuk mengubah audio menjadi teks.

- **Ringkasan Rapat Otomatis**: AI merangkum rapat dalam 5 poin utama.

- **Ekstraksi Kata Kunci**: Mengambil kata kunci utama dari transkrip.

- **Identifikasi Item Tindakan**: Menemukan tugas atau tindakan yang harus dilakukan setelah rapat.

- **Dukungan Multi-Bahasa**: Mampu menganalisis berbagai bahasa tergantung pada input audio.

###Cara Menggunakan

  1.**Instalasi**
```sh
git clone https://github.com/username/ai-meeting-summarizer.git
cd ai-meeting-summarizer
pip install -r requirements.txt
```
2. **Konfigurasi**

- Pastikan **API Key OpenAI** sudah disiapkan.

- Setel **environment** variable:
```sh
export OPENAI_API_KEY="your_api_key"
```

3. **Menjalankan Aplikasi**
```sh
python app.py
```

4. **Mengunggah File Audio**

- Gunakan cURL atau Postman untuk mengunggah file audio:
```sh
curl -X POST -F "file=@meeting.mp3" http://127.0.0.1:5000/upload
```
5. Hasil Output

Aplikasi akan mengembalikan ringkasan rapat dalam format JSON seperti berikut:
```sh
{
  "summary": "Rapat membahas strategi pemasaran baru...",
  "keywords": "strategi, pemasaran, anggaran",
  "action_items": "Tim perlu mengajukan laporan pada Jumat."
}
```
###Teknologi yang Digunakan

- **Backend**: Flask

- **Transkripsi Audio**: Whisper

- **AI Processing**: OpenAI GPT-4

- **Database (Opsional)**: MongoDB atau PostgreSQL untuk menyimpan riwayat ringkasan

###Kontribusi

Jika ingin berkontribusi, silakan lakukan fork dan pull request di repository ini.

###Lisensi

Proyek ini dilisensikan di bawah MIT License.

