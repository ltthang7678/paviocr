import os

# Đọc nội dung của file uni.txt và lưu các dòng vào tập hợp để kiểm tra
with open('kiemtra.txt', 'r', encoding='utf-8') as file:
    uni_lines = set(line.strip() for line in file)

# Đọc nội dung của file inu.txt
with open('output_info1.txt', 'r', encoding='utf-8') as file:
    inu_lines = file.readlines()

# Mở một file tạm để ghi các dòng hợp lệ
with open('temp_inu.txt', 'w', encoding='utf-8') as temp_file:
    for line in inu_lines:
        # Tách nội dung 1 và nội dung 2
        parts = line.strip().split('\t', 1)
        if len(parts) != 2:
            continue  # Nếu không có đủ 2 phần, bỏ qua dòng này

        content1, content2 = parts

        # Kiểm tra nếu nội dung 1 tồn tại trong tập hợp từ uni.txt
        if content1 in uni_lines:
            temp_file.write(line)

# Thay thế file gốc inu.txt bằng file tạm
#os.replace('temp_inu.txt', 'inu.txt')
