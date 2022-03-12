import asyncio
#coding:utf8
import re
from pyppeteer import launch
from pyppeteer_stealth import stealth
import itchat

rule = r'title":{"runs":\[{"text":"(.*?)"}]'

async def main():
    itchat.auto_login(enableCmdQR=False,hotReload=True)
    to_name = itchat.search_friends(name="理文")

    browser = await launch(headless=True, userDataDir="/Users/iwan/Library/Application Support/Google/Chrome/Default", args=['--disable-infobars'])
    page = await browser.newPage()
    await stealth(page)  # <-- Here
    await page.goto('https://www.youtube.com/feed/subscriptions')
    content= await page.content()

    i=1
    for title in re.findall(rule, content):
        if(title == "今天"):
            continue
        if(title == "昨天"):
            break
        print(f"【{i}】{title}")
        itchat.send(f"【{i}】{title}",toUserName=to_name[0]['UserName'])
        i+=1
    
    #await browser.close()

asyncio.get_event_loop().run_until_complete(main())