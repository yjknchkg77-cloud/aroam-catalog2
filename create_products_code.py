import os
import re

def normalize_name(filename):
    name = os.path.splitext(filename)[0]
    name = name.replace("_", " ").replace("-", " ")
    return name.strip()

def generate_id(category, index):
    cat_clean = re.sub(r'[^A-Za-z0-9]', '', category)
    if len(cat_clean) < 3:
        cat_clean = (cat_clean + "XXX")[:3]
    return f"{cat_clean.upper()}-{index:03d}"

def main():
    folder = input("הקלד/י את הנתיב לתיקייה הראשית: ").strip()

    if not os.path.isdir(folder):
        print("התיקייה לא נמצאה.")
        return

    print("\nמייצר קוד...\n")

    all_output = []

    for category in sorted(os.listdir(folder)):
        category_path = os.path.join(folder, category)
        if not os.path.isdir(category_path):
            continue

        images = [f for f in os.listdir(category_path) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]

        for i, img in enumerate(images, start=1):
            product_name = normalize_name(img)
            product_id = generate_id(category, i)

            line = (
                f'{{ id: "{product_id}", name: "{product_name}", category: "{category}", '
                f'price: 0.0, unit: "יחידה", image: "images/{category}/{img}" }},'
            )

            all_output.append(line)

    result = "\n".join(all_output)

    with open("products_output.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("✔️ הושלם! נוצר products_output.txt עם כל הקוד בשורה אחת לכל מוצר.")

if __name__ == "__main__":
    main()