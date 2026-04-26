import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import cv2
import json
import re
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
# الإحداثيات الدقيقة التي استخرجتها أنت
ROI = {"x1": 5, "y1": 15, "x2": 370, "y2": 95}
def run_ai():
    if not os.path.exists("labels.json"): return
    with open("labels.json", "r") as f: data = json.load(f)

    print("--- بدء معالجة الصور بالذكاء الاصطناعي ---")

    for img_name, values in data.items():
        img_path = os.path.join("images", img_name)
        if not os.path.exists(img_path): continue

        img = cv2.imread(img_path)
        if img is None: continue
        crop = img[ROI["y1"]:ROI["y2"], ROI["x1"]:ROI["x2"]]

        try:
            result = ocr.ocr(crop, cls=True)
            extracted_text = ""
            
            if result and result[0]:
                # ترتيب المربعات من اليسار لليمين لضمان أن 2750 تأتي قبل 49
                sorted_lines = sorted(result[0], key=lambda x: x[0][0][0])
                for line in sorted_lines:
                    extracted_text += str(line[1][0])
            
            # تنظيف النص ليحتوي على أرقام فقط
            clean_text = re.sub(r'[^0-9]', '', extracted_text)
            
            data[img_name]["OCR_Etiketi"] = clean_text
            human_label = values.get('Final_Etiket', '')
            print(f"الصورة: {img_name} | قراءتك: {human_label} | AI: {clean_text}")
            
        except Exception as e:
            print(f"حدث خطأ: {e}")

    with open("labels.json", "w") as f: json.dump(data, f, indent=4)
    print("--- تمت العملية بنجاح! ---")

if __name__ == "__main__":
    run_ai()