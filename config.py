import sys
import os
import datetime

import pyauto
from keyhac import *


def configure(keymap):
    # ワンショットモディファイア
    keymap_global = keymap.defineWindowKeymap()
#    keymap.replaceKey( "(28)", "Alt" ) # 「変換」キーを一旦 Alt キーに置き換え、
#    keymap_global[ "O-Alt" ] = "(28)" # Alt キーがワンショットで押されたら 「変換」されるようにする
    keymap.replaceKey( "(29)", "Ctrl" ) # (29) は「無変換」キー
    keymap_global[ "O-Ctrl" ] = "(29)"
    keymap.replaceKey( "Space", "RShift" )
    keymap_global[ "O-RShift" ] = "Space"
    keymap_global[ "(242)" ] = "S-226" #アンダースコアはつかれるのでカタカナひらがなキーで出てくるようにする
#    keymap.replaceKey( "(242)", "6") # カタカナひらがなキーはいらないので打ちにくい6にする