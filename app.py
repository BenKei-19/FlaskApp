from flask import Flask, render_template, request, send_from_directory
from PIL import Image
import os
from ultralytics import YOLO

app = Flask(__name__)

# Thêm route cho favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                              'favicon.ico', mimetype='image/vnd.microsoft.icon')

model = YOLO('models/best.pt')
model.eval()

os.makedirs('static/Images', exist_ok=True)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/Images', filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['imagefile']
        filename = image_file.filename
        image_path = os.path.join('static/Images', filename)
        image_file.save(image_path)

        results = model(image_path)
        result_image = results[0].plot()
        result_image_rgb = result_image[..., ::-1]
        result_pil = Image.fromarray(result_image)
        output_path = os.path.join('static/Images', 'result_' + filename)
        result_pil.save(output_path)

        return render_template('index.html', image_url='/images/result_' + filename)

    return render_template('index.html')
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080)) 
    app.run(host="0.0.0.0", port=port)