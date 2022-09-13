# qBot

🚀 A Discord bot to save and manage custom quotes for your server.

[![Supported Python versions](https://img.shields.io/badge/Python-%3E=3.6-blue.svg?logo=python)](https://www.python.org/downloads/) [![PEP8](https://img.shields.io/badge/Code%20style-PEP%208-orange.svg?logo=python)](https://www.python.org/dev/peps/pep-0008/) [![Discord.py](https://img.shields.io/badge/Discord.py->=1.7.3-yellow.svg?logo=python)](https://github.com/Rapptz/discord.py) [![GitHub License](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/Alyetama/Discord-Backup-Bot/blob/main/LICENSE)

[![Discord](https://img.shields.io/badge/Invite%20To%20Your%20Server-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/api/oauth2/authorize?client_id=1019318659484766360&permissions=0&scope=bot)

## Commands

- To save a quote: `.. <quote>`
- To get a quote by id: `... <quote_id>`
- To get a quote info: `.qinfo <quote_id>`
- To delete a quote: `.qdel <quote_id>`
- To get a random quote: `.qrand`

## Required Bot Permissions

`Read Messages`, `Send Messages`, `Embed Links`.

---

## Self-Hosting

### Requirements
- 🐍 [python>=3.6](https://www.python.org/downloads/)

### ⬇️ Installation

```sh
git clone https://github.com/Alyetama/qbot.git
cd qbot
pip install -r requirements.txt
```

### ⌨️ Usage

- Rename `.env.example` to `.env`, then edit it with your favorite text editor to add your bot token.
- Then, run:

```sh
python bot.py
```
