import cv2
import matplotlib.pyplot as plt
import os

# نجيب المسار الصحيح للصورة
img_path = os.path.join('images', 'cropped_meter.png')
img = cv2.imread(img_path)

if img is not None:
    # تعديل الألوان لتظهر بشكل طبيعي
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # عرض الصورة مع مسطرة وشبكة
    plt.figure(figsize=(10, 4))
    plt.imshow(img)
    plt.grid(color='red', linestyle='--', linewidth=0.5)
    plt.title("خذ أرقام الـ X من الأسفل، والـ Y من اليسار للمربع الذي يحيط بالأرقام فقط")
    plt.show()
else:
    print("خطأ: لم يتم العثور على الصورة. هل اسمها cropped_meter.png وموجودة داخل مجلد images؟")