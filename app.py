from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    if request.method == "POST":
        # Parsing parameter dari form
        nama = request.form.get("nama")
        if nama:
            hasil = f"Halo, {nama}! Data berhasil diparsing lewat POST."
        else:
            hasil = "Nama tidak boleh kosong!"

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)