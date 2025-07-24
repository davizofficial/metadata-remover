# 🛡️ Metadata Remover

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/Security-Privacy-red">
</p>

Tool to remove metadata from files (images, documents, PDF) that may contain sensitive information such as GPS location, user names, computer paths, etc.

## 🌟 Key Features

- 🖼️ **Images**: JPG, JPEG, PNG
- 📄 **Documents**: PDF
- 🔍 **Metadata Analysis**: View sensitive information
- 🧹 **Metadata Removal**: Clean files thoroughly
- 🗺️ **GPS Detection**: Find location coordinates
- 🌍 **Google Maps Integration**: View location on map
- 📱 **Device Info**: Identify camera/software
- ✨ **Attractive Display**: User-friendly interface

## 🚀 Installation

### Prerequisites
- Python 3.7 or newer
- Pip (Python package installer)

### Installation Steps

1. **Clone repository**
```bash
git clone https://github.com/davizofficial/metadata-remover.git
cd metadata-remover
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Verify installation**
```bash
python main.py -h
```

## 📖 Usage

### View Metadata
```bash
# View image file metadata
python main.py -f photo.jpg --view

# View metadata with automatic Google Maps link
python main.py -f photo.jpg --view --map

# View PDF file metadata
python main.py -f document.pdf --view
```

### Remove Metadata
```bash
# Remove image file metadata
python main.py -f photo.jpg --remove

# Remove metadata with custom output name
python main.py -f photo.jpg --remove -o clean_photo.jpg

# Remove PDF file metadata
python main.py -f document.pdf --remove -o clean_document.pdf
```

### Available Parameters
- `-f, --file` : Path to file to be processed (required)
- `-v, --view` : View metadata only
- `-r, --remove` : Remove metadata
- `-o, --output` : Output file name (optional)
- `-m, --map` : Display and open Google Maps link for GPS location
- `-h, --help` : Display help

## 🎯 Detected Information

### 📸 Images (JPG, JPEG, PNG):
- 📍 **GPS Location** (Latitude/Longitude/Altitude)
- 🌍 **Google Maps Link** for GPS location
- 📱 **Device** (Camera brand/model)
- 📷 **Camera Model**
- 📅 **Capture Date**
- ⏱️ **Digitization Date**
- ⚙️ **Technical Info** (ISO, Aperture, Shutter Speed, Focal Length)
- 👤 **Creator/Copyright**
- 💻 **Software Used**

### 📄 PDF:
- 📌 **Document Title**
- 👤 **Author**
- 📝 **Subject**
- 🏗️ **Creator Software**
- 🖨️ **Producer Software**
- 📅 **Creation Date**
- ✏️ **Modification Date**
- 🔑 **Keywords**
- 🎯 **Trapped Status**

## 📁 Project Structure

```
metadata-remover/
├── main.py              # Application entry point
├── metadata_handler.py  # Main handler for file management
├── image_processor.py   # Process images and image metadata
├── pdf_processor.py     # Process PDFs and PDF metadata
├── requirements.txt     # Required dependencies
└── README.md           # Documentation
```

## 🛡️ Sample Output

### Viewing Image Metadata Output:
```
================================================================================
🛡️  Metadata Remover - Protect Your Privacy! 🛡️
================================================================================

📁 File: vacation_photo.jpg
📊 Type: .JPG
--------------------------------------------------
🔍 Analyzing metadata...

🔍 METADATA ANALYSIS RESULTS
==================================================
📄 File Name: vacation_photo.jpg
📊 Dimensions: 4032 x 3024 pixels
🎨 Mode: RGB

🔹 📱 Device: Apple
🔹 📷 Camera Model: iPhone 12
🔹 📅 Capture Date: 2023:12:25 14:30:45
🔹 📍 Coordinates: -6.208800, 106.845600
🔗 Google Maps: https://www.google.com/maps?q=-6.208800,106.845600

⚙️  Technical Information:
   • ⏱️ Exposure Time: 1/200
   • 🔢 Aperture: f/1.6
   • 🎛️ ISO: 25
```

### Metadata Removal Output:
```
================================================================================
🛡️  Metadata Remover - Protect Your Privacy! 🛡️
================================================================================

📁 File: secret_photo.jpg
📊 Type: .JPG
--------------------------------------------------
⚙️  Processing metadata removal...
🧹 Removing metadata...
✅ Metadata successfully removed!
💾 File saved as: secret_photo_clean.jpg

🔍 Verification results...
✅ Verification successful - no metadata remaining
```

## 🗺️ Google Maps Integration Feature

This feature allows you to:
- **View GPS location** in an easy-to-read format
- **Get Google Maps link** directly from coordinates
- **Automatically open location** in browser with `--map` flag
- **Verify location** easily through interactive map

### How to Use Google Maps Feature:
```bash
# View metadata and display Google Maps link
python main.py -f photo_with_gps.jpg --view

# View metadata and automatically open Google Maps
python main.py -f photo_with_gps.jpg --view --map
```

## 🔧 Troubleshooting

### Common Issues:

**1. "ModuleNotFoundError" Error**
```
Solution: Make sure you've run `pip install -r requirements.txt`
```

**2. "File not found" Error**
```
Solution: Check the file path you entered
```

**3. "Unsupported file format" Error**
```
Solution: Ensure file has extension JPG, JPEG, PNG, or PDF
```

**4. No metadata found**
```
Solution: File genuinely has no metadata or metadata already removed
```

## 📌 How to Contribute

1. Fork this repository
2. Create new branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

### Contribution Areas:
- Adding support for new file formats
- Improving interface display
- Adding data export features
- Improving metadata detection
- Adding documentation

## 🎯 Features That Can Be Added

- [ ] Support for video/audio formats (MP4, AVI, MOV, MP3)
- [ ] Simple GUI with tkinter or PyQt
- [ ] Batch processing for multiple files
- [ ] Verification that metadata is completely removed
- [ ] Support for DOCX, XLSX, PPTX formats
- [x] **Google Maps integration for GPS location** ✅
- [ ] Export results to CSV/JSON/XML format
- [ ] Detect and remove metadata from video files
- [ ] Silent mode for script integration
- [ ] Activity logging for metadata removal

## 🔒 Security and Privacy

### Why Remove Metadata?
File metadata can contain sensitive information such as:
- Geographic location where photo was taken
- Device information used
- User/creator names
- Creation/modification dates and times
- Computer directory paths
- Company or organization information

### How This Tool Works:
1. **Analysis**: Reads all available metadata
2. **Extraction**: Identifies sensitive information
3. **Removal**: Removes metadata from original file
4. **Verification**: Ensures metadata has been removed
5. **Storage**: Saves clean file without metadata

## ⚠️ Disclaimer

This tool is for educational purposes and personal privacy protection only.
- Use this tool responsibly
- Ensure you have rights to process the files
- Creator is not responsible for misuse of this tool
- Always backup original files before processing

## 📋 License

MIT License

Copyright (c) 2024 Metadata Remover

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files ("Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 📞 Contact

If you have questions, suggestions, or issues:
- Create issue on GitHub repository
- Email: davizarvaputra@gmail.com
- Linkedin: Davis Arva Putra

## 🙏 Acknowledgements

Thanks to:
- Python and Open Source community
- Pillow, PyPDF2, and exifread libraries
- All contributors and users

---
Made with ❤️ for Privacy Protection
```
