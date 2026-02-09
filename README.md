# 🎨 WaterMark Eraser

A powerful Flask web application to remove watermarks from PDF files using multiple dynamic methods.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌐 Live Demo

**Try it now:** [https://watermark-eraser.onrender.com](https://watermark-eraser.onrender.com)

> Note: Free tier may take 30-60 seconds to wake up on first request

## ✨ Features

- **🔲 Crop Edges** - Remove watermarks by cropping from top, bottom, left, or right (0-200px)
- **📝 Remove Text** - Search and remove specific text watermarks by keywords
- **🖼️ Remove Images** - Remove small images/logos based on size threshold
- **📄 Selective Pages** - Apply cropping only to specific pages or all pages
- **🎯 Drag & Drop** - Easy file upload with drag and drop support
- **⚡ Real-time Controls** - Interactive sliders with live value display
- **✅ Success Feedback** - Visual confirmation when processing completes
- **🚀 Instant Download** - Processed PDF downloads automatically

## 🖥️ Demo

![App Screenshot](https://via.placeholder.com/800x400?text=WaterMark+Eraser+Demo)

## 📋 Requirements

- Python 3.8+
- Flask 3.0.0
- PyMuPDF 1.26.7+
- Werkzeug 3.0.1

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/PiyushJi040/WaterMark-Eraser.git
cd WaterMark-Eraser
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## 📖 Usage

### Method 1: Crop Edges
1. Upload your PDF file
2. Select "Crop Edges" method
3. Adjust sliders for Top, Bottom, Left, Right margins
4. Click "Remove Watermark"

### Method 2: Remove Text
1. Upload your PDF file
2. Select "Remove Text" method
3. Enter keywords separated by commas (e.g., "CONFIDENTIAL, DRAFT")
4. Click "Remove Watermark"

### Method 3: Remove Images
1. Upload your PDF file
2. Select "Remove Images" method
3. Set threshold percentage (removes images smaller than % of page)
4. Click "Remove Watermark"

### Method 4: Selective Pages
1. Upload your PDF file
2. Select "Selective Pages" method
3. Enter page numbers (e.g., "1,3,5") or "all"
4. Adjust crop amount
5. Click "Remove Watermark"

## 📁 Project Structure

```
WaterMark-Eraser/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── LICENSE               # MIT License
├── templates/
│   └── index.html        # Web interface
└── uploads/              # Temporary upload folder (auto-created)
```

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **PDF Processing**: PyMuPDF (fitz)
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Werkzeug

## ⚙️ Configuration

You can modify these settings in `app.py`:

```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Max file size: 50MB
UPLOAD_FOLDER = 'uploads'  # Temporary upload directory
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Piyush Ji**

- GitHub: [@PiyushJi040](https://github.com/PiyushJi040)

## 🙏 Acknowledgments

- PyMuPDF for excellent PDF processing capabilities
- Flask for the lightweight web framework
- All contributors who help improve this project

## ⚠️ Disclaimer

This tool is for legitimate use only. Please respect copyright laws and only remove watermarks from documents you own or have permission to modify.

## 📧 Support

If you have any questions or issues, please open an issue on GitHub.

---

⭐ Star this repository if you find it helpful!
