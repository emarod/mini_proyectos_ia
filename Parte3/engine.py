import spacy
from spacy.matcher import PhraseMatcher
from database import compradores, deudores

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

# Crear matcher basado en frases
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Diccionario de frases por intención
intent_phrases = {
    "mejores_compradores": [
        "mejores compradores",
        "compradores destacados",
        "quién compró más",
        "quién ha comprado más",
        "top compradores",
        "comprador que gastó más",
    ],
    "mayores_deudores": [
        "mayores deudores",
        "quién debe más",
        "deudores con más deuda",
        "deuda más alta",
        "quién tiene más deuda",
    ],
    "contar_compradores": [
        "cuántos compradores hay",
        "número de compradores",
        "total de compradores",
        "cuál es el total de compradores",
    ],
    "contar_deudores": [
        "cuántos contar_deudores hay",
        "número de contar_deudores",
        "total de contar_deudores",
        "cuál es el total de contar_deudores",
    ],
}

# Agregar frases al matcher
for intent, frases in intent_phrases.items():
    patterns = [nlp(text) for text in frases]
    matcher.add(intent, patterns)

# ----------------------------
# Función para detectar intención
# ----------------------------
def detectar_intencion(pregunta: str) -> str:
    doc = nlp(pregunta)
    matches = matcher(doc)

    if not matches:
        return "desconocido"

    # Retorna el intent del primer match
    match_id, start, end = matches[0]
    return nlp.vocab.strings[match_id]

# ----------------------------
# Función para procesar respuesta
# ----------------------------
def procesar_pregunta(pregunta: str) -> str:
    intent = detectar_intencion(pregunta)

    if intent == "mejores_compradores":
        top = sorted(compradores, key=lambda x: x["total_compras"], reverse=True)
        texto = "\n".join([f"- {c['nombre']} (${c['total_compras']})" for c in top[:3]])
        return f"Los mejores compradores son:\n{texto}"

    elif intent == "mayores_deudores":
        top = sorted(deudores, key=lambda x: x["monto_adeudado"], reverse=True)
        texto = "\n".join([f"- {d['nombre']} (${d['monto_adeudado']})" for d in top[:3]])
        return f"Los deudores con montos más altos son:\n{texto}"

    elif intent == "contar_compradores":
        return f"Hay {len(compradores)} compradores registrados."

    else:
        return "Lo siento, no entendí la pregunta. Intenta reformularla con otras palabras."
