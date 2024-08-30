from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
import zipfile
import os

def add_noise(image, noise_level=30):
    img_array = np.array(image)
    noise = np.random.normal(0, noise_level, img_array.shape).astype(np.uint8)
    noisy_image = img_array + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)

def generate_synthetic_text_image(text, font_path="arial.ttf", font_size=32, 
                                  image_size=(200, 100), background_color=(255, 255, 230), 
                                  text_color=(30, 30, 30), noise=False):
    image = Image.new("RGB", image_size, color=background_color)
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    text_width, text_height = draw.textsize(text, font=font)
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    draw.text(position, text, fill=text_color, font=font)
    
    if noise:
        image = add_noise(image)
    
    return image

def generate_images_from_texts(text_list, font_path="arial.ttf", font_size=32, 
                               image_size=(200, 100), background_color=(255, 255, 230), 
                               text_color=(30, 30, 30), noise=False, output_dir="generated_images"):
    """
    Sinh ra nhiều hình ảnh từ danh sách các đoạn văn bản và lưu chúng vào thư mục.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    images = []
    file_paths = []
    
    for i, text in enumerate(text_list):
        img = generate_synthetic_text_image(text, font_path, font_size, 
                                            image_size, background_color, 
                                            text_color, noise)
        images.append(img)
        file_name = f"{output_dir}/generated_image_{i}.png"
        img.save(file_name)
        file_paths.append(file_name)
    
    return images, file_paths

def zip_files(file_paths, zip_filename="images.zip"):
    """
    Gộp các file ảnh thành file zip.
    """
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in file_paths:
            zipf.write(file, os.path.basename(file))
    
    return zip_filename

# Ví dụ sử dụng hàm

# Nếu cần tải font từ máy tính
uploaded = files.upload()

# Đường dẫn font sau khi tải lên
font_path = "/content/arial.ttf"

# Danh sách các đoạn văn bản cần sinh hình ảnh
texts = [
    "Hello, OCR!",
    "This is an automated text generation.",
    "Google Colab is great for quick experiments.",
    "Custom text image generation is easy!"
]

# Sinh hình ảnh từ danh sách văn bản
generated_images, file_paths = generate_images_from_texts(
    text_list=texts,
    font_path=font_path,
    font_size=40,
    image_size=(400, 100),
    background_color=(255, 250, 200),  # Nền hơi vàng
    text_color=(50, 50, 50),  # Chữ xám đen
    noise=True,  # Thêm nhiễu
    output_dir="generated_images"  # Thư mục để lưu ảnh
)

# Gộp các hình ảnh thành file zip
zip_filename = zip_files(file_paths)

# Tải file zip xuống
files.download(zip_filename)
