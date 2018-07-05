#  -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pypinyin import pinyin, lazy_pinyin
from flask import Flask
from flask import request
from flask import render_template
import hashlib
import commands
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/editpass", methods=["POST", "GET"])
def editpasss():
    Username = request.form['Username']
    oldPassword = request.form['oldPassword']
    newPassword = request.form['newPassword']
    renewPassword = request.form['renewPassword']

    if newPassword != renewPassword:
        error = u"两次输入的新密码不一样"
        return render_template('index.html', error=error)
    
    # 获取用户列表
    userList = commands.getoutput("cut -d' ' -f1 ./modify_ldap/jishu.txt").split("\n")
    users = []
    for user in userList:
        un_user = user.decode('utf-8').encode('unicode_escape')
        pinyin_username = (''.join(lazy_pinyin(un_user.decode('unicode-escape'))))
        users.append(pinyin_username)

    if Username not in users:
        error = u"用户名或密码错误"
        return render_template('index.html', error=error)
    else:
        command = "grep " + Username + " ./modify_ldap/jishu.txt | cut -d' ' -f3"
        nowPassowrd = commands.getoutput(command)
        m = hashlib.md5()
        m.update(oldPassword)
        md5Password = m.hexdigest()
        if md5Password != nowPassowrd:
            error = u"用户名或密码错误"
            return render_template('index.html', error=error)
    # 生成SHA字符串
    crepass = "python modify_ldap/create_shapass.py " + renewPassword+ " | grep SSHA"
    newSHAPassword = commands.getoutput(crepass)
    # 生成修改用户密码的模板
    createFile = "sed -e 's#{{username}}#" + Username + "#g' -e 's#{{password}}#" + newSHAPassword + "#g' ./modify_ldap/modifypass_template.ldif >./modify_ldap/modifypass.ldif"
    os.system(createFile)
    # 生成用户新密码的加密字符串
    n = hashlib.md5()
    n.update(renewPassword)
    newMD5Password = n.hexdigest()
    editUserFile = "sed -i '/" + Username + "/s#" + nowPassowrd  + "#" + newMD5Password  + "#g' ./modify_ldap/jishu.txt"

    #修改ldap的密码
    os.system('dos2unix ./modify_ldap/modifypass.ldif')
    res = commands.getstatusoutput("python ./modify_ldap/modify_passwd.py")[0]

    if res == 0:
        #ldap密码修改成功后修改用户文件中的加密密码字符串
        os.system(editUserFile)
        return render_template('index.html',error="修改成功")
    else:
        return render_template('index.html',error="修改失败")

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', debug=True, port=888)
