
#预处理汉字表（虽然看起来是无用功）

# 定义拼音汉字表和一二级汉字表的文件名
pinyin_filename = "拼音汉字表/拼音汉字表.txt"
chinese_filename = "拼音汉字表/一二级汉字表.txt"

# 创建一个空的汉字列表
chinese_list = []

# 读入一二级汉字表
with open(chinese_filename, "r", encoding="gbk") as f:
    for line in f:
        for char in line.strip():
            chinese_list.append(char)
# 创建一个空的字典
pinyin_dict = {}

# 读入拼音汉字表，逐行解析拼音和汉字列表
with open(pinyin_filename, "r", encoding="gbk") as f:
    for line in f:
        # 将一行拆分为拼音和汉字列表
        line = line.strip().split()
        pinyin = line[0]
        chinese = line[1:]
        # 只保留一二级汉字
        chinese = [c for c in chinese if c in chinese_list]
        # 将拼音和汉字列表加入字典
        pinyin_dict[pinyin] = chinese
# 存储字典
with open("dict.txt", "w", encoding="gbk") as f:
    for pinyin, chinese in pinyin_dict.items():
        # 将汉字列表转换为字符串并写入文件
        chinese_str = " ".join(chinese)
        f.write(f"{pinyin}：{chinese_str}\n")
