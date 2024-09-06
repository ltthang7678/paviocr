import hashlib
import random
import os
import time
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import numpy as np

def add_noise(image, noise_level):
    """Thêm nhiễu vào ảnh."""
    if noise_level <= 0:
        return image
    
    np_image = np.array(image)
    noise = np.random.normal(0, noise_level, np_image.shape).astype(np.uint8)
    noisy_image = Image.fromarray(np.clip(np_image + noise, 0, 255).astype(np.uint8))
    
    return noisy_image

def generate_random_background_color():
    """Tạo màu nền ngẫu nhiên từ xám nhạt đến vàng nhạt."""
    if random.choice([True, False]):  # Ngẫu nhiên chọn giữa hai dạng màu
        # Tạo màu xám nhạt x,x,x
        x = random.randint(233, 255)
        background_color = (x, x, x)
    else:
        # Tạo màu vàng nhạt 255,255,y
        y = random.randint(200, 255)
        background_color = (255, 255, y)
    
    return background_color

def generate_image(text, font_path, font_size, noise_level=0, text_color=(0, 0, 0), brightness_factor=1.0, contrast_factor=1.0, scale_factor=1.0):
    # Khởi tạo font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        raise ValueError(f"Font file '{font_path}' could not be opened. Please check the path and file.")
    
    # Ước lượng kích thước hình ảnh dựa trên độ dài văn bản sử dụng textbbox
    dummy_image = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_image)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    image_width = int(text_width * 1.1)  # Thêm khoảng trống 10%
    image_height = int(text_height * 3.0)  # Thêm khoảng trống 50%

    # Sử dụng hàm random để chọn màu nền
    background_color = generate_random_background_color()
    
    # Tạo ảnh nền với màu ngẫu nhiên
    image = Image.new('RGB', (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Tính toán vị trí để văn bản nằm giữa hình ảnh
    position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
    draw.text(position, text, font=font, fill=text_color)
    
    if noise_level > 0:
        image = add_noise(image, noise_level)
    
    if random.choice([True, False]):
        image = image.rotate(random.uniform(-3, 3), resample=Image.Resampling.BICUBIC)
    
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)
    
    # Thay đổi kích thước ảnh theo scale_factor
    width, height = image.size
    new_size = (int(width * scale_factor), int(height * scale_factor))
    image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    return image

def random_parameters():
    # Sinh tham số ngẫu nhiên với khoảng giá trị mới
    fonts = ["arial.ttf", "times.ttf"]
    font_path = random.choice(fonts)
    size = random.randint(8, 36)  # Kích thước chữ từ 24 đến 64
    color = tuple(random.randint(0, 50) for _ in range(3))  # Chữ từ xám nhẹ đến đen đậm
    brightness = round(random.uniform(0.9, 1.1), 2)  # Độ sáng từ 0.9 đến 1.1
    contrast = round(random.uniform(0.9, 1.1), 2)  # Độ tương phản từ 0.9 đến 1.1
    scale = round(random.uniform(0.8, 1.2), 2)  # Tỷ lệ thay đổi kích thước từ 0.8 đến 1.2
    noise = round(random.uniform(0, 0.5), 2)  # Mức độ nhiễu từ 0 đến 0.8

    return font_path, size, color, brightness, contrast, scale, noise

def process_text_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Mở file txt ở chế độ append để ghi thêm thông tin mới mà không ghi đè
    output_txt = os.path.join(output_dir, 'output_info1.txt')
    with open(output_txt, 'a', encoding='utf-8') as info_file:

        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, text in enumerate(lines):
            text = text.strip()  # Loại bỏ khoảng trắng thừa
            
            # Lấy các tham số ngẫu nhiên
            font_path, size, color, brightness, contrast, scale, noise = random_parameters()

            # Kiểm tra tồn tại của file font
            if not os.path.isfile(font_path):
                print(f"Font file '{font_path}' không tồn tại. Bỏ qua ảnh này.")
                continue
            
            # Tạo ảnh với tham số ngẫu nhiên
            img = generate_image(
                text,
                font_path,
                size,
                noise_level=noise,
                text_color=color,
                brightness_factor=brightness,
                contrast_factor=contrast,
                scale_factor=scale
            )

            # Tạo tên file với mã MD5 kết hợp timestamp để đảm bảo duy nhất
            timestamp = str(int(time.time()))
            md5_hash = hashlib.md5((text + timestamp).encode()).hexdigest()
            img_path = os.path.join(output_dir, f"{md5_hash}_{timestamp}.png").replace('\\', '/')

            # Lưu ảnh và ghi thông tin vào file txt
            img.save(img_path)
            info_file.write(f"{img_path}\t{text}\n")
            print(f"Lưu ảnh: {img_path}")

# Thay đổi thông số đầu vào
input_file = 'depluon.txt'  # File văn bản đầu vào
output_dir = 'augmented_images'

# Xử lý file văn bản và tạo ảnh
process_text_file(input_file, output_dir)