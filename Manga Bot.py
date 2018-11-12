from selenium import webdriver
import time
import discord

client = discord.Client()
browser = webdriver.Chrome()

@client.event
async def on_ready():
    print("Manga Bot is Ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0:7] == '!manga ':
        url = message.content[7:]
        await client.send_message(message.channel, 'Printing your manga now senpai! >_<\nPrinting from ' + url)

        browser.get(url)

        time.sleep(10)

        source = browser.page_source

        html_index = source.find('<img onerror="onErrorImg(this)" onload="onLoadImg(this);" src="')
        short_source = source[html_index:]

        if html_index != -1:
            html_index = 0

        while html_index != -1:
            link_index = html_index+len('<img onerror="onErrorImg(this)" onload="onLoadImg(this);" src="')
            await client.send_message(message.channel, short_source[link_index:short_source.find('"',link_index)])

            html_index = short_source.find('<img onerror="onErrorImg(this)" onload="onLoadImg(this);" src="', link_index)


client.run('Token')