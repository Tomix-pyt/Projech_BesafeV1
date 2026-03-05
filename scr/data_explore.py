import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import models
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Embedding,LSTM,Dense,Dropout,Bidirectional
from tensorflow.keras.optimizers import Adam
from src.test import clean_text
import re
from src.test import clean_text

# LOAD DATA
DATA_PATH =''

data =pd.read_csv(DATA_PATH)

data['Label'].value_counts()
data['Text'].value_counts()