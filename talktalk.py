import discord
import asyncio

token = "insert token here"
client=discord.Client()

@client.event
async def on_ready():
    print("Logged In As")
    print(client.user.name)
    print(client.user.id)
    print("------------")

@client.event
async def on_message(message):
    if message.content.startswith("?"):
        if "hello" in message.content:
            await client.send_message(message.channel, "Hello there, " + message.author.mention, tts=True)
        elif "how are you" in message.content: 
              await client.send_message(message.channel, "I'm good, thanks for asking", tts=True)
              
client.run(token)