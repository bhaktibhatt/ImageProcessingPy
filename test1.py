from PIL import Image
from pytesseract import pytesseract
import enum #to extract text or values one by one

class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'
    DEU = 'deu'

class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Mac:
            print('Running on: MAC\n')
        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path
            print('Running on: Windows\n')

    def extract_text(self, image: str, lang: Language) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text
    
if __name__ == '__main__':
    ir = ImageReader(OS.Windows)
    # cfg1 = r'--psm 11 --oem 3'
    text = ir.extract_text('test_imgs/logos.webp', lang = Language.ENG)
    # processed_text = ' ' .join(text.split())
    print(text)