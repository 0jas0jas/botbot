# coding=utf-8

import asyncio
import discord
import os
import random
from datetime import datetime
import pytz
import wolframalpha
import http.client
import random
import praw
from discord.ext import commands
from discord.utils import get
from PyDictionary import PyDictionary

#dictionary
dictionary=PyDictionary()

#wolframAlpha
app_id = "8GUU89-YTLG2XLPRR"

#reddit
reddit = praw.Reddit(client_id = "PiZLpYlDOi67-Q", client_secret = "Mup9D2lvnNOvaBPRUBp4P3SStBa1JA", user_agent = "memehub")


# client = discord.Client()
client = commands.Bot(command_prefix='p', help_command=None)
banned_words = [' u ', ' U ', ' ur ', ' Ur ', ' UR ']

reddit_subreddits = [
    "memes",
    "dankmemes",
    "meme",
]

time_sayings = [
    "* airport lady voice *",
    "Okay I am going to say this ONCE-- I. Am. Not. A. Clock. \n BTW",
    "Time is like a waterfall, it's always running...",
    "Time is like a box of chocola- \n Nah, man.",
    "Run TIME Run",
    "TAAAAAAAAAAAAAAAAAAAIME",
    "What IS time? Time is an idea",
    "Time kya hai? Time ek soch hai"
]

rick_roll = [
    'https://pbs.twimg.com/media/Esg4czOVoAA4Qnq?format=jpg&name=medium',
    'https://pbs.twimg.com/media/Esg4dapVoAALIkh?format=jpg&name=medium',
    'https://pbs.twimg.com/media/Esg4d7LVoAYjLKZ?format=jpg&name=medium'
]

sorry_sayings_mahi = [
    "lalalalala i can't hear you",
    "*insert some cringe but clever comeback*",
    "did you know that you're a bench (bitch). also sorry, i'll shut up k thanks bye",
    "hey! my kachra self esteem says that to me too!",
    "jo bolta hai wahi hota hai \n -a 7 year old's VERY EFFECTIVE comeback(ik it doesn't make sense with the shut up-)",
    "https://www.youtube.com/watch?v=D-UmfqFjpl0",
    "and to that i say, pa. hapapapa. hathagapapapaa.",
    "tell ojas to shut up. HE'S THE LOUD ONE!",
    "you're so mean i won't send you doggo pictures anymore",
    "UNFRIEND ME"
]

sorry_sayings = [
    "https://0jas0jas.github.io/RiskOfRain/",
    "Sorry, man! Don't hate me 'cause I'm beautiful! Get rid of that yee yee ass haircut!!",
    "Nah man, I'll see you at work",
    "OKAY OKAY No need to be so sensitive. GOSH people of these days.",
    "Oh really? YOU are irritated? YOU are? YOU?",
    "https://media.giphy.com/media/UiZpBJIwdJ34k/giphy.gif",
    "My grandfather used to say: es yogins prétendent que, de toutes les énergies que renferme le corps humain, la plus haute est celle qu’ils appellent ojas. Or, cet ojas est emmagasiné dans le cerveau, et plus il y a d’ojas dans la tête d’un homme, plus l’homme est puissant, intelligent, et spirituellement vigoureux. Tel homme peut employer de belles paroles et exprimer de belles pensées sans faire aucune impression sur ceux qui l’écoutent ; tel autre, sans beau langage et sans belles idées, charme par ses paroles. Chacun de ses mouvements a de la puissance. C’est la puissance d’ojas. Or, en chaque homme se trouve emmagasinée une quantité plus ou moins grande d’ojas. Toutes les forces qui travaillent dans le corps deviennent à leur degré suprême, des ojas. Il faut vous rappeler qu’il ne s’agit là que d’une transformation. La même force qui est à l’œuvre en dehors de nous comme électricité ou comme magnétisme se changera en force intérieure ; les mêmes forces qui opèrent comme énergie musculaire se transformeront en ojas. Les yogins nous disent que la partie de l’énergie humaine qui s’exprime comme énergie sexuelle, comme pensée sexuelle, se transforme facilement en ojas lorsqu’on la refrène et qu’on la dirige. I WILL NEVER SHUT UP MUAHAHAHAHAHAHA ",
    "You got it, Boss.",
    "911. What's your emergency?",
    "You see, I just got my driver's lisence. Just like we talked about and you were SOOOOOOOO darn excited for me to finally drive up to your house but you know what I did? DO YOU KNOW? I drove through the freaking suburbs!",
    "Ojas: * shutting up noises * ",
    "No you!",
    "* ignores *",
    "https://youtu.be/BLUkgRAy_Vo",
    "[insert sick burn here]",
    "WoW Ojas won't just shut up",
    "* sings rap god *"
]

yoda = [
    "https://preview.redd.it/qv3lyh7byyn61.png?width=960&crop=smart&auto=webp&s=0492ffbd8e8a7e38271f6fa63f981e4d05e88c52",
    "https://media.giphy.com/media/Wn74RUT0vjnoU98Hnt/giphy.gif",
    "https://media.giphy.com/media/6fScAIQR0P0xW/giphy.gif",
    "https://media.giphy.com/media/Ll1rEkDebTIdO/giphy.gif",
    "https://media.giphy.com/media/SleotgmotWahW/giphy.gif",
    "https://media.giphy.com/media/33iqmp5ATXT5m/giphy.gif",
    "https://media.giphy.com/media/zQhFEBrX6plKg/giphy.gif",
    "https://media.giphy.com/media/fItgT774J3nWw/giphy.gif",
    "https://media.giphy.com/media/11ocEaLDZafNHa/giphy.gif",    
]

sparrow = [
    "https://media.giphy.com/media/o4Hy165vDlmDe/giphy.gif",
    "https://media.giphy.com/media/idY2ToQsTzyCF7Viyd/giphy.gif",
    "https://media.giphy.com/media/2PmMiUc9OH4lO/giphy.gif",
    "https://media.giphy.com/media/Urb2J1xGRDjN6zljXH/giphy.gif",
    "https://media.giphy.com/media/102oHwgyIqWwQo/giphy.gif",
    "https://media.giphy.com/media/fdbMx2WGKqaze/giphy.gif"
    
]

head_fields = [
    " 'typo again?'",
    " 'mind blown'",
    " 'good stuff'",
    " 'mood kharab'",
    " 'mood fresh'",
    " 'okay'",
    " 'Captain sparrow'",
    " 'Master Yoda'",
    " 'Get some help'",
    " 'Understandable'",
    " 'Happy god laptop day'",
    " 'Happy milk day'",
    " Type anything ending with '='",
    " meme [subreddit]",
    " 'Time'",
    " 'Sab mohmaya hai'",
    " 'Arrey bohot interesting hai'",
    " -----------------",
    " -----------------",
]
text_fields = [
    "Provide someone in need with a keybaord.",
    "Oh your mind is blown? Tell me about it.",
    "Certainly the person has some GOOOOOOOD stuff.",
    "Why do you ruin my mood?",
    "Why do you freshen my mood?",
    "Okay.",
    "Who's our favourite pirate!?",
    "All Hail Master Yoda",
    "Stop it. Get some help.",
    "Understandable have a good day.",
    "Happy god laptop day",
    "Happy milk day",
    "Calculations Calculations Calculations",
    "Get a random meme by typing 'meme' or get memes from your favourite subreddit.",
    "Time. That's deep, man!",
    "For the times when everything feels like moh maya",
    "Common Ojas sayings.",
    "Ask a 'What is [something]' question!",
    "~~NEVER~~ GONNA SAY GOODBYE",

]
no_inputs = len(head_fields)
no_sorry_sayings = len(sorry_sayings)
no_sorry_sayings_mahi = len(sorry_sayings_mahi)
no_rick_roll = len(rick_roll)
no_time_sayings = len(time_sayings)
no_subreddits = len(reddit_subreddits)
no_yoda = len(yoda)
no_sparrow = len(sparrow)
# print(all_Inputs)
@client.event

async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity=discord.Game('"what can I do?"'))
    print('HELL YEAH! {0.user} IS ALIVEEEEE'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #user types what all can I do?
    if message.content.startswith('what can I do?') or message.content.startswith('What can I do?'):
        head = "You can do a whole bunch of things with this bot! \n Try typing one of the following:"
        abilitiesEmbed = discord.Embed(title = "Welcome to meme hub!", description = head, color=0xeb4034)
        for thingsToSay in range(no_inputs):
            abilitiesEmbed.add_field(name=head_fields[thingsToSay], value= text_fields[thingsToSay], inline= False)
        abilitiesEmbed.set_footer(text= "MADE BY OJAS. I know I know, thank you thank you. YES OKAY! THANK YOU. Oh now this is becoming flattery. I know I am awesome thank you thank you.")
        await message.channel.send(embed = abilitiesEmbed)
        
    #hey mr arnab
    if message.content.startswith('Get me a time magazine') or message.content.startswith('get me a time magazine'):
        mrarnab = 'https://cdn.discordapp.com/attachments/802613961610231879/802627200472842300/TIME.png'
        await message.channel.send(mrarnab)

    # #please don't use u
    # if any(word in message.content for word in banned_words):
    #     pleaseno = 'https://pbs.twimg.com/media/Esg2D42VoAInGYd?format=png&name=small'
    #     await message.channel.send(pleaseno)

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
    if message.content.startswith('mood kharab') or message.content.startswith('Mood kharab'):
        moodkharab = 'https://pbs.twimg.com/media/Esg1vmeU0AAL6TR?format=png&name=small'
        await message.channel.send(moodkharab)

    if message.content.startswith('randNum'):
        randommes = random.randrange(1, 100, 1)
        await message.channel.send(randommes)

    #mood fresh
    if message.content.startswith('mood fresh') or message.content.startswith('Mood fresh'):
        moodfresh = 'https://i.redd.it/om1apvxcsej61.png'
        await message.channel.send(moodfresh)

    #bye
    if message.content.startswith('bye') or message.content.startswith('Bye') or message.content.startswith('Goodbye') or message.content.startswith('goodbye') or message.content.startswith('Peace out') or message.content.startswith('peace out'):
        bye = 'https://tenor.com/view/peace-out-bye-gif-10267883'
        await message.channel.send(bye)

    #Happy god laptop day
    if message.content.startswith('Happy god laptop day') or message.content.startswith('I miss him') or message.content.startswith('happy god laptop day'):
        laptopday = 'https://pbs.twimg.com/media/Esgq9i1VcAEK-4t?format=jpg&name=medium'
        await message.channel.send(laptopday)
        
    #happy milk day
    if message.content.startswith('Happy milk day') or message.content.startswith('happy milk day'):
        milkday = 'https://tenor.com/view/martin-luther-king-jr-day-mlk-day-mlk-weekend-martin-luther-king-i-have-a-dream-gif-16077544'
        await message.channel.send(milkday)

    #shut up ojas
    if message.content.startswith('Shut up, Ojas') or message.content.startswith('shut up, ojas') or  message.content.startswith('SHUT UP, OJAS') or message.content.startswith('Shut up ojas') or message.content.startswith('shut up ojas') or message.content.startswith('SHUT UP OJAS'):
        randombleh = random.randrange(0, no_sorry_sayings, 1)
        await message.channel.send(sorry_sayings[randombleh])

    #shut up mahi
    if message.content.startswith('Shut up, Mahi') or message.content.startswith('shut up, mahi') or  message.content.startswith('SHUT UP, MAHI') or message.content.startswith('Shut up mahi') or message.content.startswith('shut up mahi') or message.content.startswith('SHUT UP MAHI'):
        randombleh = random.randrange(0, no_sorry_sayings_mahi, 1)
        await message.channel.send(sorry_sayings_mahi[randombleh])

    #We're no strangers to love
    if message.content.startswith("Never gonna") or message.content.startswith("never gonna"):
        randombleh = random.randrange(0, no_rick_roll, 1)
        await message.channel.send(rick_roll[randombleh])

    #Sab Moh Maya hai
    if message.content.startswith('sab moh maya hai') or message.content.startswith('Sab moh maya hai') or message.content.startswith('Sab mohmaya hai') or message.content.startswith('sab mohmaya hai'):
        mohmaya = 'https://pbs.twimg.com/media/Esg-rXCVoAIXly2?format=png&name=900x900'
        em = discord.Embed(color=discord.Color.red())
        em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        em.set_image(url=mohmaya)
        await message.channel.send(embed=em)
        await message.delete()

    #soch hai/is an idea
    if message.content.endswith(" kya hai?"):
        cropped_message = message.content.removesuffix(' kya hai?')
        await message.channel.send(cropped_message + ' ek soch hai!🤯💭')
    elif message.content.endswith(" kya hai"):
        cropped_message = message.content.removesuffix(' kya hai')
        await message.channel.send(cropped_message + ' ek soch hai!🤯💭')
    elif message.content.startswith("What is "):
        removalquestion = message.content.removesuffix('?')
        cropped_message = removalquestion.removeprefix('What is ')
        await message.channel.send(cropped_message + ' is an idea!🤯💭')
    elif message.content.startswith("what is "):
        removalquestion = message.content.removesuffix('?')
        cropped_message = removalquestion.removeprefix('what is ')
        await message.channel.send(cropped_message + ' is an idea!🤯💭')

    #ARREY BOHOT INTERESTING HAI
    if message.content.startswith("Arrey bohot interesting hai") or message.content.startswith("arrey bohot interesting hai"):
        interesting = 'https://media.giphy.com/media/xtSLPH1I0S7p4hJ4Ty/giphy.gif'
        await message.channel.send(interesting)
    
    #time
    if message.content.startswith("Time") or message.content.startswith("time"):
        time = pytz.timezone('Asia/Kolkata')
        tame = datetime.now(time)
        randombleh = random.randrange(0, no_time_sayings, 1)
        await message.channel.send(time_sayings[randombleh])
        await message.channel.send("The time is " + tame.strftime("%H:%M"))
    if message.content.startswith("Time riyadh") or message.content.startswith("time riyadh"):
        time = pytz.timezone('Asia/Riyadh')
        taime = datetime.now(time)
        randombleh = random.randrange(0, no_time_sayings, 1)
        await message.channel.send(time_sayings[randombleh])
        await message.channel.send("The time is " + taime.strftime("%H:%M"))
    

    #Dream calculator
    if message.content.endswith("="):
        alpha = wolframalpha.Client(app_id)
        calc = message.content
        res = alpha.query(calc)
        answer = next(res.results).text
        await message.channel.send("Yo yo yo, your answer is " + answer)

    #redditMemes
    if message.content.startswith("meme"):
                    messssaage = message.content
                    random_sub = messssaage[5:]
                    if (not random_sub):
                        random_subreddit = random.choice(reddit_subreddits)
                        random_sub = random_subreddit 
                    posts = reddit.subreddit(random_sub)
                    hot = posts.rising(limit=25)
                    all_posts = []
                    for submission in hot:
                        all_posts.append(submission)
                    random_post = random.choice(all_posts)
                    name = random_post.title
                    url = random_post.url
                    permalink = "https://www.reddit.com/" + random_post.permalink
                    subreddit_info = "This post is from r/" + random_sub
                    em = discord.Embed(title="")
                    em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    em.add_field(name="-", value="[" + name + "](" + permalink + ")")
                    em.set_image(url=url)
                    em.set_footer(text=subreddit_info)
                    await message.channel.send(embed=em)

    #redditAdd
    if message.content.startswith("https://www.reddit.com"):
        reddit_post = message.content
        submission = reddit.submission(url=reddit_post)
        name = submission.title
        url = submission.url
        permalink = "https://reddit.com/" + submission.permalink
        em = discord.Embed(title="")
        em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        em.add_field(name="-", value="[" + name + "](" + permalink + ")")
        em.set_image(url=url)
        await message.delete()
        await message.channel.send(embed=em)

    if message.content.startswith("karma ") or message.content.endswith("Karma "):
        txt = message.content[6:]
        redditor = reddit.redditor(txt)
        await message.channel.send(txt + " has " + str(redditor.link_karma) + " karma.")
    #frickoff
    if message.content.startswith("Fuck off") or message.content.startswith("fuck off"):
        picture = 'https://i.redd.it/ptm4c3jqzri61.png'
        await message.channel.send(picture)

    #understandable
    if message.content.startswith("understandable") or message.content.startswith("Understandable"):
        picture = 'https://pbs.twimg.com/media/Ewis5bzUcAA_tqn?format=png&name=small'
        await message.channel.send(picture)

    #okay.
    # if message.content.startswith("Okay.") or message.content.startswith("okay."):
    #     picture = 'https://tenor.com/view/okay-smile-ok-happy-gif-14150032'
    #     await message.channel.send(picture)

    #Get Some Help
    if message.content.startswith('Get some help') or message.content.startswith('get some help'):
        gif = 'https://tenor.com/view/stop-it-get-some-help-gif-15058124'
        await message.channel.send(gif)

    #masterYoda!?!?!?!?!?
    if message.content.startswith("Master yoda") or message.content.startswith("master yoda"):
        randombleh = random.randrange(0, no_yoda, 1)
        await message.channel.send(yoda[randombleh])
        
    #captain sparrow!
    if message.content.startswith("Captain Sparrow") or message.content.startswith("Captain sparrow") or message.content.startswith("captain sparrow"):
        randombleh = random.randrange(0, no_sparrow, 1)
        await message.channel.send(sparrow[randombleh])

    #cRoOkEd
    if message.content.startswith("crooked ") or message.content.startswith("Crooked "):
        text = message.content[8:]
        crooked_message = []
        chars = list(text)
        switch = 1

        for char in chars:
            if switch == 0:
                crooked_message.append(char.lower())
                switch = 1
            elif switch == 1:
                crooked_message.append(char.upper())
                switch = 0


        output = ''.join(crooked_message)
        await message.channel.send(output)

    #dictionary
    if message.content.startswith("Meaning ") or message.content.startswith("meaning "):
      word = message.content[8:]
      await message.channel.send(dictionary.meaning(word))
    if message.content.startswith("Synonyms ") or message.content.startswith("synonyms "):
      word = message.content[9:]
      await message.channel.send(dictionary.synonyms(word))
    if message.content.startswith("Antonyms ") or message.content.startswith("antonyms "):
      word = message.content[9:]
      await message.channel.send(dictionary.antonyms(word))
        
 
    #Spacing text
    if message.content.startswith("spaced "):
      text = message.content[7: ]
      arr_text = list(text)
      spaced_text = ""
      for letter in arr_text:
        spaced_text = spaced_text + letter + " "
      await message.channel.send(spaced_text)  
      await message.delete()

    #wordle
    if message.content.startswith("wordle "):
        text = message.content[7: ]
        boxes = text.split(" ")
        output = []
        for box in boxes:
            if box == "b" or box == "B": output.append(":black_large_square:")
            if box == "y" or box == "Y": output.append(":yellow_square:")
            if box == "g" or box == "G": output.append(":green_square:")

        line1 = [output[0], output[1], output[2], output[3], output[4]]
        line2 = [output[5], output[6], output[7], output[8], output[9]]
        line3 = [output[10], output[11], output[12], output[13], output[14]]
        line4 = [output[15], output[16], output[17], output[18], output[19]]
        line5 = [output[20], output[21], output[22], output[23], output[24]]
        line6 = [output[25], output[26], output[27], output[28], output[29]]

        await message.channel.send(line1[0] + line1[1] + line1[2] + line1[3] + line1[4])
        await message.channel.send(line2[0] + line2[1] + line2[2] + line2[3] + line2[4])
        await message.channel.send(line3[0] + line3[1] + line3[2] + line3[3] + line3[4])
        await message.channel.send(line4[0] + line4[1] + line4[2] + line4[3] + line4[4])
        await message.channel.send(line5[0] + line5[1] + line5[2] + line5[3] + line5[4])
        await message.channel.send(line6[0] + line6[1] + line6[2] + line6[3] + line6[4])
        await message.delete()


#Token for bot    
client.run('Nzk4OTY0ODc3NzYyODg3NzUy.X_8sBg.o86mF7Ac7XmBWHJXAgLJVwn4sEg')
