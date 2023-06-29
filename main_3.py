import sys
import numpy as np


#三元算法


# 读取拼音词典
pinyin_dict = {}
with open('dict.txt', encoding='gbk') as f:
    for line in f:
        py, chars = line.strip().split('：')
        pinyin_dict[py] = chars.split()


# 读取一元词频
freq1_dict = {}
with open('freq1.txt', encoding='gbk') as f:
    for line in f:
        word, freq = line.strip().split('\t')
        freq1_dict[word] = int(freq)

# 读取二元词频
freq2_dict = {}
with open('freq2.txt', encoding='gbk') as f:
    for line in f:
        word, freq = line.strip().split('\t')
        freq2_dict[word] = int(freq)
        
# 读取三元词频
freq3_dict = {}
with open('freq3.txt', encoding='gbk') as f:
    for line in f:
        word, freq = line.strip().split('\t')
        freq3_dict[word] = int(freq)

#读取句首词频
freqhead_dict = {}
with open('freqhead.txt', encoding='gbk') as f:
    for line in f:
        word, freq = line.strip().split('\t')
        freqhead_dict[word] = int(freq)
        
def viterbi(obs, pinyin_dict, freq1_dict, freq2_dict,freqhead_dict):
    obs = obs.split()  # 观测序列
    T = len(obs)  # 观测序列的长度

    # 初始化动态规划表和路径表
    dp = [{} for _ in range(T)]
    path = [{} for _ in range(T)]

    # 初始状态
    for char in pinyin_dict[obs[0]]:
        try:
            dp[0][char] = freqhead_dict[char]  # 第一个汉字的概率为单字频率
        except KeyError:
            dp[0][char] = 0  # 不存在的汉字概率为0
        path[0][char] = ''  # 初始状态没有前一个汉字

    for t in range(1, 2):
        for char in pinyin_dict[obs[t]]:  # char为当前汉字
            max_prob = 0
            max_char = ' '
            for pre_char in pinyin_dict[obs[t-1]]:  # pre_char为前一个汉字
                prob = dp[t-1][pre_char] * freq2_dict.get(pre_char+char, 0) / freq1_dict.get(pre_char, 1)
                # 如果前一个汉字不存在，认为它的频率为1，避免出现0的情况
                if prob > max_prob:
                    max_prob = prob
                    max_char = pre_char
            dp[t][char] = max_prob  
            path[t][char] = max_char
            
    for t in range(2, T):
        for char in pinyin_dict[obs[t]]:  # char为当前汉字
            max_prob = 0
            max_char = ' '
            for pre_char in pinyin_dict[obs[t-1]]:  # pre_char为前一个汉字
                for prepre_char in pinyin_dict[obs[t-2]]: #prepre_char为前两个汉字
                    prob = dp[t-1][pre_char] * (4*freq3_dict.get(prepre_char+pre_char+char, 0) / freq2_dict.get(prepre_char+pre_char, 1)+ freq2_dict.get(pre_char+char, 0) / freq1_dict.get(pre_char, 1))
                    # 如果前两个汉字不存在，认为它的频率为1，避免出现0的情况
                    if prob > max_prob:
                        max_prob = prob
                        max_char = pre_char
            dp[t][char] = max_prob 

            path[t][char] = max_char
            
    # 找到最大概率的路径
    max_prob = 0
    max_char = ''
    for char in pinyin_dict[obs[-1]]:
        if dp[-1][char] > max_prob:
            max_prob = dp[-1][char]
            max_char = char
    best_path = [max_char] #从这个char开始回溯

    # 回溯路径
    for t in range(T-1, 0, -1):
        try:
            best_path.append(path[t][best_path[-1]])
        except:
            1
    best_path.reverse()

    return ''.join(best_path)



if __name__ == '__main__':
    #obs = input("请输入拼音序列，每个拼音之间用空格分隔：")
    #results = viterbi(obs, pinyin_dict,freq1_dict,freq2_dict,freqhead_dict)
    #print(results)
    with open("input.txt", "r", encoding="gbk") as f_in, open("output.txt", "w", encoding="gbk") as f_out:
        for line in f_in:
            obs = line.strip()
            results = viterbi(obs, pinyin_dict, freq1_dict, freq2_dict, freqhead_dict)
            #print(results)
            f_out.write("".join(results) + "\n")
    
