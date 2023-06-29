import re

#计算句首词频

freq_table = {}
all_i=["02","04","05","06","07","08","09","10","11"]
for i in all_i:
    corpus_filename = "sina_news_gbk/2016-"+i+".txt"

    freq_table_filename = "freqhead.txt"

# 读取语料库文件
    with open(corpus_filename, "r", encoding="gbk") as f:
        corpus = f.read()

# 去除语料库中的标点符号和数字，只保留汉字
    corpus = re.sub("[^\u4e00-\u9fa5]+", " ", corpus)

# 切分成句子
    sentences = corpus.split()

# 统计每个句子的第一个非空格字符的词频
    for sentence in sentences:
        first_char = sentence.strip()[0]
        if first_char in freq_table:
            freq_table[first_char] += 1
        else:
            freq_table[first_char] = 1

# 将词频表存储到文件中
with open(freq_table_filename, "w", encoding="gbk") as f:
    for char, freq in freq_table.items():
        f.write(char + "\t" + str(freq) + "\n")
