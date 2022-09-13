#!/usr/bin/env python
# coding: utf-8

import os
import signal
import sys
from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv

from db import Database

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='.',
                   intents=intents,
                   description='A Discord bot to save custom quotes.')

db = Database()


def keyboard_interrupt_handler(sig: int, _) -> None:
    print(f'\nKeyboardInterrupt (id: {sig}) has been caught...')
    print('Terminating the session gracefully...')
    db.con.close()
    sys.exit(1)


@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('-' * 80)


@bot.command('.')
async def add_quote(ctx: Context,
                    keyword: str,
                    message: Optional[str] = None) -> None:
    if not message:
        return
    exists, values = db.insert_quote(keyword, message, ctx.author.id)
    if exists:
        await ctx.send(f'Quote already exists: #{exists[0]}!')
    else:
        print([ctx.guild.name, ctx.guild.id, *values])
        await ctx.send(f'Added: #{values[0]}')


@bot.command('..')
async def get_quote(ctx: Context, keyword: str) -> None:
    results = db.fetch_quote(keyword)
    if results:
        await ctx.send(f'#{results[0]}: {results[1]}')


@bot.command('qdel')
async def del_quote(ctx: Context, _id: int) -> None:
    db.delete_quote(_id, ctx.author.id)
    await ctx.send(f'Deleted #{_id}')


@bot.command('qinfo')
async def get_quote_info(ctx: Context, _id: int) -> None:
    print(type(ctx))
    result = db.fetch_by_id(_id)
    if not result:
        return
    _id, user_id, keyword, message, created_on = db.fetch_by_id(_id)
    embed = discord.Embed(
        title=f'#{_id}',
        description=f'**User:** <@!{user_id}>\n**Keyword:** {keyword}\n'
        f'**Message:** {message}\n**Created on:** {created_on}',
        colour=discord.Colour.blue())
    await ctx.send(allowed_mentions=discord.AllowedMentions.none(),
                   embed=embed)


def main() -> None:
    load_dotenv()
    token = os.environ['TOKEN']
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    bot.run(token)


if __name__ == '__main__':
    main()
