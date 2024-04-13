from os import getenv
import discord
import discord.app_commands
import chat
import json_load


DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = getenv("GEMINI_API_KEY")
DISCORD_SERVER_ID = discord.Object(getenv("DISCORD_SERVER_ID"))

command_data = json_load.jsonLoad()
chat_data = chat.Chat(GEMINI_API_KEY)


client = discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree(client)


@tree.command(name="about", description=command_data.get_command_description("about"))
async def about(ctx:discord.Interaction) -> None:
    async with ctx.channel.typing():
        await ctx.response.defer(thinking=True)
        embed = discord.Embed.from_dict(command_data.get_command_embed("about"))
        await ctx.followup.send(embed=embed)

@tree.command(name="chat", description=command_data.get_command_description("chat"))
async def chat(ctx:discord.Interaction, message:str) -> None:
    async with ctx.channel.typing():
        await ctx.response.defer(thinking=True)
        embed = discord.Embed(description=message)
        embed.set_author(name=ctx.user.name, icon_url=ctx.user.avatar.url)
        embed.add_field(name="Gemini-Proの回答", value=chat_data.get_response(message)[:1024])
        await ctx.followup.send(embed=embed)

@tree.context_menu(name="Gemini replies to message")
async def reply(ctx:discord.Interaction, message:discord.Message) -> None:
    async with ctx.channel.typing():
        await ctx.response.defer(thinking=True)
        embed = discord.Embed(description=message.content)
        embed.set_author(name=ctx.user.name, icon_url=ctx.user.avatar.url)
        embed.add_field(name="Gemini-Proの回答", value=chat_data.get_response(message.content)[:1024])
        await ctx.followup.send(embed=embed)

@client.event
async def on_ready() -> None:
    print(f"LOGGED IN: {client.user.name}")
    tree.copy_global_to(guild=DISCORD_SERVER_ID)
    await tree.sync(guild=DISCORD_SERVER_ID) #コマンド同期
    print("COMMAND SYNCED")
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name="Gemini 1.5 Proを実行中"))

# Discordに接続
client.run(DISCORD_BOT_TOKEN)
