
# -*- coding: utf-8 -*-
#from linepy import *
#from thrift import*
from Linephu.linepy import *
from datetime import datetime
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
botStart = time.time()
cl = LINE()
cl.log(cl.authToken)
k1 = LINE(cl.authToken)
k2 = LINE(cl.authToken)
k3 = LINE(cl.authToken)
k4 = LINE(cl.authToken)
k5 = LINE(cl.authToken)
k6 = LINE(cl.authToken)
k7 = LINE(cl.authToken)
k8 = LINE(cl.authToken)
k9 = LINE(cl.authToken)
k10 = LINE(cl.authToken)
k11 = LINE(cl.authToken)
k12 = LINE(cl.authToken)
k13 = LINE(cl.authToken)
k14 = LINE(cl.authToken)
k15 = LINE(cl.authToken)
k16 = LINE(cl.authToken)
k17 = LINE(cl.authToken)
k18 = LINE(cl.authToken)
k19 = LINE(cl.authToken)
k20 = LINE(cl.authToken)

clMID = cl.profile.mid

bots = [cl, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20]
Rfu = [cl]

oepoll = OEPoll(cl)

banOpen = codecs.open("ban.json","r","utf-8")
groupOpen = codecs.open("group.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
ban = json.load(banOpen)
gp = json.load(groupOpen)
settings = json.load(settingsOpen)
read = json.load(readOpen)
print("機器壹登入成功")
print("[ 登錄系統 ]成功(  -᷄ω-᷅ )")
print("登入所花時間為"+str(format_timespan(time.time())))
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def Kick(n, to, mid):
    while 1:
        bots[n].kickoutFromGroup(to, mid)
        break
def backupData():
    try:
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = gp
        f = codecs.open('group.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def helpmessage():
    helpMessage = """🔥  skp 歡迎機   🔥 
🔥 add_wc:(歡迎訊息)-新增群組歡迎訊息
🔥 renew_wc:(歡迎訊息)-更新群組歡迎訊息
🔥 del_wc-刪除群組歡迎訊息
🔥 sn 設立以讀點
🔥 sf 關閉已讀點
🔥 sr 更新已讀點
🔥 r 查看當前已讀"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""🔥  skp 歡迎機   🔥
🔥 add_wc:(歡迎訊息)-新增群組歡迎訊息
🔥 renew_wc:(歡迎訊息)-更新群組歡迎訊息
🔥 del_wc-刪除群組歡迎訊息
🔥 wc-歡迎詞初始化
🔥 sn 設立以讀點
🔥 sf 關閉已讀點
🔥 sr 更新已讀點
🔥 r 查看當前已讀"""
    return helpMessageTag
def helpn():
    helpN = """🔥  sk-p 歡迎機   🔥
🔥 Gc-查詢自己剩餘票數
🔥 喵-蘿莉共鳴
🔥 Speed-速度
🔥 GM-查看本群管理者"""
    return helpN

wait = {
    "ban" : False,
    "unban" : False,
    "add" : False,
    "del" : False
}

if clMID not in ban["owners"]:
    ban["owners"].append(clMID)

def lineBot(op):
    try:
        if op.type == 11:
            if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                pass
            else:
                gs = cl.getGroup(op.param1)
                if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                    pass
                else:
                    bot = random.choice([cl])
                    gs.preventJoinByTicket = True
                    bot.updateGroup(gs)
                    bot.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            cl.findAndAddContactsByMid(op.param1) #自動加好友
            cl.sendMessage(op.param1, "你好 {} 謝謝你加我為好友 ε٩(๑> ₃ <)۶з \n此機器為歡迎機器人 \n有興趣可以私以下友資購買".format(str(cl.getContact(op.param1).displayName)))
            cl.sendMessage(op.param1, None, contentMetadata={'mid': 'u56d30ff9392a9dddbe7fcdec518d1894'}, contentType=13)
        if op.type ==19:
            a = 0
            if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                if op.param3 in clMID:
                    while (a<3):
                        try:
                            bot = random.choice([cl])
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot.updateGroup(G)
                            Ticket = bot.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            a+=1
                            pass
                        else:
                            break
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
        if op.type == 60:
            if op.param2 in ban['blacklist']:
                cl.sendMessage(op.param1, "[警告]\n此人位於黑名單中! ! !")
            else:
                if op.param2 not in ban['bot']:
                    if op.param1 not in ban['wel']:
                        try:
                            arrData = ""
                            text = "%s " %('你好~~')
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention + '!!歡迎加入群組!!!!'
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)   
                    else:
                        cl.sendMessage(op.param1, ban['wel'][op.param1])
        if op.type == 0:
            return
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                if op.param2 in ban["owners"]:
                    cl.acceptGroupInvitation(op.param1)
                    botJoin(op.param1)
                    gMembMids = [contact.mid for contact in G.members]
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl])
                        bot.kickoutFromGroup(op.param1,[jj])
                elif op.param2 in ban["user"]:
                    ban["user"][op.param2] =ban["user"][op.param2] -1
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"你還擁有{}張票".format(str(ban["user"][op.param2])))
                    botJoin(op.param1)
                    if ban["user"][op.param2] == 0:
                        del ban["user"][op.param2]
                    G = cl.getGroup(op.param1)
                    gp["s"][G.id] =[]
                    gp["s"][G.id].append(op.param2)
                    backupData()
                    gMembMids = [contact.mid for contact in G.members]
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl])
                        bot.kickoutFromGroup(op.param1,[jj])
                else:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"你的票不夠啦ヾ(;ﾟ;Д;ﾟ;)ﾉﾞ")
                    cl.leaveGroup(op.param1)
            elif op.param2 in ban["admin"] or op.param2 in Bots or op.param2 in ban["owners"]:
                pass
            else:
                bot = random.choice([cl])
                G=bot.getGroup(op.param1)
                matched_list = []
                for tag in ban["blacklist"]:
                    if tag in op.param3:
                        matched_list.append(str(tag))
                if matched_list == []:
                    return
                for mid in matched_list:
                    bot.cancelGroupInvitation(op.param1,[mid])
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if clMID in op.param3:
                cl.leaveRoom(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in sender:
                if text.lower() == 'gc':
                    if sender in ban["user"]:
                        cl.sendMessage(to,"你還擁有{}張票".format(str(ban["user"][sender])))
                    else:
                        cl.sendMessage(to,"沒有票惹(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)歡迎購買邀請票券")
                elif text.lower() =='test':
                    cl.sendMessage(to,"運行中......")
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(to, "計算中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'gm':
                    G = cl.getGroup(to)
                    if G.id not in gp["s"] or gp["s"][G.id]==[]:
                        cl.sendMessage(to,"無群管!")
                    else:
                        mc = "╔══[ Group Manager ]"
                        for mi_d in gp["s"][G.id]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'help':
                    if sender in ban["admin"]:
                        helpMessage = helpmessage()
                        cl.sendMessage(to, str(helpMessage))
                    elif sender in ban["owners"]:
                        helpMessageTag = helpmessagetag()
                        cl.sendMessage(to, str(helpMessageTag))
                    else:
                        helpN = helpn()
                        cl.sendMessage(to, str(helpN))
            if sender in ban["admin"] or sender in ban["owners"]:
                if text.lower() =='歡迎退':
                    cl.leaveGroup(msg.to)
                elif text.lower() == 'join':
                    botJoin(msg.to)
                elif text.lower() == 'adminlist':
                    if ban["admin"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ Admin List ]"
                        for mi_d in ban["admin"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == '主控權限':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ Admin List ]"
                        for mi_d in ban["owners"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "[ Black List ]"
                        for mi_d in ban["blacklist"]:
                            if ban["blacklist"][mi_d] == True:
                                mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)
                            else:
                            	mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)+"[baned]"
                        cl.sendMessage(msg.to,mc + "\n[ Finish ]")
                elif text.lower().startswith("tk "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in ban["owners"]:
                            pass
                        else:
                            try:
                                kicker=random.choice([cl, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20])
                                kicker.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif text.lower() == '取消邀請':
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        cl.sendMessage(to, "平均0.4秒取消一個人ヽ(✿ﾟ▽ﾟ)ノ")
                        if X.invitee is not None:
                            gInviMids = (contact.mid for contact in X.invitee)
                            ginfo = cl.getGroup(msg.to)
                            sinvitee = str(len(ginfo.invitee))
                            start = time.time()
                            for cancelmod in gInviMids:
                                bot = random.choice([cl, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20])
                                time.sleep(2.5)
                                bot.cancelGroupInvitation(msg.to, [cancelmod])
                            elapsed_time = time.time() - start
                            cl.sendMessage(to, "已取消完成\n取消時間: %s秒" %
                                           (elapsed_time))
                            cl.sendMessage(to, "取消人數:" + sinvitee)
                            time.sleep(3)
                            cl.sendMessage(to, "バイバイ")
                            cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == '標記':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s = 0
                        b = []
                        for i in group.members[a*20: (a+1)*20]:
                            b.append({"S": str(s), "E": str(s+6), "M": i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={
                                       u'MENTION': json.dumps({'MENTIONEES': b})}, contentType=0)
                    cl.sendMessage(to, "總共 {} 人".format(str(len(nama))))
                elif msg.text.lower().startswith("add_wc"):
                    list_ = msg.text.split(":")
                    if to not in ban['wel']:
                        try:
                            ban['wel'][to] = list_[1]
                            with open('ban.json', 'w') as fp:
                                json.dump(ban, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功設置群組歡迎訊息\n歡迎訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[ERROR]\n設置群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[ERROR]\n群組歡迎訊息已存在!!!")
                elif msg.text.lower().startswith("renew_wc"):
                    list_ = msg.text.split(":")
                    if to in ban['wel']:
                        try:
                            del ban['wel'][to]
                            ban['wel'][to] = list_[1]
                            with open('ban.json', 'w') as fp:
                                json.dump(ban, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功更新群組歡迎訊息\n歡迎訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[ERROR]\n更新群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[ERROR]\n你正在更新不存在的歡迎訊息!!!")
                elif text.lower() == ("del_wc"):
                    if to in ban['wel']:
                        try:
                            del ban['wel'][to]
                            with open('ban.json', 'w') as fp:
                                json.dump(ban, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n成功刪除群組歡迎訊息")
                        except:
                            cl.sendMessage(to, "[ERROR]\n刪除群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[ERROR]\n你正在刪除不存在的歡迎訊息!!!")
                elif text.lower() == 'wc':
                    if to in ban['wel']:
                        cl.sendMessage(to, ban['wel'][to])
                    else:
                        cl.sendMessage(to, "[提示]\n使用預設群組歡迎訊息中!!!")
                elif text.lower() == 'sn':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"已讀點已開始")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "設定已讀點:\n" + readTime)
                elif text.lower() == 'sf':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        cl.sendMessage(msg.to,"已讀點已經關閉")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                                pass
                        cl.sendMessage(msg.to, "刪除已讀點:\n" + readTime)
                elif text.lower() == 'sr':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        cl.sendMessage(msg.to, "重置已讀點:\n" + readTime)
                    else:
                        cl.sendMessage(msg.to, "已讀點未設定")
                elif text.lower() == 'r':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ 已讀者 ]:\n沒有")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ 已讀者 ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ 已讀時間 ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        cl.sendMessage(receiver,"已讀點未設定")
                elif msg.text.lower().startswith("gbc:"):
                    bctxt = text.replace("gbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,"[群組廣播]\n"+bctxt)
                        cl.sendContact(manusia, "u56d30ff9392a9dddbe7fcdec518d1894")                     
            if sender in ban["owners"]:
                if text.lower().startswith("gadd "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        gp["s"][G.id] =[]
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to,"OK")
                if text.lower().startswith("gdel "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        cl.sendMessage(to, "There is no group manager！")
                    else:
                        for x in key["MENTIONEES"]:
                            try:
                                gp["s"][G.id].remove(x["M"])
                            except:
                                cl.sendMessage(to,"Not in GM.")
                        cl.sendMessage(to,"OK")
                elif "轟炸" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("轟炸","")
                            gs = cl.getGroup(to)
                            start = time.time()
                            cl.sendMessage(to, "踢一些人掉")
#                            cl.sendMessage(to, "🍌见识见识马甲冷童的机器🍌")
#                            cl.sendMessage(to, "✒作者✒")
#                            cl.sendMessage(to, "🔱ㄊㄌ🔱")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if not target in Rfu:
                                        pass
                                    else:
                                        try:
                                            cl.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif text.lower().startswith("gjoin "):
                    try:
                        gid = cl.getGroupIdsJoined()[int(text[6:])-1]
                    except:
                        cl.sendMessage(to,"not in range.")
                        return
                    try:
                        G = cl.getGroupWithoutMembers(gid)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                        cl.sendMessage(to,"https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(gid))))
                    except:
                        cl.sendMessage(to,"not found")
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower().startswith("gc "):
                    x = text.split(" ")
                    if x[1] in ban["user"]:
                        cl.sendMessage(to,"你還擁有{}張票".format(str(ban["user"][x[1]])))
                    else:
                        cl.sendMessage(to,"沒有票惹(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)歡迎購買邀請票券")
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動中...")
                    cl.sendMessage(to, "重啟成功")
                    restartBot()
                elif text.lower() == 'clear ban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower().startswith("tk "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in ban["owners"]:
                            pass
                        else:
                            try:
                                kicker=random.choice([cl])
                                kicker.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif text.lower() == 'kg':
                    gid = cl.getGroupIdsJoined() 
                    for i in gid:
                        group=cl.getGroup(i)
                        gMembMids = [contact.mid for contact in group.members] 
                        ban_list = [] 
                        for tag in ban["blacklist"]: 
                            ban_list += filter(lambda str: str == tag, gMembMids) 
                        if ban_list == []: 
                            cl.sendMessage(i, "沒有黑名單") 
                        else: 
                            for jj in ban_list: 
                                bot = random.choice([cl]) 
                                bot.kickoutFromGroup(i, [jj]) 
                            cl.sendMessage(i, "掃黑結束") 
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in ban["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有黑名單")
                        else:
                            bot = random.choice([cl])
                            for jj in matched_list:
                                bot.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單以踢除")
                elif text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["admin"]:
                        ban["admin"].append(str(inkey))
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        cl.sendMessage(to,"already")
                elif text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["admin"]:
                        ban["admin"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                    else:
                    	cl.sendMessage(to,"user is not in admin")
                elif text.lower().startswith("新增主控權 "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["owners"]:
                        ban["owners"].append(str(inkey))
                        cl.sendMessage(to, "已獲得主權限！")
                    else:
                        cl.sendMessage(to,"already")
                elif text.lower().startswith("取消主控權 "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["owners"]:
                        ban["owners"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                    else:
                    	cl.sendMessage(to,"user is not in admin")
                elif text.lower() == 'add':
                    wait["add"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'del':
                    wait["del"] = True
                    cl.sendMessage(to,"Please send a Contact")
                elif text.lower() == '新增主控權':
                    wait["新增主控權"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == '取消主控權':
                    wait["取消主控權"] = True
                    cl.sendMessage(to,"Please send a Contact")
                elif text.lower().startswith("a "):
                    x = text.split(" ")
                    ban["admin"].append(x[1])
                    if len(x) ==2:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = 1
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=1
                            cl.sendMessage(to,"ok")
                    elif len(x) ==3:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = int(x[2])
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=int(x[2])
                            cl.sendMessage(to,"ok")
                    backupData()
                elif text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith("ban:"):
                    txt = text.replace("Ban:","")
                    try:
                        ban["blacklist"][txt] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    except:
                        cl.sendMessage(msg.to,"添加失敗 !" +txt)
                elif text.lower().startswith("unban:"):
                    txt = text.replace("Unban:","")
                    try:
                        del ban["blacklist"][txt]
                        cl.sendMessage(msg.to,"已刪除黑單!")
                    except:
                        cl.sendMessage(msg.to,"刪除失敗 !" +txt)
                elif text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] =False
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'ban':
                    wait["ban"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'unban':
                    wait["unban"] = True
                    cl.sendMessage(to,"Please send a Contact")                              
        if op.type == 25 or op.type ==26:
            msg = op.message
            if msg.contentType == 13:
                if wait["ban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["ban"] = False
                        else:
                           ban["blacklist"][msg.contentMetadata["mid"]] = True
                           wait["ban"] = False
                           cl.sendMessage(msg.to,"成功新增黑單")
                elif wait["unban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["unban"] = False
                        else:
                           del ban["blacklist"][msg.contentMetadata["mid"]]
                           wait["unban"] = False
                           cl.sendMessage(msg.to,"成功移除黑單")
                elif wait["add"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["add"] = False
                        else:
                           ban["admin"].append(str(msg.contentMetadata["mid"]))
                           wait["add"] = False
                           cl.sendMessage(msg.to,"成功新增權限")
                elif wait["del"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["del"] = False
                        else:
                           ban["admin"].remove(str(msg.contentMetadata["mid"]))
                           wait["del"] = False
                           cl.sendMessage(msg.to,"成功移除權限")
                elif wait["新增主控權"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["owners"]:
                           cl.sendmessage(to,"already")
                           wait["新增主控權"] = False
                        else:
                           ban["owners"].append(str(msg.contentMetadata["mid"]))
                           wait["add"] = False
                           cl.sendMessage(msg.to,"成功新增權限")
                elif wait["取消主控權"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["owners"]:
                           cl.sendmessage(to,"使用者不在權限中")
                           wait["取消主控權"] = False
                        else:
                           ban["owners"].remove(str(msg.contentMetadata["mid"]))
                           wait["取消主控權"] = False
                           cl.sendMessage(to,"成功移除權限")
#                else:
#                    cl.sendMessage(msg.to,str(msg.contentMetadata["mid"]))
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                        cl.log()
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    sendMessageWithMention(to, contact.mid)
                                    cl.sendMessage(to, "安安你好,我是防翻機器人,有事請找主人")
                                    time.sleep(0.5)
                                    cl.sendContact(op.param1, "ub809d1621e65e5defd74e9e61b1b51b4")
                                break
        if op.type == 55:
            print ("[ 55 ] 通知讀取消息")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
