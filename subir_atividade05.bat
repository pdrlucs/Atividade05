@echo off
cd /d "D:\Atividade Prática 05"
git init
git add .
git commit -m "Atividade 05 concluída com README"
git remote add origin https://github.com/pdrlucs/Atividade05.git
git branch -M main
git push -u origin main
pause