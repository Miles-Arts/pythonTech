import discord
import requests

# Clave API de Jooble
API_KEY = "925c61ce-0418-48cc-a504-5b9fd4b26ebf"

# Configuración de permisos para el bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Función para buscar vacantes utilizando la API de Jooble
def buscar_vacantes(palabra_clave, ubicacion="remote"):
    url = f"https://jooble.org/api/{API_KEY}/"
    data = {
        "keywords": palabra_clave,
        "location": ubicacion,
        "page": 1,
        "size": 5  # Número de vacantes que quieres recuperar
    }
    print(f"Enviando solicitud a {url} con datos: {data}")
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP 4xx/5xx
        print(f"Respuesta recibida: {response.json()}")
        return response.json().get("jobs", [])
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return []

# Evento que se ejecuta cuando el bot se conecta a Discord
@client.event
async def on_ready():
    print(f'{client.user} se ha conectado a Discord!')

# Evento que se ejecuta cuando el bot recibe un mensaje
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!vacantes'):
        comando = message.content.split(' ')
        palabra_clave = comando[1] if len(comando) > 1 else "desarrollador"
        ubicacion = comando[2] if len(comando) > 2 else "remote"
        vacantes = buscar_vacantes(palabra_clave, ubicacion)
        if vacantes:
            for vacante in vacantes:
                embed = discord.Embed(
                    title=vacante['title'],
                    url=vacante['link'],
                    description=vacante['company'],
                    color=discord.Color.blue()
                )
                embed.add_field(name="Ubicación", value=vacante['location'], inline=True)
                embed.add_field(name="Salario", value=vacante.get('salary', 'No especificado'), inline=True)
                embed.add_field(name="Descripción", value=vacante.get('snippet', 'No disponible'), inline=False)
                await message.channel.send(embed=embed)
        else:
            await message.channel.send("No se encontraron vacantes.")