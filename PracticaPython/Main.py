from textblob import TextBlob

def analizar_sentimiento(texto):
    analisis = TextBlob(texto)
    # Traducimos al inglés porque TextBlob funciona mejor en ese idioma internamente
    if analisis.sentiment.polarity > 0:
        return "Positivo 😊"
    elif analisis.sentiment.polarity < 0:
        return "Negativo ☹️"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    print("--- Analizador de Sentimientos ---")
    frase = input("Escribe algo en inglés (ej: I love this project): ")
    resultado = analizar_sentimiento(frase)
    print(f"El sentimiento es: {resultado}")