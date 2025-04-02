import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QMenuBar, QAction
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer

class QRCodeScanner(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuração da Janela
        self.setWindowTitle("Leitor de QR Code")
        self.setGeometry(100, 100, 600, 500)
        
        # Criar Layout
        layout = QVBoxLayout()
        
        # Criar Menu
        self.menu_bar = QMenuBar(self)
        menu = self.menu_bar.addMenu("Opções")
        sair_action = QAction("Sair", self)
        sair_action.triggered.connect(self.close)
        menu.addAction(sair_action)
        layout.addWidget(self.menu_bar)
        
        # Criar Label para a Câmera
        self.label_camera = QLabel(self)
        layout.addWidget(self.label_camera)
        
        # Criar Label para Exibir Texto do QR Code
        self.label_qrcode = QLabel("QR Code: Nenhum código lido", self)
        layout.addWidget(self.label_qrcode)
        
        # Criar Botões
        self.btn_ler = QPushButton("Ler QR Code", self)
        self.btn_ler.clicked.connect(self.start_scan)
        layout.addWidget(self.btn_ler)
        
        self.btn_sair = QPushButton("Sair", self)
        self.btn_sair.clicked.connect(self.close)
        layout.addWidget(self.btn_sair)
        
        self.setLayout(layout)
        
        # Configuração da Câmera
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.scan_qrcode)
    
    def start_scan(self):
        self.cap = cv2.VideoCapture(0)  # Abrir câmera
        self.timer.start(30)  # Atualizar a cada 30ms
    
    def scan_qrcode(self):
        ret, frame = self.cap.read()
        if ret:
            # Converter para RGB e exibir
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            qt_img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.label_camera.setPixmap(QPixmap.fromImage(qt_img))
            
            # Detectar QR Code
            detector = cv2.QRCodeDetector()
            data, bbox, _ = detector.detectAndDecode(frame)
            if data:
                self.label_qrcode.setText(f"QR Code: {data}")
    
    def closeEvent(self, event):
        self.timer.stop()
        if self.cap:
            self.cap.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeScanner()
    window.show()
    sys.exit(app.exec_())
