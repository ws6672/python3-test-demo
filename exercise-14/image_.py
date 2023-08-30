import os

from PIL import Image,ImageFilter


@staticmethod
def filter_image(src_file_path,output_path):
    if not output_path:
        output_path = os.path.dirname(os.path.abspath(__file__))
    img = Image.open(src_file_path)
    img = img.filter(ImageFilter.BLUR)
    img.save(os.path.join(output_path,re_generator_name(src_file_path)))


@staticmethod
def re_generator_name(file_path:str)->str:
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1]
    return "{}_解析.{}".format(file_name,file_extension)