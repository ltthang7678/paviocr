import unicodedata

def normalize_text(text):
    """
    Chuẩn hóa văn bản để kết hợp các ký tự và dấu thanh thành ký tự có dấu.

    Args:
        text: Chuỗi văn bản cần chuẩn hóa.

    Returns:
        Chuỗi văn bản đã được chuẩn hóa.
    """
    # Sử dụng unicodedata để chuẩn hóa văn bản
    return unicodedata.normalize('NFC', text)

def normalize_file(file_path):
    """
    Chuẩn hóa văn bản trong file để kết hợp các ký tự và dấu thanh.

    Args:
        file_path: Đường dẫn đến file văn bản cần chuẩn hóa.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        normalized_lines = [normalize_text(line) for line in lines]

    # Ghi lại file đã được chuẩn hóa
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(normalized_lines)

# Ví dụ sử dụng:
file_path = 'output_info.txt'  # Đường dẫn đến file input.txt của bạn
normalize_file(file_path)
