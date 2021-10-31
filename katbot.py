from nltk.chat.util import Chat, reflections
mis_reflexions = {
    "ir": "fui",
    "hola": "hey",
    "adios": "chao",
    "bien": "bien"
}
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]
    ],
    [
        r"Cual es tu nombre ?",
        ["Mi nombre es Katbot ",]
    ],
    [
        r"como estas ?",
        ["Bien y tu?",]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal?",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"finalizar|chao|adios|me voy",
        ["Chao","Fue bueno hablar contigo"]
    ],
]
def chatear():
    #MENSAJE POR DEFECTO
    print("Hola soy Katbot, escribe algo para comenzar")
    chat = Chat(pares, mis_reflexions)
    chat.converse()
if __name__ == "__main__":
    chatear()