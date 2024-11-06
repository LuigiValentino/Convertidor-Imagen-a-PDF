from flask import Flask, request, send_file, render_template
import img2pdf
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image_file = request.files.get("image")

        if not image_file:
            return "Por favor, sube una imagen", 400

        pdf_bytes = BytesIO(img2pdf.convert(image_file.read()))
        pdf_bytes.seek(0)
        return send_file(pdf_bytes, as_attachment=True, download_name="converted.pdf", mimetype="application/pdf")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
