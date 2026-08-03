#!/bin/bash

cd "$(dirname "$0")" || exit

if command -v mpv >/dev/null 2>&1; then
    mkdir -p ~/.config/mpv

    if ls -A ~/.config/mpv &>/dev/null; then
        read -p "警告：$HOME/.config/mpv 已有配置，是否覆盖？(y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf ~/.config/mpv/*
            cp -r ./portable_config/* ~/.config/mpv/
            echo "--- 覆盖完成 ---"
        else
            echo "操作已取消。"
            exit 0
        fi
    else
        cp -r ./portable_config/* ~/.config/mpv/
        echo "--- 配置完成 ---"
    fi
else
    echo "mpv 未安装，请先安装。"
fi