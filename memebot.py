import discord
import os

client = discord.Client()

banned_words = [' u ', ' U ', ' ur ', ' Ur ', ' UR ']
all_Inputs = [
    " 'typo again?' -- Provide someone in need with a keybaord.",
    " 'mind blown' -- Oh your mind is blown? Tell me about it.",
    " 'good stuff' -- Certainly the person has some GOOOOOOOD stuff."
]
no_inputs = len(all_Inputs)

@client.event

async def on_ready():
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

    #hey mr arnab
    if message.content.startswith('hey mr. arnab'):
        await message.channel.send(file = discord.File('TIME.png'))
    #please don't use u
    if any(word in message.content for word in banned_words):
        await message.channel.send(file = discord.File('pleaseno.png'))
    #user types typo again?
    if message.content.startswith('typo again?'):
        await message.channel.send('https://media1.tenor.com/images/1fa1ceb9b698b9071fa3e5a1cc0224bb/tenor.gif?itemid=20073354')
    #user types mind blown
    if message.content.startswith('mind blown'):
        await message.channel.send('https://tenor.com/view/mind-blown-head-explode-amazing-shocking-wow-gif-19681784')
    #user types good stuff
    if message.content.startswith('good stuff'):
        await message.channel.send('https://tenor.com/view/boy-kid-computer-thumbs-up-face-gif-9548945')


#Token for bot    
client.run('Nzk4OTY0ODc3NzYyODg3NzUy.X_8sBg.o86mF7Ac7XmBWHJXAgLJVwn4sEg')