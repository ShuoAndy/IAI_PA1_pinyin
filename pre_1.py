import re

#计算单字词频

freq_table = {}
all_i=["02","04","05","06","07","08","09","10","11"]
for i in all_i:
    corpus_filename = "sina_news_gbk/2016-"+i+".txt"

    freq_table_filename = "freq1.txt"

    # 读取语料库文件
    with open(corpus_filename, "r", encoding="gbk") as f:
        corpus = f.read()

    # 去除语料库中的标点符号和数字，只保留汉字
    corpus = re.sub("[^\u4e00-\u9fa5]+", "", corpus)

    # 建立单个汉字的词频表
    for char in corpus:
        if char in freq_table:
            freq_table[char] += 1
        else:
            freq_table[char] = 1

# 将词频表存储到文件中
with open(freq_table_filename, "w", encoding="gbk") as f:
    for char, freq in freq_table.items():
        if(freq<10):
            continue
        f.write(char + "\t" + str(freq) + "\n")
