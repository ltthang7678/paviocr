# Đường dẫn đến tệp g2.txt
file_path = 'output.txt'
# Đếm số dòng trong g2.txt
with open(file_path, 'r', encoding='utf-8') as file:
    line_count = sum(1 for line in file)
print(f"Số dòng trong {file_path} là: {line_count}")
