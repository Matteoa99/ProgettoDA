# Data Analytics Project
Project build in Python for data analytics course usging python and Sentiment Analysis and Emotion Recognition in Italian (using BERT).
Python script will read json values from csv file, it will predict sentiment foreach line in the file after that a new csv file will create 

Input json content 

- user_id: alphanumeric user id
- uuid: message unique id
- text: message text
- meta1: optional field 
- meta2: optional field

Output json content

- user_id: alphanumeric user id
- uuid: message unique id
- text: message text
- meta1: optional field 
- meta2: optional field
- tz_sa: timestamp sentiment evaluation (ISO DATE 8601, es: 2022-01-04T01:30:08+01:00)
- sentiment: negative|positive
- sentiment_value: percentage sentiment forecast

# pre-requisite
- NumPy: NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
- PyTorch is an open source machine learning library based on the Torch library used for applications such as computer vision and natural language processing.It is free and open-source software released under the Modified BSD license.

PyTorch provides two high-level features:

Tensor computing (like NumPy) with strong acceleration via graphics processing units (GPU)
Deep neural networks built on a type-based automatic differentiation system

- Trasformer:  Transformers (formerly known as pytorch-transformers and pytorch-pretrained-bert) provides thousands of pretrained models to perform tasks on different modalities such as text, vision, and audio.
Transformers provides APIs to quickly download and use those pretrained models on a given text, fine-tune them on your own datasets and then share them with the community on our model hub.
Transformers is backed by the three most popular deep learning libraries — Jax, PyTorch and TensorFlow — with a seamless integration between them. It’s straightforward to train your models with one before loading them for inference with the other.

- Tensorflow: TensorFlow is a free and open-source software library for machine learning and artificial intelligence. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks.[4][5]

- TensorFlow was developed by the Google Brain team for internal Google use in research and production. The initial version was released under the Apache License 2.0 in 2015.[1][9] Google released the updated version of TensorFlow, named TensorFlow 2.0, in September 2019.[10]
TensorFlow can be used in a wide variety of programming languages, most notably Python, as well as Javascript, C++, and Java.[11] This flexibility lends itself to a range of applications in many different sectors.
