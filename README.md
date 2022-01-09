# Data Analytics Project
Project is build in Python for data analytics course using python and Sentiment Analysis and Emotion Recognition in Italian (using BERT). The aim of the project is to perform sentiment analytics of an Italian sentence.
Python script will read json values from *csv* file, it will predict sentiment foreach line after that a new file is created.

# Pre-requisite
- **TensorFlow**: TensorFlow is a free and open-source software library for machine learning and artificial intelligence. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks. It can be used in a wide variety of programming languages, most notably Python, as well as Javascript, C++, and Java. This flexibility lends itself to a range of applications in many different sectors.
- **BERT**: Bidirectional Encoder Representations from Transformers (BERT) is a transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google. BERT was created and published in 2018 by Jacob Devlin and his colleagues from Google; is it integrate in Tensorflow

# Libraries 
Following python libraries are necessary for the project
- **NumPy**: is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
- **PyTorch** is an open source machine learning library based on the Torch library used for applications such as computer vision and natural language processing.It is free and open-source software released under the Modified BSD license.
PyTorch provides tensor computing (like NumPy) with strong acceleration via graphics processing units (GPU)
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

Python script after read json and load AI model will provide a predic of the sentiment foreach row, then a new json content is create foreach line, below contents are added:

- **tz_sa**: timestamp sentiment evaluation (ISO DATE 8601, es: 2022-01-04T01:30:08+01:00)
- **sentiment**: negative | positive
- **sentiment_value**: percentage sentiment forecast

At the end a new csv file with new json content is created.

