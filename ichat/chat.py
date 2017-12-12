#!/usr/bin/env python
# coding=utf-8
import itchat
#itchat.login()
itchat.auto_login(enableCmdQR=2)
#itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
def get_friend():
    for friend in friends[1:]:
        print(friend.NickName + ": "),
        if friend.City:
            print("\033[0;32m %s\033[0m" % friend.City)
        else:
            print("\033[0;32m地址暂无！\033[0m")
        if friend.Signature:
            print(friend.Signature)
        print("\n")
get_friend()
