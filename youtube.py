#coding:utf8
import asyncio
import re
from pyppeteer import launch
from pyppeteer_stealth import stealth
import itchat
import time

import urllib.parse

rule = r'title":{"runs":\[{"text":"(.*?)"}]'

async def main():
    itchat.auto_login(enableCmdQR=False,hotReload=True)
    to_name = itchat.search_friends(name="理文")

    browser = await launch(headless=False, userDataDir="/Users/iwan/Library/Application Support/Google/Chrome/Default", args=['--disable-infobars'])
    page = await browser.newPage()
    await stealth(page)  # <-- Here
    await page.goto('https://www.youtube.com/feed/subscriptions')
    content= urllib.parse.unquote(await page.content())

    i=1
    info= f"新闻播报 {time.strftime('%Y年%m月%d日%H时')}\n"
    for title in re.findall(rule, content):
        if(title == "今天"):
            continue
        if(title == "昨天"):
            break
        info+= f"{i}-{title}\n"
        i+=1
    print(info)
    itchat.send(info,toUserName=to_name[0]['UserName'])
    
    #await browser.close()

asyncio.get_event_loop().run_until_complete(main())