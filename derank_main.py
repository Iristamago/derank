# -*- coding:utf-8 -*-
'''
Created on 2017-11-09

@author: YilisiC
'''

import requests
import subprocess
import webbrowser
import os
from bs4 import BeautifulSoup

def GetLobbyUrl():
    fafk = open('./configs/afk.conf', 'r')
    afkconf = fafk.readlines()
    fafk.close()
    for i in afkconf:
        line = i.strip('\n')
        afk.append(line)
    frank = open('./configs/rank_accept.conf', 'r')
    rankconf = frank.readlines()
    frank.close()
    for j in rankconf:
        line = j.strip('\n')
        rank_accept.append(line)
        
    time_accepted = ['seconds', 'just', 'now', 'just now', 'minute']
    
    res = requests.get("https://derank.me")
#     res.encoding = "utf-8"
    
    soup = BeautifulSoup(res.text, "html.parser")
#     print(soup.select('.cta'))  #links are inside class
    
    count = 0
    for match in soup.select('.match'):
        if len(match.select('.conditions')) > 0:
            rank = match.select('p')[0].text
        if len(match.select('.time-posted')) > 0:
            int_time = match.select('p')[1].text.split(" ago")[0].split(" ")[-2]
            time = match.select('p')[1].text.split(" ago")[0].split(" ")[-1]
            past_time = int_time + ' ' + time + ' ago'
        if rank.split(', ')[-1] in afk and time in time_accepted and rank.split(', ')[0] in rank_accept:
            if len(match.select('.cta')) > 0:
                link = match.select('a')[0]['href']
                
#                 print("Rank: %s"%rank)
#                 print("Link: %s"%link)
            count = count + 1    
            yield count, rank, past_time, link

def Browser(lobby):
    webbrowser.open(lobby, new=1, autoraise=True)
    print('Wait a moment. You are joining the lobby.\n')
    
def settings():
    if not os.path.exists('./configs'):
        os.makedirs('./configs')
    if not os.path.exists('./configs/afk.conf'): 
        while True:
            print('Search Settings (You can change settings at configs/afk.conf): \n')
            cafk = input('1 - AFK Only\n2 - Win 3 rounds\n3 - AFK Only & Win 3 rounds\n4 - No AFK\n\nWhich do you prefer? (Your choice): ')
            if cafk == '1':
                file_afk = open('./configs/afk.conf', 'w')
                file_afk.write('AFK only')
                file_afk.close()
                break
            elif cafk == '2':
                file_afk = open('./configs/afk.conf', 'w')
                file_afk.write('Win 3 rounds')
                file_afk.close()
                break
            elif cafk == '3':
                file_afk = open('./configs/afk.conf', 'w')
                file_afk.write('AFK only\nWin 3 rounds')
                file_afk.close()
                break
            elif cafk == '4':
                file_afk = open('./configs/afk.conf', 'w')
                file_afk.write('No AFK')
                file_afk.close()
                break
            else:
                print('Please input number 1-4 only.') 
        subprocess.call("cls",shell=True)
            
    if not os.path.exists('./configs/rank_accept.conf'):
        while True:
            print('Search Settings (You can change settings at configs/rank_accept.conf): \n')
            crank = input('Select the lobby rank:\n\n1 - Silvers only\n2 - Gold Novas and below\n3 - Master Guardians and below\n4 - Any rank\n5 - All rank\n\nWhich do you prefer? (Your choice): ')
            if crank == '1':
                file_rank = open('./configs/rank_accept.conf', 'w')
                file_rank.write('Silvers only')
                file_rank.close()
                break
            elif crank == '2':
                file_rank = open('./configs/rank_accept.conf', 'w')
                file_rank.write('Silvers only\nGold Novas and below')
                file_rank.close()
                break
            elif crank == '3':
                file_rank = open('./configs/rank_accept.conf', 'w')
                file_rank.write('Silvers only\nGold Novas and below\nMaster Guardians and below')
                file_rank.close()
                break
            elif crank == '4':
                file_rank = open('./configs/rank_accept.conf', 'w')
                file_rank.write('Any rank')
                file_rank.close()
                break
            elif crank == '5':
                file_rank = open('./configs/rank_accept.conf', 'w')
                file_rank.write('Silvers only\nGold Novas and below\nMaster Guardians and below\nAny rank')
                file_rank.close()
                break
            else:
                print('Please input number 1-5 only.')
        subprocess.call("cls",shell=True)
    
def main():
    print('Searching Derank Lobby...(Close the window if you want to exit)\n')
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] #There are 20 links the whole page
    if len(list(GetLobbyUrl())) == 0:
        print('\nNo lobby needs your demand. Please try later.\n')
    else:
        for count, rank, past_time, lobby in GetLobbyUrl():
            print("The %s Lobby:\n\nLobby Rank: %s\nLobby Time: %s\nLobby Link: %s\n"%(str(count) + endings[count - 1], rank, past_time, lobby))
            m = input(r"Do you want to join the lobby? (Y=Yes/n=no/r=research): ")
            if m == 'n':
                print('\n')
                continue
            elif m == 'r':
                print('\n')
                break
            else:
                Browser(lobby)
    subprocess.call("cls",shell=True)

if __name__=="__main__":
    settings()
    modify_ = input('Do you want to modify configs? (y/N): ')
    subprocess.call("cls",shell=True)
    if modify_ == 'y' or modify_ == 'Y':
        os.remove('./configs/afk.conf')
        os.remove('./configs/rank_accept.conf')
        settings()
    while True:
        afk = []
        rank_accept = []
        try:
            main()
        except:
            break