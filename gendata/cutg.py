# Đường dẫn đến tệp g.txt
input_file = 'g2.txt'

# Đọc toàn bộ nội dung từ g.txt
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Tính toán số ký tự cho g1 và g2
total_length = len(content)
split_point = int(total_length * 0.8)  # 70% cho g1

# Tạo nội dung cho g1 và g2
content_g1 = content[:split_point]
content_g2 = content[split_point:]

# Ghi nội dung vào g1.txt và g2.txt
with open('g3.txt', 'w', encoding='utf-8') as file_g1:
    file_g1.write(content_g1)

with open('g4.txt', 'w', encoding='utf-8') as file_g2:
    file_g2.write(content_g2)

print("Đã chia nội dung thành g1.txt và g2.txt")
