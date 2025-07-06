
# Proyecto Multi-partes: OCR, Scraping, Chatbot y CNN Predictiva

---

## Parte 1 – OCR con FastAPI y Frontend React

1. Descargar e instalar **Tesseract OCR** desde su sitio oficial:  
   https://github.com/tesseract-ocr/tesseract

2. En la carpeta del proyecto ejecutar el backend:  
   ```bash
   uvicorn api:app --reload
   ```

3. En otra terminal ejecutar el frontend:  
   ```bash
   npm run dev
   ```

4. Abrir en el navegador:  
   [http://localhost:3000](http://localhost:3000)

---

## Parte 2 – Web Scraping y API con FastAPI

1. En la carpeta del proyecto ejecutar:  
   ```bash
   uvicorn main:app --reload
   ```

2. Acceder a la documentación automática de la API:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Consumir el servicio `/scrape` para iniciar scraping.

4. Consumir el servicio `/products` con algún filtro para obtener productos.

---

## Parte 3 – Chatbot + NLP + Consulta Dinámica

1. En la carpeta del proyecto ejecutar:  
   ```bash
   uvicorn main:app --reload
   ```

2. Acceder a la documentación:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Lanzar preguntas al chatbot como por ejemplo:  
   - ¿Quiénes son los mejores compradores?  
   - ¿Cuáles son los deudores más altos?  
   - ¿Cuántos compradores hay?

---

## Parte 4 – CNN Predictiva con PyTorch y FastAPI

1. Entrenar el modelo ejecutando:  
   ```bash
   python train_cnn.py
   ```

2. Levantar el servidor backend:  
   ```bash
   uvicorn main:app --reload
   ```

3. Acceder a la documentación:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

4. Consumir el servicio `/predict-upload` y subir alguna imagen para predecir.  
   Puedes usar imágenes dentro de la carpeta del proyecto.
