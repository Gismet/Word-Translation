import pandas as pd
from googletrans import Translator

# The file containing the words - specify the full file path
file = "./Book1.xlsx"
df = pd.read_excel(file)

# The translator
translator = Translator()


# Translating each columns 
for column in df.columns:
    df[column] = df[column].apply(lambda x: translator.translate(x, src="en", dest="az").text)

# Saving the words to a new file
df.to_csv("translated_words.csv", index=False)
