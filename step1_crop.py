import cv2
import json

json_data = '{"count":8,"scanAreaX1":11.162790697674419,"scanAreaY1":33.489132656537436,"scanAreaX2":470.2325581395349,"scanAreaY2":147.91033589970704,"scanStepRate":2}'
data = json.loads(json_data)

x1 = int(data['scanAreaX1'])
y1 = int(data['scanAreaY1'])
x2 = int(data['scanAreaX2'])
y2 = int(data['scanAreaY2'])

# ملاحظة: يجب أن تكون الصورة موجودة داخل مجلد images واسمها meter.png
image_path = 'images/meter.png' 
img = cv2.imread(image_path)

if img is not None:
    roi_cropped = img[y1:y2, x1:x2]
    cv2.imwrite('cropped_meter.png', roi_cropped)
    cv2.imshow('Cropped ROI', roi_cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Success: Image cropped successfully!")
else:
    print("Error: Image not found. Make sure you have 'mete" \
    "r.png' inside the 'images' folder.")

    