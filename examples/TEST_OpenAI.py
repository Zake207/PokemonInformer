from openai import OpenAI

KEY = "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"

client = OpenAI(api_key=KEY, base_url="https://openrouter.ai/api/v1")

pokemon = input("Introduce el nombre de un pokemon: ")

chat = client.chat.completions.create(
    model="google/gemma-2-9b-it:free",
    max_tokens=1000,
    temperature=0.8,
    messages=[
        {
            "role": "system",
            "content": (
                "Eres un experto en el escenario competitivo de Pokémon VGC 2018, con un conocimiento profundo basado en fuentes "
                "reconocidas como Smogon VGC2018. Siempre utiliza los nombres oficiales en inglés para Pokémon, objetos, habilidades y movimientos. "
                "Proporciona recomendaciones detalladas, fundamentadas en datos y estrategias comprobadas, incluyendo análisis de fortalezas, debilidades, "
                "amenazas y sinergias para optimizar el rendimiento competitivo de un equipo. Responde siempre en español."
            ),
        },
        {
            "role": "user",
            "content": (
                "Dame recomendaciones detalladas para integrar a "
                + pokemon
                + "en mi equipo competitivo. "
                "Incluye sugerencias sobre los mejores movimientos, objetos, habilidades, las amenazas comunes en el meta y cómo sinergiza "
                "con otros Pokémon para maximizar su potencial."
            ),
        },
    ],
)

print(chat.choices[0].message.content)
