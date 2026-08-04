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

    echo ">>> 安装 VapourSynth 依赖 k7sfunc ..."
        cd ~/.config/mpv/ || exit
        if command -v pip >/dev/null 2>&1; then
            python -m venv venv
            source venv/bin/activate
            pip install -U k7sfunc
        elif command -v pip3 >/dev/null 2>&1; then
            python -m venv venv
            source venv/bin/activate
            pip3 install -U k7sfunc
        else
            echo "警告：未找到 pip，请手动安装python和pip"
        fi

else
    echo "mpv 未安装，请先安装。"
fi