import os
from enum import Enum, auto

from PIL import Image,ImageFilter

class ImageFilterEnum(Enum):
    BLUR = auto() # 模糊
    CONTOUR = auto() # 轮廓
    DETAIL = auto() # 细节
    EDGE_ENHANCE = auto() # 边缘增强
    EMBOSS = auto() # 浮雕
    SHARPEN = auto() # 锐化

    @staticmethod
    def get_by_str(str):
        result = ImageFilterEnum.BLUR
        for member in ImageFilterEnum:
            if member.name == str:
                result = member
                break
        return result.to_image_filter()
    
    def to_image_filter(self):
        if self == ImageFilterEnum.BLUR:
            return ImageFilter.BLUR
        elif self == ImageFilterEnum.CONTOUR:
            return ImageFilter.CONTOUR
        elif self == ImageFilterEnum.DETAIL:
            return ImageFilter.DETAIL
        elif self == ImageFilterEnum.EDGE_ENHANCE:
            return ImageFilter.EDGE_ENHANCE
        elif self == ImageFilterEnum.EMBOSS:
            return ImageFilter.EMBOSS
        elif self == ImageFilterEnum.SHARPEN:
            return ImageFilter.SHARPEN
    

@staticmethod
def filter_image(src_file_path,output_path,filter_type):
    if not output_path:
        output_path = os.path.dirname(os.path.abspath(__file__))
    img = Image.open(src_file_path)
    img = img.filter(ImageFilterEnum.get_by_str(filter_type))
    img.save(os.path.join(output_path,re_generator_name(src_file_path)))


@staticmethod
def re_generator_name(file_path:str)->str:
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1]
    name = os.path.splitext(file_name)[0]
    return "{}_解析{}".format(name,file_extension)