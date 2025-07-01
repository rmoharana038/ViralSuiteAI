import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from utils.video_to_shorts import generate_short_with_captions
from utils.watermark_removal import remove_watermark
from utils.upscale import upscale_media

class ViralSuiteAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ViralSuiteAI")
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        layout = QVBoxLayout()
        
        self.label = QLabel("Welcome to ViralSuiteAI")
        layout.addWidget(self.label)

        btn_shorts = QPushButton("Generate Shorts")
        btn_shorts.clicked.connect(self.generate_shorts)
        layout.addWidget(btn_shorts)

        btn_watermark = QPushButton("Remove Watermark")
        btn_watermark.clicked.connect(self.remove_watermark)
        layout.addWidget(btn_watermark)

        btn_upscale = QPushButton("Upscale Media")
        btn_upscale.clicked.connect(self.upscale)
        layout.addWidget(btn_upscale)

        self.setLayout(layout)

    def generate_shorts(self):
        generate_short_with_captions()

    def remove_watermark(self):
        remove_watermark()

    def upscale(self):
        upscale_media()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ViralSuiteAI()
    win.show()
    sys.exit(app.exec_())

# utils/__init__.py
# empty file to treat 'utils' as a package

# utils/video_to_shorts.py
def generate_short_with_captions():
    print("[Video to Shorts] Generating short clip with captions...")
    # Placeholder for actual Whisper + ffmpeg-based logic

# utils/watermark_removal.py
def remove_watermark():
    print("[Watermark Remover] Auto/manual watermark removal triggered...")
    # Placeholder for OpenCV + inpainting logic

# utils/upscale.py
def upscale_media():
    print("[Upscale] Running Real-ESRGAN on image/video...")
    # Placeholder for ESRGAN upscaling logic
