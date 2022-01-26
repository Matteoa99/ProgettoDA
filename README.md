# Data Analytics Project - italian sentiment analytics
Project is built in Python for data analytics course using a library for **Sentiment Analysis and Emotion Recognition in Italian**. The aim of the project is to perform sentiment analytics of an Italian sentence read *json* value from *csv* file, it will predict sentiment foreach line after that a new file is created.

# Pre-requisite
- **BERT**: Bidirectional Encoder Representations from Transformers (BERT) is a transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google. BERT can consider at the same time all the words present in that same sentence, therefore in a bidirectional way.

# Model
[Feel-it-italian-sentiment model](https://huggingface.co/MilaNLProc/feel-it-italian-sentiment) performs sentiment analysis on Italian. They fine-tuned the [UmBERTo model](https://huggingface.co/Musixmatch/umberto-commoncrawl-cased-v1) on their new dataset (i.e., FEEL-IT) obtaining state-of-the-art performances on different benchmark corpora.

# Python libraries 
Following python libraries are necessary for the project
- **NumPy**: is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
- **PyTorch**: is an open source machine learning library based on the Torch library used for applications such as computer vision and natural language processing.It is free and open-source software released under the Modified BSD license.
PyTorch provides tensor computing (like NumPy) with strong acceleration via graphics processing units (GPU).
- **Trasformer**: provides thousands of pretrained models to perform tasks on different modalities such as text, vision, and audio.
Transformers provides APIs to quickly download and use those pretrained models on a given text, fine-tune them on your own datasets and then share them with the community on our model hub.
Transformers is backed by the three most popular deep learning libraries — Jax, PyTorch and TensorFlow — with a seamless integration between them.

# Usage
User can provide to the script a csv file in which each line is a json content structure as below:

- **user_id**: alphanumeric user id
- **uuid**: message unique id
- **text**: message text
- **meta1**: optional field 
- **meta2**: optional field

Python script after read json and load AI model will predic sentiment foreach row, then a new json content is create foreach line, below contents are added:

- **tz_sa**: timestamp sentiment evaluation (ISO DATE 8601, es: 2022-01-04T01:30:08+01:00)
- **sentiment**: negative | positive
- **sentiment_value**: percentage sentiment forecast

At the end a new csv file with new json content is created.

