from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from torchvision import transforms
from PIL import Image
import io
from model import CNN

app = FastAPI()

# Cargar modelo
model = CNN()
model.load_state_dict(torch.load("mnist_cnn.pth", map_location="cpu"))
model.eval()

# Preprocesamiento
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

@app.post("/predict-upload")
async def predict_upload(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("L")

    tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(tensor)
        predicted = torch.argmax(output, dim=1).item()

    return {"prediction": predicted}
