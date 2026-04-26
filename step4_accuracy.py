<<<<<<< HEAD
import json
import re
import matplotlib.pyplot as plt

def calculate_accuracy():
    try:
        with open("labels.json", "r") as f: data = json.load(f)
    except FileNotFoundError:
        return

    total = len(data)
    correct = 0

    for img, values in data.items():
        human_raw = str(values.get("Final_Etiket", ""))
        ai_raw = str(values.get("OCR_Etiketi", ""))
        
        human_clean = re.sub(r'[^0-9]', '', human_raw)
        ai_clean = re.sub(r'[^0-9]', '', ai_raw)
        
        if human_clean == ai_clean and human_clean != "":
            correct += 1
    
    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"إجمالي الصور: {total} | الصحيح: {correct} | الدقة: {accuracy:.2f}%")

    labels = ['Correct', 'Incorrect']
    sizes = [correct, total - correct]
    colors = ['#2ecc71', '#e74c3c']

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("AI Accuracy vs Human Labeling")
    plt.show()

if __name__ == "__main__":
=======
import json
import re
import matplotlib.pyplot as plt

def calculate_accuracy():
    try:
        with open("labels.json", "r") as f: data = json.load(f)
    except FileNotFoundError:
        return

    total = len(data)
    correct = 0

    for img, values in data.items():
        human_raw = str(values.get("Final_Etiket", ""))
        ai_raw = str(values.get("OCR_Etiketi", ""))
        
        human_clean = re.sub(r'[^0-9]', '', human_raw)
        ai_clean = re.sub(r'[^0-9]', '', ai_raw)
        
        if human_clean == ai_clean and human_clean != "":
            correct += 1
    
    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"إجمالي الصور: {total} | الصحيح: {correct} | الدقة: {accuracy:.2f}%")

    labels = ['Correct', 'Incorrect']
    sizes = [correct, total - correct]
    colors = ['#2ecc71', '#e74c3c']

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("AI Accuracy vs Human Labeling")
    plt.show()

if __name__ == "__main__":
>>>>>>> ffd5cc1 (Initial commit: Water meter OCR project)
    calculate_accuracy()