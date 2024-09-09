import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, Dropout, Add
from tensorflow.keras.models import Model
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from PIL import Image
import matplotlib.pyplot as plt
import pickle

# Load and preprocess the image, extract features
def extract_image_features(image_path):
    model = InceptionV3(weights='imagenet')
    model = Model(model.input, model.layers[-2].output)  # Use the second-to-last layer for features
    img = Image.open(image_path).resize((299, 299))
    img = np.array(img).astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    features = model.predict(img)
    return features

# Generate a caption for an image
def generate_caption(model, tokenizer, image_features, max_length):
    in_text = 'startseq'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)

        # Predict the next word index
        yhat = model.predict([image_features, sequence], verbose=0)
        yhat = np.argmax(yhat)

        # Check if the predicted word index exists in the tokenizer's vocabulary
        if yhat not in tokenizer.index_word:
            print(f"Word index {yhat} not found in tokenizer vocabulary!")
            break

        word = tokenizer.index_word[yhat]
        print(f"Predicted Word Index: {yhat}, Predicted Word: {word}, Sequence so far: {in_text}")  # Debugging output

        # Append the predicted word to the caption
        in_text += ' ' + word

        # Stop if 'endseq' is predicted
        if word == 'endseq':
            break
    return in_text

# Define the image captioning model
def define_model(vocab_size, max_length):
    # Image feature input
    inputs1 = Input(shape=(2048,))
    fe1 = Dropout(0.5)(inputs1)
    fe2 = Dense(256, activation='relu')(fe1)

    # Sequence input
    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = Dropout(0.5)(se1)
    se3 = LSTM(256)(se2)

    # Decoder (combine image features and sequence output)
    decoder1 = Add()([fe2, se3])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax')(decoder2)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Load and preprocess the dataset
def load_data():
    # This is a placeholder for loading your dataset
    # Replace with your own dataset loading code
    captions = [
        'startseq a person is sitting endseq',
        'startseq a person is standing endseq',
        # Add more captions
    ]
    return captions

# Main function to run the captioning system
def main():
    # Load dataset and fit tokenizer
    captions = load_data()
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(captions)
    vocab_size = len(tokenizer.word_index) + 1
    max_length = max(len(caption.split()) for caption in captions)

    # Define and compile the model
    model = define_model(vocab_size, max_length)

    # Load pre-trained model weights (if applicable)
    # model.load_weights('path_to_your_trained_model_weights.h5')

    # Load tokenizer (if saved separately)
    # with open('path_to_your_tokenizer.pkl', 'rb') as handle:
    #     tokenizer = pickle.load(handle)

    # Load and preprocess the image, extract features
    image_path = 'your_image.jpg'  # Replace with your image path
    image_features = extract_image_features(image_path)

    # Generate a caption for the image
    caption = generate_caption(model, tokenizer, image_features, max_length)
    print("Generated Caption:", caption)

    # Plot the image
    img = Image.open(image_path)
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    main()
