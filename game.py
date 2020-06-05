import json

def set_char(name):
    character = {
        'name':name,
        'pokemon':'꼬부기',
        "items": ["오랭열매","하이퍼볼","치료제"],
        "skill": ["물대포","하이드로펌프","몸통박치기"]
    }
    with open('static/save.txt', 'w', encoding='utf-8') as f: 
        json.dump(character, f,ensure_ascii = False, indent=4)

    #print("{0}님 반갑습니다,{1}와 모험을 떠납니다".format(character["name"],character["pokemon"]))
    return character

def save_game(filename,char):
    f = open(filename,"w",encoding="uft-8")
    for key in char:
        print("%s:%s " % (key,char[key]))
        f.write("%s:%s\n" % (key,char[key]))
    f.close()