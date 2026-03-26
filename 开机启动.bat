@echo off
chcp 65001 >nul

echo 📂 正在打开自启动文件夹...
explorer shell:startup
echo ✅ 文件夹已打开！你可以将需要开机自启的快捷方式拖入其中。

pause