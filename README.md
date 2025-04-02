- Aqui estão alguns módulos populares em Python para escanear QR Codes:  

### 1. **OpenCV (`opencv-python`)**  
   - Pode ser usado para capturar imagens da câmera e detectar QR Codes.  
   - Requer `cv2.QRCodeDetector()`.  
   - Instalação:  
     ```bash
     pip install opencv-python
     ```

### 2. **Pyzbar (`pyzbar`)**  
   - Usa a biblioteca `ZBar` para ler QR Codes e outros códigos de barras.  
   - Funciona com imagens estáticas e vídeo.  
   - Instalação:  
     ```bash
     pip install pyzbar
     ```

### 3. **Zxing (`zxing`)**  
   - Interface Python para a biblioteca `ZXing` do Google.  
   - Suporta QR Code e outros códigos de barras.  
   - Instalação:  
     ```bash
     pip install zxing
     ```

### 4. **QRCode Reader (`qreader`)**  
   - Um módulo baseado em `OpenCV` e `pyzbar`, especializado em leitura de QR Codes.  
   - Instalação:  
     ```bash
     pip install qreader
     ```

### 5. **Pillow + qrtools**  
   - `qrtools` funciona com `Pillow` para processar imagens QR.  
   - Instalação:  
     ```bash
     pip install pillow
     ```
- programa usando **PyQt5** e **OpenCV** para criar uma aplicação gráfica que lê **QR Codes** da câmara. O programa terá:  

✅ Uma **janela PyQt5** com **botões** e **menu**.  
✅ Um botão **"Ler QR Code"** para ativar a câmara.  
✅ Exibição da **imagem da câmara** e do **QR Code** detectado.  
✅ Um botão **"Sair"** para fechar a aplicação.  
✅ Exibição do **texto decifrado do QR Code**.  

---

### 🛠 **Passo 1: Instalar as Dependências**  
Se ainda não tiver instalado, execute:  
```bash
pip install pyqt5 opencv-python numpy
```
### 📝 **Explicação do Código**  
1. **Criação da Janela:**  
   - Usamos `QWidget` para criar a janela principal.  
   - `QVBoxLayout()` organiza os elementos verticalmente.  
   - Criamos um **menu** com a opção de **sair**.  

2. **Integração com a Câmera:**  
   - `cv2.VideoCapture(0)` abre a câmara.  
   - `QTimer` chama `scan_qrcode()` a cada 30ms.  
   - `cv2.cvtColor()` converte a imagem para RGB.  

3. **Detecção do QR Code:**  
   - `cv2.QRCodeDetector()` detecta QR Codes no frame.  
   - Se encontrar um QR Code, exibe o **texto decifrado**.  

4. **Fechar a Aplicação:**  
   - `closeEvent()` fecha a câmera corretamente ao sair.  

---

### 🎯 **Como Usar**  
1️⃣ **Executar o script Python.**  
2️⃣ **Clicar no botão "Ler QR Code"** para iniciar a câmara.  
3️⃣ **Apontar um QR Code** para a câmara.  
4️⃣ O texto do QR Code será **exibido na interface**.  
5️⃣ **Clicar em "Sair"** para fechar a aplicação.
