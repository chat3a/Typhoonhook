from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.dgpa.gov.tw/typh/daily/nds.html")

url.encoding = "UTF-8"

timer = 5

soup = BeautifulSoup(url.text, "html.parser")
status = soup.find("h2")

update_time = soup.find("h4")

if status != None and update_time != None:
    title_ = print(soup.title.string)
    for i in status:
        if i != None:
            global status_output
            status_output = print(i.text)
    update_time_output = print(update_time.text.strip()[5:30])
else:
    print("! There's nothing.")

hook = DiscordWebhook(url = "https://discord.com/api/webhooks/1301429892847632455/Wfx7Bwuk5oK1oBZdF3bcgHU2vqdM-t04yxl-ec0gmla42DsXUcMoPh9CJ4mZErspf4jj",
                      id = "1062296350722637855")


embed = DiscordEmbed(title=":cyclone: 颱風最新停班課資訊",
                      description= f"# {i.text}",
                      colour=0xffffff,
                      )

embed.add_embed_field(name="",
                value="[資料來源](https://www.dgpa.gov.tw/typh/daily/nds.html)",
                inline=False)

embed.set_footer(text=f"Typhoonhook | ✅上次更新: {update_time.text.strip()[6:30]}",
                 icon_url="https://cdn.discordapp.com/attachments/1068462587618021416/1417136087406612701/alerta.gif?ex=68c96254&is=68c810d4&hm=eb7e241e58161c42e8454f1000356edb7c361471b6b0da74c7dadee5cb0b3453&")



hook.add_embed(embed)


hook.execute()
print("> 訊息已發送!")

a = 0
times = 0
while True:

    timer -= 1
    if timer < 0:
        timer = 5
        times += 1
    a += 1
    hook.edit()
    hook.content = f" 🕝 距離下次資料更新還剩 `{timer}` 秒 [{times}]"
    print(f"> 資料更新! [{a}]")
    time.sleep(1)



