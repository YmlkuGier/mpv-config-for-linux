### https://github.com/hooke007/mpv_PlayKit/wiki/3_K7sfunc
### 降低彩噪，开销中等

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

Nr_Lv = 30.0
## 浮点，彩噪阈值，越高的值降噪效果越明显（涂抹越重）

clip = k7f.CCD_STD(clip, nr_lv=Nr_Lv)

clip.set_output()
