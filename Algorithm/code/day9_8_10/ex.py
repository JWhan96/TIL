text = "   Hello, world!   "
delimiter = '-'
strip_text = text.strip(' ')
text_list = []
for item in text:
    if item != ' ':
        text_list.append(item)
 # 문자열을 리스트로 변환

result = delimiter.join(text_list)

print(result)  # 출력: "H-e-l-l-o-,- -w-o-r-l-d-!"
print(text_list)