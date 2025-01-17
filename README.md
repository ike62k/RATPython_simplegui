# RATPython_simplegui
# 重要
**このプログラムはRIFEAutomationToolPython Version 1.x用のアドオンです。<br>
Version2.x~には対応しませんのでご注意ください、またそれに伴ってこのアドオンの開発は凍結しています。<br>
Version2.xでのGUI実装は本体リポジトリ[RIFEAutomationToolPython](https://github.com/ike62k/RIFEAutomationToolPython)で作成されています。**

[RIFEAutomationToolPython](https://github.com/ike62k/RIFEAutomationToolPython)のGUI動作用アドオン。左記のプログラムに付け加える形で動作します<br>
Python本体に付け加えて、外部ライブラリである[PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)を使用しています<br>
プログラム本体のダウンロードは[こちら](https://github.com/ike62k/RIFEAutomationToolPython/releases)から

本アドオンのダウンロードは[こちら](https://github.com/ike62k/RATPython_simplegui/releases)から

# 注意事項
1. 補完対象のパスに半角スペース(' ')が含まれているとうまく動作しません
2. 補完対象のパスにドット('.')が含まれているとうまく動作しません
3. 補完対象が実行ファイルと違うドライブ(相対パスで位置を書き表せない位置)にあるファイルではうまく動作しません(修正予定)
4. 'Shell = True'を使用しているので入力次第で予期しない動作を引き起こす可能性があります
5. 同梱されているRAT_simpleguiconfig.iniに初期値の設定があるため、先に環境に応じて設定をしてから使用してください
6. このソフトウェアは趣味で制作されたものです。本ソフトウェアの使用によって引き起こされた全ての結果について作者は一切の責任を負いません

# 必要ソフトウェア
1. [rife-ncnn-vulkan.exeと各種プロファイル](https://github.com/nihui/rife-ncnn-vulkan)
2. [ffmpegとffprobe](https://www.ffmpeg.org/)
3. [Python3](https://www.python.org/)
4. [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
5. [RIFEAutomationToolPython](https://github.com/ike62k/RIFEAutomationToolPython)

# 対応動画  
入力ファイル : ffmpegで動画ファイルとして読み込めるほとんどすべての映像/音声形式  
出力ファイル : コンテナフォーマット→入力ファイルと同じ / 映像コーデック→ユーザー指定 /  音声コーデック→ユーザー指定 

# 使い方
1. [RIFEAutomationToolPython](https://github.com/ike62k/RIFEAutomationToolPython)の環境を作成する
2. 上記ファイルやffmpegなどと同じフォルダにこのソフトウェアを貼り付ける
3. [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)をインストールする
4. このソフトウェアをPythonで実行し、指示に従う


# はしがき<br>
こちらも例の如く最新バージョン以外非推奨
