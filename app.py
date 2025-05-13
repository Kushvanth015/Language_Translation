from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import custom_object_scope
from tensorflow.keras.layers import Layer

app = Flask(__name__)

# Define a dummy layer for unknown objects
custom_objects = {
    "NotEqual": Layer  # Placeholder for any unknown layer
}

# Load Model & Tokenizers
with custom_object_scope(custom_objects):
    model = tf.keras.models.load_model("translation_model.h5")

with open("tokenizer_en.pkl", "rb") as f:
    tokenizer_en = pickle.load(f)
with open("tokenizer_te.pkl", "rb") as f:
    tokenizer_te = pickle.load(f)

max_len_en = model.input_shape[1]  # Get max sequence length

def translate_text(text):
    sequence = tokenizer_en.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_len_en, padding="post")

    prediction = model.predict(padded_sequence)
    predicted_indices = np.argmax(prediction, axis=-1)[0]

    translated_words = [
        tokenizer_te.index_word.get(idx, "") for idx in predicted_indices if idx != 0
    ]

    # Remove unwanted words like "నిజం"
    translated_words = [word for word in translated_words if word != "నిజం"]
    translated_words = [word for word in translated_words if word != "అంతా"]

    return " ".join(translated_words).strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        translation = translate_text(input_text)
        return jsonify({"input": input_text, "translation": translation})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
