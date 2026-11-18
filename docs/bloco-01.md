# Bloco 01 — Preparação do ambiente

Objetivo: preparar o ambiente Python para o BongoBuster. Execute em um terminal gráfico do Kali Linux.

## Instalação

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git libportaudio2
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
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --only-binary=:all: pygame-ce
python -m pip install pynput numpy sounddevice
```

Pygame CE é instalado em ambiente isolado para evitar incompatibilidade SDL e compilação do Pygame 2.6.1 no Python 3.14. Em caso de erro do PortAudio, instale `sudo apt install libportaudio2`.

## Validação

```bash
python -c "import pygame, pynput, numpy, sounddevice; print('BongoBuster: OK')"
```

O pynput requer uma sessão gráfica compatível; no Linux, X11 é a opção inicial. Renderização gráfica validada pelo usuário com `python -m pygame.examples.aliens`. Teclado global e áudio ainda precisam de testes.

## Privacidade

Não publicar fotografias pessoais, ambientes virtuais, credenciais, gravações de áudio ou registros de teclas. O projeto deverá processar eventos localmente sem armazenar o conteúdo digitado.
