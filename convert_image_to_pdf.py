import os
from PIL import Image

# משתנים
images_folder = '/app/images'
output_folder = '/app/output'
pdf_name = os.getenv('PDF_NAME', 'output.pdf')  # אם לא קיבלת משתנה, השתמש בשם ברירת מחדל

# קריאת כל קבצי התמונות
image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# בדיקה שיש קבצים
if not image_files:
    raise Exception('No image files found in the images folder.')

# פתיחת התמונות
images = []
for file in image_files:
    img_path = os.path.join(images_folder, file)
    img = Image.open(img_path).convert('RGB')  # להמיר ל-RGB בשביל PDF
    images.append(img)

# שמירת התמונות לקובץ PDF אחד
output_path = os.path.join(output_folder, pdf_name)
images[0].save(output_path, save_all=True, append_images=images[1:])

print(f"PDF created successfully at {output_path}")
