from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

def lemmanzation(text_list):
    wnl = WordNetLemmatizer()
    res = []
    for text in text_list:
        text_t=[]
        for word in text.split(' '):
            text_t.append(wnl.lemmatize(word))
        res.append(' '.join(text_t))
    return res
#词干提取
def stemming(text_list):
    stemmer = SnowballStemmer("english")  # 选择语言
    res = []
    for text in text_list:
        text_t=[]
        for word in text.split(' '):
            text_t.append(stemmer.stem(word))
        res.append(' '.join(text_t))
    return res
text_list=["he plays to doing flowers"]
data_stem=stemming(text_list)
data_lem=lemmanzation(text_list)
data_stem_lem=lemmanzation(data_stem)

print(data_lem)
print(data_stem)
print(data_stem_lem)

wnl=WordNetLemmatizer()
print(wnl.lemmatize("is"))
print("github")
