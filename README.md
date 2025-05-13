
<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=800&height=70&duration=4000&lines=Hi+There!+👋;+💻Language+Translation💻;&color=ADD8E6&color2=90EE90" />
</h1>

# 🌐 Language Translator (English ↔ Telugu)

A Deep Learning-based Language Translator that converts text between **English and Telugu** using a custom-trained Seq2Seq model with Attention Mechanism. This project includes a web interface built with Flask, HTML, and CSS for an interactive experience.

---

## 🚀 Features

- 🔁 **Bidirectional Translation** (English to Telugu & Telugu to English)
- 🎯 **Seq2Seq LSTM Model** with Attention Mechanism
- 📄 Custom Cleaned Dataset
- 🖥️ Simple & User-Friendly Web Interface (Flask, HTML, CSS)
- 🧠 Model trained and saved using TensorFlow/Keras
- 📦 Easy-to-run Python app

---

## 🖼️ Screenshots

![Screenshot (264)](https://github.com/user-attachments/assets/bb5f2b9b-b3fb-4e64-821a-278d71227911)

![Screenshot (265)](https://github.com/user-attachments/assets/1b5e0995-23f1-4dad-b50d-0adeb8a8edda)


---

## 📂 Project Structure
```
final_project/
│
├── static/ # Static files (CSS/images)
├── templates/ # HTML templates (index.html, result.html, etc.)
├── model/ # Saved model and tokenizer files
├── English-Telugu-Cleaned.csv # Cleaned dataset
├── app.py # Flask backend
├── README.md # Project documentation
└── requirements.txt # Python dependencies
```
---

## 🔧 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kushvanth015/Language_Translation.git
cd Language_Translation
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

python train.py

python app.py
```
---
## 📊 Model Info
Architecture: Seq2Seq using LSTM + Attention

Libraries: TensorFlow, Keras, NumPy, Flask

Dataset: Custom bilingual data (English-Telugu-Cleaned.csv)

Training Flow:

Preprocessing: Lowercasing, punctuation removal

Tokenization: Word-level tokens

Padding and teacher forcing during training

Model saved using .h5 and tokenizer using .pkl


---

## 💡 Future Enhancements
🎙️ Speech input/output using audio APIs

📷 OCR for real-time image-based translation

🌍 Support for more languages (Hindi, Kannada, etc.)

📱 Mobile App integration using React Native or Flutter

---
## 🙌 Acknowledgments
TensorFlow, Keras Docs

NLP and Seq2Seq Tutorials

GitHub open-source community

---
## 🧑‍🤝‍🧑 Team Members:
- **BADISA KUSHVANTH VENKATA KARTHIK (TL)**
- **AVVARU HARICHANDRA PRASAD**
- **KANASANI MANIKANTA**
- **SAGIRAJU NAVEEN VARMA**
- **PARUPALLI YERRAM NAIDU**
---
## 👤 Author
Kushvanth
```
📧 Email: [badisakushvanthvenkatakarthik@gmail.com]
🔗 GitHub: https://github.com/Kushvanth015
```
---
