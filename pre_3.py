import re

#计算三字词频
freq_table = {}
all_i=["02","04","05","06","07","08","09","10","11"]
for i in all_i:
    corpus_filename = "sina_news_gbk/2016-"+i+".txt"
    freq_table_filename = "freq3.txt"

    # 读取语料库文件
    with open(corpus_filename, "r", encoding="gbk") as f:
        corpus = f.read()

    # 去除语料库中的标点符号和数字，只保留汉字
    corpus = re.sub("[^\u4e00-\u9fa5]+", "", corpus)

    # 建立三元词组的词频表
    for i in range(len(corpus) - 2):
        word_triple = corpus[i:i+3]
        if word_triple in freq_table:
            freq_table[word_triple] += 1
        else:
            freq_table[word_triple] = 1

    # 将词频表存储到文件中
    with open(freq_table_filename, "w", encoding="gbk") as f:
        for word_triple, freq in freq_table.items():
            if(freq<100):
                continue
            f.write(word_triple + "\t" + str(freq) + "\n")
