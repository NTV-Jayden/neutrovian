from datetime import datetime
import io
from flask import Flask, request, render_template, send_file
import qrcode


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    '''main app'''
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        url = request.form.get("url")
        img = qrcode.make(url)
        current_datetime = datetime.now()
        filename = current_datetime.strftime('%Y%m%d-%H%M')

        img_stream = io.BytesIO()
        img.save(img_stream, 'PNG')
        img_stream.seek(0)

        return send_file(img_stream, mimetype='image/png', as_attachment=True,
                         download_name=f'{filename}.png')

if __name__ == "__main__":
    app.run()
