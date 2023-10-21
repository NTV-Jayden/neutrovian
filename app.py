from datetime import datetime
import io
import base64
from flask import Flask, request, render_template
import qrcode
import validators
import pytz


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    '''main app'''
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        url = request.form.get("url")
        filename = request.form.get("filename")
        if not validators.url(url):
            return render_template("index.html", message="Not a valid URL", url=url, filename=filename)
        qr = qrcode.QRCode(version=1, box_size=5, border=5)
        qr.add_data(url)
        img = qr.make_image(fill_color='black', back_color='#fbcd08')
        my_timezone = pytz.timezone('Asia/Singapore')
        current_datetime = datetime.now(my_timezone)
        filename = ' - ' + filename.strip() if filename else ''
        filename = current_datetime.strftime('%Y%m%d-%H%M%S') + filename

        img_stream = io.BytesIO()
        img.save(img_stream, 'PNG')
        img_base64 = base64.b64encode(img_stream.getvalue()).decode()
    return render_template("index.html", img_data=img_base64, url=url, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
