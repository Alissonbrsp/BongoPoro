# Bloco 01 — Preparação do ambiente

Objetivo: preparar o ambiente Python para o BongoBuster. Execute em um terminal gráfico do Kali Linux.

## Instalação

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git python3-pygame
python3 --version
pip3 --version
git --version
```

## Repositório e estrutura

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/Alissonbrsp/BongoPoro.git
cd BongoPoro
mkdir -p assets/{images,sprites,sounds} src config docs tests
touch src/{main,character,animations,inputs,config}.py
```

Se já clonou o repositório, entre nele e use `git pull --ff-only` após verificar `git status`.

## Ambiente virtual

```bash
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pynput numpy sounddevice
```

Pygame é instalado via APT para facilitar a compatibilidade com Kali. O ambiente virtual acessa os pacotes do sistema. Em caso de erro do PortAudio, instale `sudo apt install libportaudio2`.

## Validação

```bash
python -c "import pygame, pynput, numpy, sounddevice; print('BongoBuster: OK')"
```

O pynput requer uma sessão gráfica compatível; no Linux, X11 é a opção inicial. A validação ainda deve ser realizada no computador do usuário. Não há protótipo executável nesta etapa.

## Privacidade

Não publicar fotografias pessoais, ambientes virtuais, credenciais, gravações de áudio ou registros de teclas. O projeto deverá processar eventos localmente sem armazenar o conteúdo digitado.
