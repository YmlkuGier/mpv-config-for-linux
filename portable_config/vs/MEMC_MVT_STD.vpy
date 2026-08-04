### https://github.com/hooke007/mpv_PlayKit/wiki/3_K7sfunc
### mvtools倍帧，标准开销

import os
import sys

# 自动获取 Python 版本号
py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"

# 构建虚拟环境路径
venv_path = os.path.expanduser(f"~/.config/mpv/venv/lib/python{py_ver}/site-packages")

# 添加到 sys.path
if os.path.exists(venv_path):
    sys.path.insert(0, venv_path)
else:
    print(f"⚠️ 虚拟环境路径不存在: {venv_path}")

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# 用户选项 #
############

H_Pre = 1440
Qty_Lv = 3
Block = True
BlkSize = 8
ThSCD1 = 360
ThSCD2 = 80
Lk_Fmt = False
## 整数，预降低处理源高度（填你的显示器高度）
## <1|2|3> 质量等级
## <True|False> 是否使用Block模式
## <4|8|16|32> 块大小
## <0-1024> 场景检测阈值1
## <0-1024> 场景检测阈值2
## <True|False> 锁定像素格式为yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.MVT_MQ(clip, fps_in=container_fps, fps_out=container_fps*2, qty_lv=Qty_Lv, block=Block, blksize=BlkSize, thscd1=ThSCD1, thscd2=ThSCD2)

clip.set_output()
