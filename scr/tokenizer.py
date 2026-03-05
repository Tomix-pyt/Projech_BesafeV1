from tokenizers import Tokenizer
import pandas as pd
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from tokenizers.pre_tokenizers import Whitespace

tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()

trainer = WordLevelTrainer(
    special_tokens=["[UNK]", "[PAD]"],
    min_frequency=2
)

DATA_PATH ='finalLargeDs.csv'


# x_train =data['Text']
# x_train.to_csv("train_text.txt", index=False, header=False)
data = pd.read_csv('train_text.txt')

tokenizer.train(files=['train_text.txt'], trainer=trainer)

tokenizer.save("tokenizers/tokenizer.json")