#!/bin/bash

git init

# 添加所有更改到暂存区
git add .

# 提交这些更改
git commit -m "Update all files and folders"

# 切换到 main 分支（如果需要）
git branch -M main

# 添加远程仓库
git remote add origin https://github.com/mmqqq-art/hellometron.git

# 拉取远程仓库的更改并允许不相关的历史合并
git pull origin main --allow-unrelated-histories

# 强制推送你的更改到远程仓库
git push -u origin main --force
