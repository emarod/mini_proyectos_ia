import spacy
from database import compradores, deudores

nlp = spacy.load("es_core_news_sm")

def detectar_intencion(pregunta: str) -> str:
    pregunta = pregunta.lower()
    if "mejor" in pregunta and "comprador" in pregunta:
        return "mejores_compradores"
    if "deudores más altos" in pregunta or "deben más" in pregunta:
        return "mayores_deudores"
    if "cuántos compradores" in pregunta:
        return "contar_compradores"
    return "desconocido"

def procesar_pregunta(pregunta: str) -> str:
    intencion = detectar_intencion(pregunta)

    if intencion == "mejores_compradores":
        top = sorted(compradores, key=lambda x: x["total_compras"], reverse=True)
        texto = "\n".join([f"- {c['nombre']} (${c['total_compras']})" for c in top[:3]])
        return f"Los mejores compradores son:\n{texto}"

    elif intencion == "mayores_deudores":
        top = sorted(deudores, key=lambda x: x["monto_adeudado"], reverse=True)
        texto = "\n".join([f"- {d['nombre']} (${d['monto_adeudado']})" for d in top[:3]])
        return f"Los deudores con montos más altos son:\n{texto}"

    elif intencion == "contar_compradores":
        return f"Hay {len(compradores)} compradores registrados."

    else:
        return "Lo siento, no entendí la pregunta. ¿Puedes reformularla?"
