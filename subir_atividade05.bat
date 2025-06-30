@echo off
cd /d "D:\Atividade Prática 05"

:: Inicializa o repositório (caso ainda não esteja iniciado)
git init

:: Adiciona todos os arquivos, incluindo o README.md
git add .

:: Faz o commit com mensagem
git commit -m "Atividade 05 concluída com README"

:: Define o repositório remoto (altere se necessário)
git remote add origin https://github.com/pdrlucs/Atividade05.git

:: Define o branch principal como main
git branch -M main

:: Envia os arquivos para o GitHub
git push -u origin main

pause
