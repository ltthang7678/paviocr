def clean_text_file(input_filepath, output_filepath, vocab):
    with open(input_filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Tạo tập hợp các ký tự cho phép để tra cứu nhanh
    allowed_chars = set(vocab)

    # Xử lý từng dòng để xóa các ký tự không có trong vocab
    cleaned_lines = []
    for line in lines:
        parts = line.split('\t', 1)
        if len(parts) == 2:
            image_path = parts[0]
            text = ''.join([char for char in parts[1] if char in allowed_chars])
            cleaned_lines.append(f"{image_path}\t{text}")

    # Ghi các dòng đã làm sạch vào file đầu ra
    with open(output_filepath, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_lines))

# Ví dụ sử dụng
vocab = ' aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!"#$%&\'()*+,-./:;'
input_filepath = 'output_info.txt'  # Thay thế bằng đường dẫn tới file đầu vào của bạn
output_filepath = 'raday.txt'  # Thay thế bằng đường dẫn tới file đầu ra của bạn

# Gọi hàm để làm sạch file văn bản
clean_text_file(input_filepath, output_filepath, vocab)
