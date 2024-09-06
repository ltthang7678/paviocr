import random

def transfer_random_lines(input_file, output_file, num_lines_to_transfer):
    # Đọc tất cả các dòng từ file gốc
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Kiểm tra nếu số lượng dòng yêu cầu lớn hơn số dòng trong file
    if num_lines_to_transfer > len(lines):
        print("Số dòng yêu cầu lớn hơn số dòng trong file.")
        return

    # Chọn ngẫu nhiên 200.000 dòng từ file
    random_lines = random.sample(lines, num_lines_to_transfer)

    # Ghi các dòng đã chọn vào file output1.txt
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(random_lines)

    # Xóa các dòng đã chuyển khỏi danh sách ban đầu
    remaining_lines = [line for line in lines if line not in random_lines]

    # Ghi lại các dòng còn lại vào file output.txt
    with open(input_file, 'w', encoding='utf-8') as file:
        file.writelines(remaining_lines)

    print(f"Đã chuyển ngẫu nhiên {num_lines_to_transfer} dòng sang '{output_file}' và cập nhật '{input_file}'.")

# Đặt tên file và số lượng dòng cần chuyển
input_file = 'output.txt'
output_file = 'output1.txt'
num_lines_to_transfer = 200000

# Thực hiện chuyển
transfer_random_lines(input_file, output_file, num_lines_to_transfer)
