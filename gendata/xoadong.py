def remove_last_n_lines(filename, n, encoding='utf-8'):
    try:
        # Đọc toàn bộ nội dung của tệp
        with open(filename, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Giữ lại tất cả các dòng ngoại trừ n dòng cuối
        new_lines = lines[:-n]

        # Ghi các dòng còn lại vào tệp
        with open(filename, 'w', encoding=encoding) as file:
            file.writelines(new_lines)

        print(f"Removed the last {n} lines from {filename}")

    except UnicodeDecodeError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Thay 'input.txt' bằng tên tệp của bạn và 60000 bằng số dòng cần xóa
remove_last_n_lines('input.txt', 15000, encoding='utf-8')
