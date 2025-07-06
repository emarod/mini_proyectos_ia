'use client';

import React, { useState } from 'react';

const Home: React.FC = () => {
  const [fileContent, setFileContent] = useState<string>('');
  const [fileName, setFileName] = useState<string>('');

  const handleUpload = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/upload-ocr", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        setFileContent("⚠️ Error en el backend al procesar la imagen.");
        return;
      }

      const data = await response.json();
      const extractedText = data.text?.trim();

      if (!extractedText) {
        setFileContent("⚠️ No se pudo extraer texto de la imagen.");
      } else {
        setFileContent(extractedText);
      }
    } catch (error) {
      console.error("Error en el cliente:", error);
      setFileContent("⚠️ Error al conectar con el backend.");
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && file.type.startsWith("image/")) {
      setFileName(file.name);
      handleUpload(file);
    } else {
      alert("Sube una imagen válida (JPG, PNG)");
    }
  };

  return (
    <div className="flex flex-col items-center p-8">
      <h1 className="text-2xl font-bold mb-4">Cargar imagen</h1>

      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="mb-4"
      />

      {fileName && <p className="font-semibold">Imagen: {fileName}</p>}

      {fileContent && (
        <pre className="mt-4 p-4 border rounded bg-gray-100 max-w-xl overflow-auto whitespace-pre-wrap">
          {fileContent}
        </pre>
      )}
    </div>
  );
};

export default Home;
