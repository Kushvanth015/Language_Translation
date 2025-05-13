import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load dataset
df = pd.read_csv("English-Telugu.csv")  # Ensure CSV has 'English' and 'Telugu' columns

# Convert to string
english_sentences = df["English"].astype(str).tolist()
telugu_sentences = df["Telugu"].astype(str).tolist()

# Tokenization
tokenizer_en = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n')  # Remove punctuation
tokenizer_te = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n')
tokenizer_en.fit_on_texts(english_sentences)
tokenizer_te.fit_on_texts(telugu_sentences)

sequences_en = tokenizer_en.texts_to_sequences(english_sentences)
sequences_te = tokenizer_te.texts_to_sequences(telugu_sentences)

# Determine max sequence length
max_len = max(
    max(len(seq) for seq in sequences_en),
    max(len(seq) for seq in sequences_te)
)

# Padding
padded_en = pad_sequences(sequences_en, maxlen=max_len, padding="post")
padded_te = pad_sequences(sequences_te, maxlen=max_len, padding="post")

# Vocabulary sizes
vocab_size_en = len(tokenizer_en.word_index) + 1
vocab_size_te = len(tokenizer_te.word_index) + 1

# Define Model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size_en, output_dim=256, mask_zero=True),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(256, return_sequences=True)),
    tf.keras.layers.Dense(vocab_size_te, activation="softmax")
])

# Compile Model
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# Train Model
model.fit(padded_en, padded_te, epochs=50, batch_size=32, validation_split=0.2)

# Save Model & Tokenizers
model.save("translation_model.h5")
with open("tokenizer_en.pkl", "wb") as f:
    pickle.dump(tokenizer_en, f)
with open("tokenizer_te.pkl", "wb") as f:
    pickle.dump(tokenizer_te, f)

print("✅ Training complete and model saved.")