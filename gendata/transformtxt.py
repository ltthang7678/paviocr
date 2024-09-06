import os
import random

def process_text_file(input_file, output_file):
    """
    Xử lý file văn bản để loại bỏ khoảng trắng giữa các dòng và giới hạn số ký tự tối đa mỗi dòng,
    đồng thời đảm bảo rằng các từ không bị cắt ngang dòng.
    
    :param input_file: Đường dẫn đến file văn bản đầu vào.
    :param output_file: Đường dẫn đến file văn bản đầu ra.
    """
    # Chọn giá trị max_length ngẫu nhiên từ 50 đến 150
    max_length = random.randint(90, 90)
    
    print(f"Số ký tự tối đa mỗi dòng: {max_length}")

    # Kiểm tra xem file đầu vào có tồn tại không
    if not os.path.isfile(input_file):
        print(f"File '{input_file}' không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
        return

    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    processed_lines = []
    first_non_empty_found = False

    # Xử lý từng dòng
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            first_non_empty_found = True
            processed_lines.append(stripped_line)
        elif first_non_empty_found:
            processed_lines.append('')

    # Gộp các dòng thành một chuỗi liên tiếp
    all_text = ' '.join(processed_lines)
    
    # Chia chuỗi thành các đoạn nhỏ với số ký tự tối đa
    words = all_text.split(' ')
    current_line = ''
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for word in words:
            # Kiểm tra nếu thêm từ vào dòng hiện tại có vượt quá max_length
            if len(current_line) + len(word) + 1 <= max_length:
                if current_line:
                    current_line += ' '
                current_line += word
            else:
                # Ghi dòng hiện tại và bắt đầu một dòng mới
                if current_line:
                    outfile.write(current_line + '\n')
                current_line = word
        
        # Ghi phần còn lại vào file
        if current_line:
            outfile.write(current_line + '\n')

# Thay đổi thông số đầu vào
input_file = 'input.txt'  # Đảm bảo file này tồn tại tại đường dẫn này
output_file = 'trafo2.txt'  # File văn bản đầu ra

# Xử lý file văn bản
process_text_file(input_file, output_file)
