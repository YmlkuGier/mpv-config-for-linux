# mvp-config-for-linux

> 基于 **hooke007/mpv_PlayKit** 兼容linux端

## 安装教程

1. 必要软件包``python``,``python-pip``
2. 使用``mvtools``补帧方案需要安装``vapoursynth-plugin-mvtools``插件
3. 使用``svpflow``补帧方案需要安装``vapoursynth-plugin-svpflow``插件

```bash
# 运行目录下的setup脚本即可
./setup.sh
```

## [按键速查](./KeyBinding.md)

## 常见问题

- 使用补帧的时候提示``changing filters failed!``
  - 删除``mpv``软件包,更换成``mpv-full``
- 使用补帧没效果
  - 安装``vapoursynth-plugin-mvtools``

## 代办事项

-[x] 补帧滤镜修复