from keras.preprocessing.text import Tokenizer
texts = ['The quick brown fox jumped over the lazy dog.', 'I never saw a lazy dog jump over a quick fox.']
tokenizer = Tokenizer(None,  '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\\n',  True,  ' ', char_level=False)
