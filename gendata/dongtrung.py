def remove_duplicate_lines(filename):
    # Đọc nội dung file và xử lý mã hóa
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='latin-1') as file:
            lines = file.readlines()

    # Tạo một tập hợp để lưu các dòng không bị trùng
    unique_lines = set()
    result_lines = []

    for line in lines: # Loại bỏ khoảng trắng ở đầu và cuối dòng
        if line not in unique_lines:
            unique_lines.add(line)
            result_lines.append(line)

    # Ghi lại các dòng không bị trùng vào file mới
    with open('output.txt', 'w', encoding='utf-8') as file:
        for line in result_lines:
            file.write(line)

    print("Các dòng đã được xử lý và lưu vào file 'output.txt'.")

# Đặt tên file của bạn ở đây
filename = 'output_info1.txt'
remove_duplicate_lines(filename)
