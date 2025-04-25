import cv2
import pytesseract
import os

# ✅ Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ✅ Set the path to the tessdata folder (where tam.traineddata is located)
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"



def extract_text(image_path):
    try:
        image = cv2.imread(image_path)

        # ✅ Preprocessing starts here
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        thresh = cv2.adaptiveThreshold(
            blurred, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )

        # Optional: show the result for visual debugging
        cv2.imshow("Preprocessed", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # ✅ OCR using Tamil language model
        custom_config = r'--oem 3 --psm 6 -l tam'
        text = pytesseract.image_to_string(thresh, config=custom_config)
        return text.strip()

    except Exception as e:
        print(f"[❌] OCR failed: {e}")
        return ""
