import discord
import responses
import random
import string
from discord.ext import commands

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'TOKEN'
    intents = discord.Intents.all()
    intents.members = True
    intents.messages = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        game = discord.Game("PrisonOP", url="https://imgur.com/a/SkK2VJS")
        await client.change_presence(status=discord.Status.online, activity=game)

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if message.channel.type == discord.ChannelType.private:
            # Do not process the message
            if message.content == '-nitro':
                await message.author.send('Nu poti folosi comanda `-nitro` aici, incearca pe un anumit server.')
        elif message.content == '-nitro':
            rndint = random.randint(1, 4)

            c = random.sample(string.digits, rndint)
            b = random.sample(string.ascii_letters, 13)
            characters = list(b + c)

            print(str(rndint) + ' cifre')

            random.shuffle(characters)
            nitro = 'https://discord.gift/' + str(''.join(characters[:16]))
            await message.channel.send('Am trimis un cod de nitro la tine, ' + str(message.author) + ' , in dm. Daca nu l-ai primit, accepta mesajele de la boti sau verifica-ti inca o data mesajele!')
            await message.author.send(nitro)
            await message.add_reaction("✅")

        if "lola" in user_message.lower():
            # Send message to the user who sent the message
            await message.channel.send("Lola este un caine foarte mic si iubit. Prietenii ei sunt xSenny, Anat0lica, drimuletzu si putin alexandradty. Stapanul ei este Drimuletzu si magarul ei principal este Edi2144.")

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")



    client.run(TOKEN)
