with open('测试语料/std_output.txt', 'r') as f1, open('output.txt', 'r',encoding="gbk") as f2:
    total_sentence = 0
    total_correct = 0   #句子正确数
    total_chars=0
    total_yes = 0   #汉字正确数
    for line1, line2 in zip(f1, f2):
        total_sentence += 1
        if line1 == line2:
            total_correct += 1
        line1_chars = [char for char in line1.strip()]
        line2_chars = [char for char in line2.strip()]
        for i in range(len(line1_chars)):
            total_chars += 1
            try:
                if line1_chars[i] == line2_chars[i]:
                    total_yes += 1
            except:
                1
    accuracy = total_correct / total_sentence
    accuracy_char = total_yes / total_chars
    print(f"句平均正确率为：{accuracy:.2%} ",f"字平均正确率为：{accuracy_char:.2%} ")
