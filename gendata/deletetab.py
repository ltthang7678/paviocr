import os

def clean_annotation_file(annotation_path, output_path):
    """
    Cleans the annotation file by removing tab characters from the text content.

    Args:
        annotation_path: Path to the original annotation file.
        output_path: Path to save the cleaned annotation file.
    """
    cleaned_lines = []

    with open(annotation_path, 'r', encoding='utf-8') as ann_file:
        lines = ann_file.readlines()
        for line in lines:
            # Split only on the first tab to get the image path and the text
            image_path, text = line.split('\t', 1)
            
            # Remove any tab characters within the text
            text = text.replace('\t', ' ')
            
            # Join the cleaned image path and text
            cleaned_line = f"{image_path}\t{text}"
            cleaned_lines.append(cleaned_line)

    # Write the cleaned lines to a new file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(cleaned_lines)

# Example usage:
annotation_path = 'output_info1.txt'  # Đường dẫn đến tệp chú thích gốc
output_path = 'clean.txt'  # Đường dẫn để lưu tệp chú thích đã được làm sạch
clean_annotation_file(annotation_path, output_path)
