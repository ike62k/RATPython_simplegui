#RIFE AutomationTool Python SimpleGUI Ver1.2 2022/9/14

import PySimpleGUI as sg
import os
import concurrent.futures
import sys
import configparser


os.chdir(os.path.dirname(__file__))


configdata = configparser.ConfigParser()
configdata.read("RAT_simpleguiconfig.ini", encoding="utf-8")
configdata = configdata["DEFAULT"]


#初期設定
Basefile =""
video_list = []
result = ""
Default_ver = str(configdata.get("RIFEVER"))
Default_interpolation = str(configdata.get("INTERPOLATION"))
Default_bitrate = str(configdata.get("BITRATE"))
Default_codec = str(configdata.get("CODEC"))
Default_picture = str(configdata.get("PICTURE"))
Default_jpgquality = str(configdata.get("JPGQUALITY"))
Default_rifeusage = str(configdata.get("RIFEUSAGE"))
interpolation = ""
rifever = ""
bitrate = ""
codec = ""
picture = ""
jpgquality = ""
rifeusage = ""
systemrunner = False
startchecker = False
endchecker = False
closetab = False
process_status = False
themename = str(configdata.get("THEME")) #https://pysimplegui.readthedocs.io/en/latest/readme/#themes

#from以下には使用したいRIFEAutomationToolのファイル名を記入(基本的にバージョンアップごとに機能が変わっているので、変更は完全非推奨)
from RIFEAT import mainfunc


def processfunc(setting):
    global process_status
    for video in video_list:
        try:
            print(f"{video}の補完処理を開始します")

            mainfunc(video,True,setting)
        except:
            print(f"{video}の補完処理に失敗しました")
        else:
            print(f"{video}の補完処理に成功しました")
    print("すべての作業が完了しました")
    window["開始"].update(disabled=False)
    process_status = False


def listupdate():
    window["-listlist-"].update(values=video_list)
    return


sg.theme(themename)

layout = [
    [sg.Text("補完するファイルを選択してください")],
    [sg.Input(key="-directinput-", size=(60,1), enable_events=True), sg.Button("追加"), sg.Input(key="-inputobserver-", enable_events=True, visible=False), sg.FileBrowse("参照", key="-SelectFile-", enable_events=True)],
    [sg.Listbox(video_list, size=(100,5),key="-listlist-")],
    [sg.Input(key="-selectdelete-", size=(5,1)), sg.Button("番目のファイルを削除する"), sg.Button("リストの最後を削除する"), sg.Button('リストをすべて削除する')],
    [sg.Text("Option")],
    [sg.Text("・RIFE-"), sg.Combo(["無印","anime","HD","UHD","v2","v2.4","v3.0","v3.1","v4"], default_value= Default_ver, key="-rifever-", size=(6,1), readonly=True), sg.Text("    ・補完倍率"), sg.Combo(["2","4"], default_value= Default_interpolation, key="-interpolation-"), sg.Text("    ・ビットレート"), sg.Input(default_text=Default_bitrate, key="-bitrate-", size=(8,1)), sg.Text("bps"), sg.Text("    ・コーデック"), sg.Input(default_text=Default_codec, key="-codec-", size=(10,1))],
    [sg.Text("・画像コーデック"), sg.Combo(["jpg","png"], default_value = Default_picture, key="-picture-", readonly=True), sg.Text("    ・画像品質"), sg.Input(default_text=Default_jpgquality, key="-jpgquality-", size=(20,1)), sg.Text("    ・RIFEスレッド数"), sg.Input(default_text = Default_rifeusage, key="-rifeusage-", size=(16,1))],
    [sg.Output(size=(100,20), key="-Reply-", )],
    [sg.Button("ファイルを確認する"), sg.Button("開始")],
]


window = sg.Window("RIFE", layout)


while True:
    event, values= window.read()

    if event == sg.WINDOW_CLOSED:
        closetab = True
        break

    if event == "-inputobserver-":
        if not str(values["-SelectFile-"]) == "":
            video_list.append(values["-SelectFile-"])
            listupdate()
            print("ファイルを追加しました")

    if event == "追加":
        if not str(values["-directinput-"]) == "":
            video_list.append(values["-directinput-"])
            listupdate()
            print("ファイルを追加しました")
    
    if event == "ファイルを確認する":
        print("===選択したファイル一覧===\n")
        for i in range(len(video_list)):
            print(video_list[i])
        print("\n======")

    if event == "番目のファイルを削除する":
        try:
            target_number = int(values["-selectdelete-"]) - 1
            target_name = video_list[target_number]
            del video_list[target_number]
        except:
            print("指定した番目は存在しません")
        else:
            print(f"{target_name}を削除しました")
            listupdate()
            

    if event == "リストの最後を削除する":
        try:
            print(f"{video_list[-1]}を削除しました")    
        except:
            print("リストはすでに空です")
        else:
            del video_list[-1]
            listupdate()

    if event == "リストをすべて削除する":
        video_list.clear()
        listupdate()
        print("リストをすべて削除しました")

    if event == "開始":
        window["-rifever-"].update
        window["-interpolation-"].update
        window["-bitrate-"].update
        window["-picture-"].update
        window["-jpgquality-"].update
        window["-rifeusage-"].update
        window["-codec-"].update

        rifever = str(values["-rifever-"])
        if rifever == "無印":
            rifever = ""
        else:
            rifever = "-" + rifever
        interpolation = str(values["-interpolation-"])
        bitrate = str(values["-bitrate-"])
        picture = str(values["-picture-"])
        jpgquality = str(values["-jpgquality-"])
        rifeusage = str(values["-rifeusage-"])
        codec = str(values["-codec-"])

        setting = [codec,bitrate,rifever,rifeusage,interpolation,picture,jpgquality]

        window["開始"].update(disabled=True)
        process_status = True

        if __name__ == "__main__":
            process = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            process.submit(processfunc,setting)

sys.exit