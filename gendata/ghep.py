# Đọc nội dung từ các file với bộ mã hóa utf-8
with open('depluon1.txt', 'r', encoding='utf-8') as file_a:
    content_a = file_a.read()

with open('depluon2.txt', 'r', encoding='utf-8') as file_g:
    content_g = file_g.read()

# Mở file d.txt để ghi nội dung
with open('depluon.txt', 'a', encoding='utf-8') as file_d:
    file_d.write(content_a + '\n' + content_g)
