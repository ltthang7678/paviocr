import unicodedata

# Vocab cung cấp
vocab = "aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \n"  # Thêm ký tự xuống dòng vào vocab

# Tạo từ điển các ký tự thay thế
replacement_dict = {
    "\t": "    ",
    '“': '"', '”': '"',  # Dấu ngoặc kép cong
    '‘': "'", '’': "'",  # Dấu nháy đơn cong
    '–': '-', '—': '-',  # Dấu gạch ngang dài
    '…': '...',          # Dấu ba chấm
}

# Chức năng đọc và xử lý file txt
def process_text_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Chuẩn hóa văn bản về dạng chuẩn NFC
    text = unicodedata.normalize('NFC', text)
    
    # Thay thế các ký tự bằng từ điển thay thế
    for original, replacement in replacement_dict.items():
        text = text.replace(original, replacement)
    
    # Tạo một tập hợp các ký tự vocab để kiểm tra
    vocab_set = set(vocab)
    
    # Xóa các ký tự không thuộc vocab hoặc không có trong từ điển thay thế, giữ lại các dòng tách biệt
    cleaned_text = ''.join([char for char in text if char in vocab_set])
    
    # Lưu lại nội dung đã xử lý
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)
    
    print(f"File đã được xử lý và lưu lại tại {output_file}")

# Thay đổi thông số đầu vào
input_file = 'trafo2.txt'  # File văn bản đầu vào
output_file = 'depluon2.txt'  # File văn bản đầu ra

# Xử lý file văn bản
process_text_file(input_file, output_file)
