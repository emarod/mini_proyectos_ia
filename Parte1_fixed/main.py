from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract
import io

print("main.py ejecutado")
pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.js dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-ocr")
async def upload_ocr(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        print(f"Archivo recibido: {file.filename} ({file.content_type})")

        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)

        print("Texto extraído:", text)
        return {"text": text}

    except Exception as e:
        print("Error procesando imagen:", str(e))
        raise HTTPException(status_code=500, detail=f"Error procesando imagen: {str(e)}")
