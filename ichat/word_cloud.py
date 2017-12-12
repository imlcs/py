#!/usr/bin/env python
# coding=utf-8
# coding:utf-8
import itchat
import re
import os

itchat.auto_login(enableCmdQR=2)
friends = itchat.get_friends(update=True)[0:]
tList = []
for friend in friends:
    signature = friend.Signature.replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)

# 拼接字符串
text = "".join(tList)

# jieba分词
import jieba
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

d = './'
alice_coloring = np.array(Image.open(os.path.join(d, "wechat_cloud.png")))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,max_font_size=40, random_state=42,font_path='叶立群几何体.ttf').generate(wl_space_split)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.figure()
plt.axis("off")
plt.show()

# 保存图片 并发送到手机
my_wordcloud.to_file(os.path.join(d, "wechat_cloud.png"))
#itchat.send_image("wechat_cloud.png", 'filehelper')
