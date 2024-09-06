import random

def generate_phone_number():
    # Đầu số bạn yêu cầu là 03, 07, 08, 09, 05
    prefixes = ['3', '7', '8', '9', '5']
    prefix = random.choice(prefixes)
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # Tạo số ngẫu nhiên 8 chữ số
    return f"+84{prefix}{number}"

# Tạo 10.000 số điện thoại
phone_numbers = [generate_phone_number() for _ in range(8686)]

# Lưu vào tệp
with open('phone_numbers.txt', 'w') as file:
    file.write('\n'.join(phone_numbers))

print("Đã tạo 10.000 số điện thoại và lưu vào file phone_numbers.txt")
