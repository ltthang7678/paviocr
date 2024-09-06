def count_occurrences(file_path, search_string):
    """Đếm số lần xuất hiện của search_string trong file_path."""
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            count += line.count(search_string)
    return count

# Đường dẫn đến file và chuỗi cần tìm
file_path = 'output_info1.txt'
search_string = 'augmented_images'

# Đếm số lần xuất hiện và in kết quả
occurrences = count_occurrences(file_path, search_string)
print(f"Số lần xuất hiện của '{search_string}' là: {occurrences}")