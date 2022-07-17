text_data = '과수원길 동구 밖 과수원길 아카시아 꽃이 활짝 폈네 하얀 꽃 이파리 눈송이처럼 날리네 향긋한 꽃냄새가 실바람타고 솔솔 둘이서 말이 없네 얼굴 마주 보며 생긋 아카시아 꽃 하얗게 핀 먼 옛날에 과수원길'
word_dic = {}
for w in text_data.split():
    if w in word_dic:
        word_dic[w] += 1
    else:
        word_dic[w] = 1
num = 0
for w, count in sorted(word_dic.items()):
    if count >= 2:
        print(w, ':', count)
    else:
        num = num + 1
print('문장에서 단어가 1번 만 나올 확률:', num / len(text_data.split()) * 100, '%')
