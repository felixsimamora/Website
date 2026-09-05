app.py

from flask import Flask, render_template

app = Flask(__name__)

tips = [
    {
        "judul": "Hemat Listrik",
        "isi": "Matikan lampu dan alat elektronik jika tidak digunakan."
    },
    {
        "judul": "Gunakan Transportasi Ramah Lingkungan",
        "isi": "Berjalan kaki, bersepeda, atau menggunakan transportasi umum."
    },
    {
        "judul": "Kurangi Sampah",
        "isi": "Gunakan barang yang bisa dipakai kembali dan lakukan daur ulang."
    },
    {
        "judul": "Menanam Pohon",
        "isi": "Pohon membantu menyerap karbon dioksida dari atmosfer."
    },
    {
        "judul": "Hemat Air",
        "isi": "Gunakan air secukupnya dan jangan membiarkan keran terbuka."
    }
]

@app.route("/")
def home():
    return render_template("index.html", tips=tips)


@app.route("/tip/<int:index>")
def detail(index):
    if index < 0 or index >= len(tips):
        return "Tips tidak ditemukan", 404

    tip = tips[index]
    return render_template("detail.html", tip=tip)


app.run(debug=True)
