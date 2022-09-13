# qBot

🚀 A Discord bot to save and manage custom quotes for your server.

[![Supported Python versions](https://img.shields.io/badge/Python-%3E=3.6-blue.svg?logo=python)](https://www.python.org/downloads/) [![PEP8](https://img.shields.io/badge/Code%20style-PEP%208-orange.svg?logo=python)](https://www.python.org/dev/peps/pep-0008/) [![Discord.py](https://img.shields.io/badge/Discord.py->=1.7.3-yellow.svg?logo=python)](https://github.com/Rapptz/discord.py) [![GitHub License](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/Alyetama/Discord-Backup-Bot/blob/main/LICENSE)

## ☑️ Requirements
- 🐍 [python>=3.6](https://www.python.org/downloads/)

## ⬇️ Installation

```sh
git clone https://github.com/Alyetama/qbot.git
cd qbot
pip install -r requirements.txt
```

## ⌨️ Getting Started

- Rename `.env.example` to `.env`, then edit it with your favorite text editor to add your bot token.
- Then, run:

```sh
python bot.py  # For verbose output, pass: `--print-logs`
```

## 🐳 Docker

```shell
export TOKEN="xxxxxxxxxxxxxxxxxxxxxx"

docker run \
  -d --restart unless-stopped \
  -e TOKEN="${TOKEN}" \
  -v "${PWD}/database":/database \
  alyetama/qbot:latest
```


## 🤖 Commands

- To save a quote: `.qa <quote>`
- To get a quote by keyword: `.q <keyword>`
- To get a quote info by id: `.qinfo <quote_id>`
- To delete a quote: `.qdel <quote_id>`
- To get a random quote: `.qrand`


## 🗒️ Notes

- Discord now requires `Message Content Intent` to be turned on to handle the content of messages. Make sure you have it turned on for your bot in the developer portal: `Bot` -> `Message Content Intent`.
