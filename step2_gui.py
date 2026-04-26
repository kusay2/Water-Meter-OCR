import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os

class MeterAnnotationApp:
    def __init__(self, root, image_folder):
        self.root = root
        self.root.title("أداة التحقق المزدوج - Water Meter Verification")
        self.root.geometry("650x550")

        self.image_folder = image_folder
        # جلب الصور من مجلد images
        self.images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.current_idx = 0
        self.results_file = "labels.json" 
        self.data = {}

        if not self.images:
            messagebox.showerror("خطأ", "لم يتم العثور على صور في مجلد images!")
            root.destroy()
            return

        self.setup_ui()
        self.load_image()

    def setup_ui(self):
        # عرض الصورة المقطوعة (التي أنتجها الكود السابق) أو الأصلية
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.info_label.pack()

        # حقول الإدخال للتحقق المزدوج
        tk.Label(self.root, text="إدخال المراقب الأول (Kontrolör 1):", font=("Arial", 11)).pack(pady=5)
        self.entry1 = tk.Entry(self.root, font=("Arial", 14), justify='center')
        self.entry1.pack()

        tk.Label(self.root, text="إدخال المراقب الثاني (Kontrolör 2):", font=("Arial", 11)).pack(pady=5)
        self.entry2 = tk.Entry(self.root, font=("Arial", 14), justify='center')
        self.entry2.pack()

        # زر الحفظ
        self.save_btn = tk.Button(self.root, text="تحقق وحفظ (Save & Next)", command=self.save_data, 
                                  bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), width=20)
        self.save_btn.pack(pady=25)

    def load_image(self):
        if self.current_idx < len(self.images):
            img_name = self.images[self.current_idx]
            self.info_label.config(text=f"صورة رقم {self.current_idx + 1} من {len(self.images)}: {img_name}")
            
            img_path = os.path.join(self.image_folder, img_name)
            img = Image.open(img_path)
            img = img.resize((500, 250)) 
            photo = ImageTk.PhotoImage(img)
            
            self.image_label.config(image=photo)
            self.image_label.image = photo
            
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.entry1.focus_set()
        else:
            messagebox.showinfo("انتهى", "تم الانتهاء من جميع الصور في المجلد!")
            self.root.destroy()

    def save_data(self):
        v1 = self.entry1.get().strip()
        v2 = self.entry2.get().strip()
        
        if not v1 or not v2:
            messagebox.showwarning("تنبيه", "يرجى ملء الحقلين!")
            return

        # منطق المهمة: يجب أن يتطابق الإدخالان
        if v1 == v2:
            img_name = self.images[self.current_idx]
            self.data[img_name] = {"Final_Etiket": v1}
            
            with open(self.results_file, 'w') as f:
                json.dump(self.data, f, indent=4)
            
            self.current_idx += 1
            self.load_image()
        else:
            messagebox.showerror("خطأ في المطابقة", "القيم غير متطابقة! أعد التأكد من الرقم.")

if __name__ == "__main__":
    root = tk.Tk()
    # سنستخدم مجلد images الذي يحتوي على صورك
    app = MeterAnnotationApp(root, "images")
    root.mainloop()