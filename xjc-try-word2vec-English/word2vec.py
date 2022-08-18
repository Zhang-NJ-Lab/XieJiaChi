# -*- coding: utf-8 -*-
from gensim.models import word2vec, KeyedVectors
import pandas as pd
# import gensim.downloader
# from nltk.corpus import PlaintextCorpusReader
# import gensim
import numpy as np
# import pkuseg
from nltk.tokenize import MWETokenizer
import nltk
import string
from nltk import word_tokenize
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
# 小写化
# with open(r"E:\Springer Nature EN 2010-2021\2021物理.txt", encoding='utf-8') as f1: #加载原始数据库并分词
#     content = f1.read()
#     lower_content = content.lower()
#     with open(r"E:\Springer Nature EN 2010-2021\2021物理-小写.txt", 'w', encoding="utf-8") as f2:
#         f2.write(lower_content)
#
#
# # 去空行
# with open(r"E:\Springer Nature EN 2010-2021\2021物理-小写.txt", 'r', encoding="utf-8") as f2,open(r"E:\Springer Nature EN 2010-2021\2021物理-小写-空格.txt",'w',encoding="utf-8") as f3:
#     for line in f2.readlines():
#         if line.split():
#                 f3.write(line)

# with open('。。。.json', 'r', encoding="utf-8") as f2:
#     for line in f2.readlines():
#         print(str.index(line,'.')+2)

#
# 归一化
# with open('2000小写-去空行.txt', 'r', encoding="utf-8") as f3:
#     content = f3.read()
#     porterstemmer = PorterStemmer()
#     porterstemmer.stem(content)
#     with open('2000小写-去空行_归一化.txt','w',encoding="utf-8") as f4:
#         f4.write(content)
#
#
# stopwords = stopwords.words('english')
# print(stopwords)
#
# stopwords = [line.strip() for line in open(r'钙钛矿材料_效率_停止词库.txt', encoding='UTF-8').readlines()] #加载自定义停止词
#
# sentence=str()
#
# with open(r'E:\Springer Nature EN 2010-2021\2010物理-小写-空格-还原.txt', encoding='utf-8') as f: #加载原始数据库并分词
#     document = f.read()
#     # print(document)
#     #document_cut = jieba.cut(document)
#     tokenizer = MWETokenizer([('solar', 'cell'),('surface','area'),('electron','transport','layer'),('hole','transport','layer'),('constant','voltage'),
#                               ('solar','energy'),('band','gap'),('metal','bond'),('conduction','band'),('activated','carbon'),('ionic','bond'),('energy','storage'),
#                               ('energy','level'),('negative','charge'),('high','temperature'),('sodium','ion'),('polarization','intensity'),('forbidden','band'),
#                               ('low','temperature'),('negative','electrode'),('covalent','bond'),('superconducting','state'),('space','lattice'),('secondary','electron'),
#                               ('diffuse','reflection'),('magnetic','susceptibility'),('electron','microscope'),('water','absorption'),('total','reflection'),
#                               ('additive','polymerization'),('auger','electron'),('positive','electrode'),('valence','band'),('lithium','ion'),('positive','electricity'),
#                               ('energy','band'),('constant','temperature'),('red','copper'),('hydrogen','bond'),('titanium','alloy'),
#                               ('greenhouse','effect'),('surface','wave'),('aluminum','powder'),('phase','transition'),('negative','pressure'),('thermal''conductivity'),
#                               ('numerical','value'),('coordination','number')], separator = '-')
#     #seg = pkuseg.pkuseg(user_dict = "userdict.txt")
#     text=tokenizer.tokenize(nltk.word_tokenize(document))
#     # print(text)
#     result = ' '.join(text)
#     # print(result)
#     for word in text:
#         if word not in stopwords:
#             if word != "\t":
#                 sentence += word + ' '
#
#     with open(r'E:\Springer Nature EN 2010-2021\2010物理-小写-空格-还原-停止-自定.txt', 'w',encoding="utf-8") as f2:
#         f2.write(sentence)
#
#
#
#
#
#
#
#
# sentences = word2vec.LineSentence(r'E:\整合\2010-2021-EN-预处理.txt')
# # print(sentences)
# model = word2vec.Word2Vec(sentences, min_count=3, vector_size=200, window=5,sg=1,sample=1e-4,epochs=10) #训练word2vec模型,设置超参数
# model.save(r'E:\整合\Model.model')
# model.wv.save_word2vec_format(r'E:\整合\model.txt') #保存为模型类文件
#
#
# print(aa)
# print(type(aa))
model = KeyedVectors.load_word2vec_format(r'E:\整合\model.txt' ,binary= False) #以Word2vec文件形式打开刚刚保存的模型类文件

Me = model.most_similar('tio2-in2o3',topn=50000) #与' '最相似的单词
# # # print(Me)
# aa = []
# lines = ""
# file = open(r'E:\整合\photovoltaic-sim.csv', mode='w', encoding='utf-8')
# with open(r'E:\整合\model-word-化学式.txt', "r",encoding='utf-8') as f:
#     for line in f.readlines():
#         data = line.split('\n')
#         for line in data:
#             sub_str = line.split(' ')
#             print(sub_str)
#         if sub_str:
#             aa.append(sub_str)
#             for i in Me:
#                 if i[0] in aa[0]:
#                     print(i)
#                     lines = str(i[1]) + ", "
#                     lines += "\n"
#                     file.write(lines)


lines = ""
file = open(r'E:\整合\tio2-in2o3-sim-all1.csv', mode='w', encoding='utf-8')
for i in Me:
	lines = str(i[1])
	lines = lines + ", "
	lines += "\n"
	file.write(lines)
file.close()


# print(Me)

# w = gensim.downloader.load('w2vModel.txt')
# w.most_similar('solar_cell')

# word2 = model.similarity('tio2-in2o3','polarization_intensity') #计算任意两个词向量之间的余弦相似度
# print(word2)
# print(model.similarity('tio2-in2o3', 'surface_area'))
# print(model.similarity('tio2-in2o3', 'thermal-conductivity'))
# print(model.similarity('tio2-in2o3', 'magnetic_susceptibility'))


'''
# Me = np.array([('1',2), ('3',4), ('5',6), ('7',8)])
lines = ""
file = open("result1.csv", mode='w', encoding='utf-8')
for i in Me:
	lines = str(i[1])
	lines = lines + ", "
	lines += "\n"
	file.write(lines)
file.close()
'''



# from nltk import word_tokenize, pos_tag
# from nltk.corpus import wordnet
# from nltk.stem import WordNetLemmatizer
#
#
# # 获取单词的词性
# def get_wordnet_pos(tag):
#     if tag.startswith('J'):
#         return wordnet.ADJ
#     elif tag.startswith('V'):
#         return wordnet.VERB
#     elif tag.startswith('N'):
#         return wordnet.NOUN
#     elif tag.startswith('R'):
#         return wordnet.ADV
#     else:
#         return None
# with open(r"E:\Springer Nature EN\1980.txt", "r",encoding='utf-8') as f,open(r"E:\Springer Nature EN\1980词形还原.txt", "w",encoding='utf-8') as f1:
#     content = f.read()
#     sentence = content
#     tokens = word_tokenize(sentence)  # 分词
#     tagged_sent = pos_tag(tokens)     # 获取单词词性
#
#     wnl = WordNetLemmatizer()
#     lemmas_sent = []
#     for tag in tagged_sent:
#         wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
#         lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos)) # 词形还原
#     print(lemmas_sent)
#     sentence1 = str()
#     for word in lemmas_sent:
#         print(word)
#         sentence1 = word + ' '
#         f1.write(sentence1)


# # 去除带_的chemdata
# aa = []
# line = ''
# file = open("去_的chemdata.txt", mode='w', encoding='utf-8')
# with open("chemdata结果.txt", "r",encoding='utf-8') as f:
#     for line in f.readlines():
#         data = line.split('\n')
#         for str1 in data:
#             sub_str = str1.split(' ')
#         if sub_str:
#             aa.append(sub_str)
#         # print(aa[0])
#         for i in aa[0]:
#             for word in i:
#                 if word != '_':
#                     b = aa[0].remove(i)
#                     break
#         print(b)
#         #             line = i +' '
#         # file.write(line)


from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


# # 获取单词的词性
# def get_wordnet_pos(tag):
#     if tag.startswith('J'):
#         return wordnet.ADJ
#     elif tag.startswith('V'):
#         return wordnet.VERB
#     elif tag.startswith('N'):
#         return wordnet.NOUN
#     elif tag.startswith('R'):
#         return wordnet.ADV
#     else:
#         return None
# with open(r"E:\Springer Nature EN 2010-2021\2010物理-小写-空格.txt", "r",encoding='utf-8') as f,open(r"E:\Springer Nature EN 2010-2021\2010物理-小写-空格-还原.txt", "w",encoding='utf-8') as f1:
#     sentences1 = str()
#     for line in f.readlines():
#         sentence = line
#         tokens = word_tokenize(sentence)  # 分词
#         print(tokens)
#         tagged_sent = pos_tag(tokens)     # 获取单词词性
#         print(tagged_sent)
#         wnl = WordNetLemmatizer()
#         lemmas_sent = []
#         for tag in tagged_sent:
#             wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
#             lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos)) # 词形还原
#         print(lemmas_sent)
#         result = ' '.join(lemmas_sent)
#         print(result)
#         result = result + '\n'
#         f1.write(result)



'''
     提取前 i名相似度计算的化学式并导入csv文件
'''
model = KeyedVectors.load_word2vec_format(r'E:\整合\model.txt' ,binary= False) #以Word2vec文件形式打开刚刚保存的模型类文件

Me = model.most_similar('heterojunction',topn=15000) #与' '最相似的单词

aa = []
lines = ""

dataset = r'E:\整合\model-word-化学式.xlsx'
data = pd.DataFrame(pd.read_excel(dataset))
first_word = data.values[:,0]
print(first_word)
file = open(r'E:\整合\heterojunction-sim1.csv', mode='w', encoding='utf-8')
for i in Me:
    if i[0] in first_word:
        print(i[0])
        # lines = i[0] + ", " # 化学式
        lines = i[0] + ", " # 余弦相似度
        lines += "\n"
        file.write(lines)

'''
    相关词非相关词计算
'''
# model = KeyedVectors.load_word2vec_format(r'E:\整合\model.txt' ,binary= False) #以Word2vec文件形式打开刚刚保存的模型类文件
#
# dataset = r'E:\相关与非相关.xlsx'
# data = pd.DataFrame(pd.read_excel(dataset))
# first_word = data.values[:,10]
# second_word = data.values[:,11]
# for i in range(len(first_word)):
#     sim = model.similarity(first_word[i], second_word[i])
#     print(first_word[i],second_word[i],sim)