import discord
import os
import random
client = discord.Client()

banned_words = [' u ', ' U ', ' ur ', ' Ur ', ' UR ']
rick_roll = [
    'https://pbs.twimg.com/media/Esg4czOVoAA4Qnq?format=jpg&name=medium',
    'https://pbs.twimg.com/media/Esg4dapVoAALIkh?format=jpg&name=medium',
    'https://pbs.twimg.com/media/Esg4d7LVoAYjLKZ?format=jpg&name=medium'
]
sorry_sayings = [
    "Sorry, man! Don't hate me 'cause I'm beautiful! Get rid of that yee yee ass haircut!!",
    "Nah man, I'll see you at work",
    "OKAY OKAY No need to be so sensitive. GOSH people of these days.",
    "Oh really? YOU are irritated? YOU are? YOU?",
    "https://media.giphy.com/media/UiZpBJIwdJ34k/giphy.gif",
    "'OBLITERATED!' \n --Raze. "
]
all_Inputs = [
    " 'typo again?' -- Provide someone in need with a keybaord.",
    " 'mind blown' -- Oh your mind is blown? Tell me about it.",
    " 'good stuff' -- Certainly the person has some GOOOOOOOD stuff.",
    " 'mood kharab' -- Why do you ruin my mood?",
    " 'Happy god laptop day' -- Happy god laptop day",
    " 'Happy milk day' -- Happy milk day",
    " 'Sab moh maya hai' -- For the times when everything feels like moh maya",
    " NEVER GONNA SAY GOODBYE",
    " //or you could try greeting me\\",
    "MADE BY OJAS. I know I know, thank you thank you. YES OKAY! THANK YOU. Oh now this is becoming flattery. I know I am awesome thank you thank you."

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
    if message.content.startswith('what can I do?') or message.content.startswith('What can I do?'):
        await message.channel.send('You can do a whole bunch of stuff with this bot!')
        await message.channel.send('You can type the following things: ')
        for thingsToSay in range(no_inputs):
            await message.channel.send(all_Inputs[thingsToSay])

    #greeting
    if message.content.startswith('hey') or message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('yo') or message.content.startswith('heyo') or message.content.startswith('Hello') or message.content.startswith('Hi') or message.content.startswith('Yo') or message.content.startswith('Heyo'):
        await message.channel.send('HELLO!')
    #hey mr arnab
    if message.content.startswith('Get me a time magazine'):
        mrarnab = 'https://cdn.discordapp.com/attachments/802613961610231879/802627200472842300/TIME.png'
        await message.channel.send(mrarnab)
    #please don't use u
    if any(word in message.content for word in banned_words):
        pleaseno = 'https://pbs.twimg.com/media/Esg2D42VoAInGYd?format=png&name=small'
        await message.channel.send(pleaseno)
    #user types typo again?
    if message.content.startswith('typo again?') or message.content.startswith('Typo again?'):
        typo = 'https://media1.tenor.com/images/1fa1ceb9b698b9071fa3e5a1cc0224bb/tenor.gif?itemid=20073354'
        await message.channel.send(typo)
    #user types mind blown
    if message.content.startswith('mind blown') or message.content.startswith('Mind blown'):
        mindblown = 'https://tenor.com/view/mind-blown-head-explode-amazing-shocking-wow-gif-19681784'
        await message.channel.send(mindblown)
    #user types good stuff
    if message.content.startswith('good stuff') or message.content.startswith('Good stuff'):
        thumbsup = 'https://tenor.com/view/boy-kid-computer-thumbs-up-face-gif-9548945'
        await message.channel.send(thumbsup)
    #mood kharab
    if message.content.startswith('mood kharab'):
        moodkharab = 'https://pbs.twimg.com/media/Esg1vmeU0AAL6TR?format=png&name=small'
        await message.channel.send(moodkharab)
    #bye
    if message.content.startswith('bye') or message.content.startswith('Bye') or message.content.startswith('Goodbye') or message.content.startswith('goodbye'):
        bye = 'https://tenor.com/view/peace-out-bye-gif-10267883'
        await message.channel.send(bye)
    #Happy god laptop day
    if message.content.startswith('Happy god laptop day') or message.content.startswith('I miss him') or message.content.startswith('happy god laptop day'):
        laptopday = 'https://pbs.twimg.com/media/Esgq9i1VcAEK-4t?format=jpg&name=medium'
        await message.channel.send(laptopday)
        await message.channel.send('@everyone ')
    #happy milk day
    if message.content.startswith('Happy milk day') or message.content.startswith('happy milk day'):
        milkday = 'https://tenor.com/view/martin-luther-king-jr-day-mlk-day-mlk-weekend-martin-luther-king-i-have-a-dream-gif-16077544'
        await message.channel.send(milkday)
        await message.channel.send('@everyone ')
    #shut up ojas
    if message.content.startswith('Shut up, Ojas') or message.content.startswith('shut up, ojas') or  message.content.startswith('SHUT UP, OJAS') or message.content.startswith('Shut up ojas') or message.content.startswith('shut up ojas') or message.content.startswith('SHUT UP OJAS'):
        await message.channel.send(random.choice(sorry_sayings))
    #We're no strangers to love
    if message.content.startswith("Never gonna") or message.content.startswith("never gonna"):
        await message.channel.send(random.choice(rick_roll))
    #Sab Moh Maya hai
    if message.content.startswith('sab moh maya hai') or message.content.startswith('Sab moh maya hai'):
        mohmaya = 'https://pbs.twimg.com/media/Esg-rXCVoAIXly2?format=png&name=900x900'
        await message.channel.send(mohmaya)
#Token for bot    
client.run('Nzk4OTY0ODc3NzYyODg3NzUy.X_8sBg.o86mF7Ac7XmBWHJXAgLJVwn4sEg')