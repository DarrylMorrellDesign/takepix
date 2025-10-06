#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget

from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2

from datetime import datetime


picam2 = Picamera2()
picam2.options["compress_level"] = 0 # Don't do any compression on png file
picam2.configure(picam2.create_preview_configuration())

def on_button_clicked():
  button.setEnabled(False)
  cfg = picam2.create_still_configuration()
  current_date_time = datetime.now()
  formatted_time = current_date_time.strftime("%Y-%m-%d-%H-%M-%S")
  file_path = f"Images/Image-{formatted_time}.png"
  picam2.switch_mode_and_capture_file(cfg, file_path, 
        signal_function=qpicamera2.signal_done)

def capture_done(job):
  result = picam2.wait(job)
  
  button.setEnabled(True)

app = QApplication([])
qpicamera2 = QGlPicamera2(picam2, width=800, height=600, keep_ar=False)
button = QPushButton("Click to capture JPEG")
window = QWidget()
qpicamera2.done_signal.connect(capture_done)
button.clicked.connect(on_button_clicked)
layout_v = QVBoxLayout()
layout_v.addWidget(qpicamera2)
layout_v.addWidget(button)
window.setWindowTitle("Qt Picamera2 App")
window.resize(640, 480)
window.setLayout(layout_v)
picam2.start()
window.show()
app.exec()
