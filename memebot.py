import discord
import os

client = discord.Client()

banned_words = [' u ', ' U ', ' ur ', ' Ur ', ' UR ']

all_Inputs = [
    " 'typo again?' -- Provide someone in need with a keybaord.",
    " 'mind blown' -- Oh your mind is blown? Tell me about it.",
    " 'good stuff' -- Certainly the person has some GOOOOOOOD stuff.",
    " 'mood kharab' -- Why do you ruin my mood?",
    " NEVER GONNA SAY GOODBYE",
    " //or you could try greeting me\\"
]
no_inputs = len(all_Inputs)

@client.event

async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity=discord.Game('"what can I do?"'))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #user types what all can I do?
    if message.content.startswith('what can I do?'):
        await message.channel.send('You can do a whole bunch of stuff with this bot!')
        await message.channel.send('You can type the following things: ')
        for thingsToSay in range(no_inputs):
            await message.channel.send(all_Inputs[thingsToSay])

    #greeting
    if message.content.startswith('hey') or message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('yo') or message.content.startswith('heyo') or message.content.startswith('Hello') or message.content.startswith('Hi') or message.content.startswith('Yo') or message.content.startswith('Heyo'):
        await message.channel.send('HELLO!')
    #hey mr arnab
    if message.content.startswith('hey mr. arnab'):
        mrarnab = 'https://cdn.discordapp.com/attachments/802613961610231879/802627200472842300/TIME.png'
        await message.channel.send(mrarnab)
    #please don't use u
    if any(word in message.content for word in banned_words):
        pleaseno = 'https://pbs.twimg.com/media/EsV_mSAU0AM2PC1?format=png&name=small'
        await message.channel.send(pleaseno)
    #user types typo again?
    if message.content.startswith('typo again?'):
        typo = 'https://media1.tenor.com/images/1fa1ceb9b698b9071fa3e5a1cc0224bb/tenor.gif?itemid=20073354'
        await message.channel.send(typo)
    #user types mind blown
    if message.content.startswith('mind blown'):
        mindblown = 'https://tenor.com/view/mind-blown-head-explode-amazing-shocking-wow-gif-19681784'
        await message.channel.send(mindblown)
    #user types good stuff
    if message.content.startswith('good stuff'):
        thumbsup = 'https://tenor.com/view/boy-kid-computer-thumbs-up-face-gif-9548945'
        await message.channel.send(thumbsup)
    #mood kharab
    if message.content.startswith('mood kharab'):
        moodkharab = 'https://pbs.twimg.com/media/EsV_Mi-UcAA_vy5?format=jpg&name=360x360'
        await message.channel.send(moodkharab)
    #bye
    if message.content.startswith('bye') or message.content.startswith('Bye') or message.content.startswith('Goodbye') or message.content.startswith('goodbye'):
        bye = 'https://tenor.com/view/peace-out-bye-gif-10267883'
        await message.channel.send(bye)
#Token for bot    
client.run('Nzk4OTY0ODc3NzYyODg3NzUy.X_8sBg.o86mF7Ac7XmBWHJXAgLJVwn4sEg')