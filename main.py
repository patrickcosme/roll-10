import discord
import random
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print('Bot Online Olá Mundo')
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):

    sucess = 0

    msgSplited = message.content.split('-')

    numberDices = int(msgSplited[0])

    try:
        difficulty = int(msgSplited[1])
    except:
        difficulty = 6

    res = [random.randint(1, 10) for x in range(numberDices)]
    res.sort(reverse=True)

    for x in res:
        if x >= difficulty:
            sucess = sucess + 1
        elif x == 1:
            sucess = sucess - 1

    print("[{}]  Sucessos: {}".format(res, sucess))
    print(sucess)

    await message.channel.send("{}  Sucessos: {}".format(res, sucess))


client.run('NzI4NjY3ODIxMzE5NjUxMzk5.Xv9wRg.lxD8yrqJP8y82Jx0qCZCl85tnB0')



