import os
import csv
from ocr import extract_text
from llm_translate import translate_text


# Input image directory
image_dir = "images"
output_csv = "outputs/translation_results.csv"

# Ensure output dir exists
os.makedirs("outputs", exist_ok=True)

# CSV Header
header = ["filename", "ancient_tamil_text", "modern_tamil_translation", "english_translation"]

# Create/open the output CSV
with open(output_csv, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_dir, filename)
            print(f"\n🔍 Processing: {filename}")

            # Step 1: OCR
            ancient_text = extract_text(image_path)


            if not ancient_text.strip():
                print("❌ No text extracted.")
                continue

            # Step 2: Translation (via LLM)
            translation = translate_text(ancient_text)

            # If you want to split modern Tamil and English, adjust here:
            modern_tamil = translation.get("modern_tamil") if isinstance(translation, dict) else translation
            english = translation.get("english") if isinstance(translation, dict) else ""

            # Log to CSV
            writer.writerow([filename, ancient_text, modern_tamil, english])
            print("✅ Logged result.\n")
