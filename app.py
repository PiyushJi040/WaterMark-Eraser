from flask import Flask, render_template, request, send_file, jsonify
import fitz
import os
from werkzeug.utils import secure_filename
import io
import traceback

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_pdf():
    input_path = None
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400
        
        method = request.form.get('method', 'crop')
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_path)
        
        output = io.BytesIO()
        doc = fitz.open(input_path)
        
        if method == 'crop':
            top = int(request.form.get('crop_top', 0))
            bottom = int(request.form.get('crop_bottom', 30))
            left = int(request.form.get('crop_left', 0))
            right = int(request.form.get('crop_right', 0))
            for page in doc:
                r = page.rect
                page.set_cropbox(fitz.Rect(r.x0 + left, r.y0 + top, r.x1 - right, r.y1 - bottom))
        
        elif method == 'text':
            keywords = request.form.get('keywords', '').split(',')
            for page in doc:
                for kw in keywords:
                    kw = kw.strip()
                    if kw:
                        for area in page.search_for(kw):
                            page.add_redact_annot(area, fill=(1, 1, 1))
                        page.apply_redactions()
        
        elif method == 'image':
            threshold = float(request.form.get('threshold', 0.5))
            for page in doc:
                for img in page.get_images():
                    bbox = page.get_image_bbox(img)
                    if (bbox.width * bbox.height) / (page.rect.width * page.rect.height) < threshold:
                        page.add_redact_annot(bbox, fill=(1, 1, 1))
                page.apply_redactions()
        
        elif method == 'pages':
            pages_str = request.form.get('pages', 'all')
            bottom = int(request.form.get('crop_bottom', 30))
            pages_to_crop = range(len(doc)) if pages_str == 'all' else [int(p.strip()) - 1 for p in pages_str.split(',')]
            for i, page in enumerate(doc):
                if i in pages_to_crop:
                    r = page.rect
                    page.set_cropbox(fitz.Rect(r.x0, r.y0, r.x1, r.y1 - bottom))
        
        doc.save(output)
        doc.close()
        
        if input_path and os.path.exists(input_path):
            os.remove(input_path)
        
        output.seek(0)
        return send_file(output, mimetype='application/pdf', as_attachment=True, download_name='cleaned.pdf')
    
    except Exception as e:
        if input_path and os.path.exists(input_path):
            os.remove(input_path)
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
