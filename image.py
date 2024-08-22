import os
import base64
from PIL import Image

def convert_image_to_svg(image_path, svg_path):
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_image = base64.b64encode(image_data).decode('utf-8')
        
        image_format = image_path.split('.')[-1].lower()
        if image_format == 'jpg':
            image_format = 'jpeg'
        
        # 创建SVG内容，移除固定的宽度和高度
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
        <image href="data:image/{image_format};base64,{base64_image}" width="100%" height="100%"/>
    </svg>'''

        with open(svg_path, "w") as svg_file:
            svg_file.write(svg_content)

        print(f"Converted {image_path} to {svg_path}, SVG is responsive to external parameters.")
    except Exception as e:
        print(f"Failed to convert {image_path}. Error: {e}")

def batch_convert_images_to_svg(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg')):
                image_path = os.path.join(subdir, file)
                svg_path = os.path.splitext(image_path)[0] + '.svg'
                convert_image_to_svg(image_path, svg_path)

# 获取当前工作目录
root_directory = os.getcwd()

# 开始批量转换
batch_convert_images_to_svg(root_directory)
