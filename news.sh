#!/bin/sh

# 记录一下开始时间
echo `date` >> log &&
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 ~/work/python/youtube_news/youtube.py
# 运行完成
echo 'finish' >> log
