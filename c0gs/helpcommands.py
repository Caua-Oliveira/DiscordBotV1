import discord
from discord.ext import commands


class HelpCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['help'])
    async def ajuda(self, ctx, *, escolha=None):
        if escolha != None:
            escolha = escolha.lower()

        if escolha==None:

            embed = discord.Embed(title="📰👴",
                                  description="**Use `!ajuda` <categoria> para ver informações sobre uma categoria.**\n**Use `!ajuda` <comando> para ver informações sobre um comando.**\n\nAqui está todos os meus comandos:",
                                  color=discord.Colour.blue())
            embed.set_author(name="Prazer, meu nome é Enzo.",
                             icon_url="https://cdn.discordapp.com/avatars/989409439956213830/b9336d36eb09936ca2405830600c1bc3.webp?size=1024")
            embed.add_field(name="**Admin**", value="`prefixo` • `alternar` • `limpar` • `kick` • `ban` • `unban` ",
                            inline=False)
            embed.add_field(name="**Variedade**", value="`falar` • `falard` • `avatar`, `moeda` • `ppt` • `dado` • `hug`",
                            inline=False)
            embed.set_footer(text='Bom uso! ✌')

            return await ctx.reply(embed=embed)

        if escolha in ['prefix', 'prefixo']:

            embed = discord.Embed(title="✏ | `!prefixo`",
                                  description="Use esse comando para alterar o prefixo do servidor!",
                                  color=discord.Colour.blue())
            embed.set_author(name="Espero que isso te ajude!",
                             icon_url="https://cdn.discordapp.com/avatars/989409439956213830/b9336d36eb09936ca2405830600c1bc3.webp?size=1024")
            embed.add_field(name="📖 **| Exemplos**", value="`!prefixo +`\nAgora o comando seria `+prefixo`",
                            inline=False)
            embed.add_field(name="🔀 **| Sinônimos**", value="`prefix`",
                            inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)

            return await ctx.reply(embed=embed)

        if escolha in ['abraco', 'abraço', 'abraçar', 'abracar', 'hug']:

            embed = discord.Embed(title="🤗 **| `!hug`**",
                                  description="Use esse comando para abraçar alguem especial!",
                                  color=discord.Colour.blue())
            embed.set_author(name="Espero que isso te ajude!",
                             icon_url="https://cdn.discordapp.com/avatars/989409439956213830/b9336d36eb09936ca2405830600c1bc3.webp?size=1024")
            embed.add_field(name="📖 **| Exemplos**", value="`!hug 989409439956213830`\n`!hug @AlgumaPessoaLegal`",
                            inline=False)
            embed.add_field(name="🔀 **| Sinônimos**", value="`abraço`, `abraco`, `abraçar`, `abracar`",
                            inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)

            return await ctx.reply(embed=embed)

        if escolha in ['dice', 'dado', 'roll']:

            embed = discord.Embed(title="🎲 **| `!dado`**",
                                  description="Use esse comando para rolar um dado de sua escolha! (Padrão = 6)",
                                  color=discord.Colour.blue())
            embed.set_author(name="Espero que isso te ajude!",
                             icon_url="https://cdn.discordapp.com/avatars/989409439956213830/b9336d36eb09936ca2405830600c1bc3.webp?size=1024")
            embed.add_field(name="📖 **| Exemplos**", value="`!dado`\n`!dado 20`\n`!dado 3d10`",
                            inline=False)
            embed.add_field(name="🔀 **| Sinônimos**", value="`roll`, `dice`",
                            inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)

            return await ctx.reply(embed=embed)

        if escolha in ['coin', 'moeda', 'coinflip']:

            embed = discord.Embed(title="🌗 **| `!moeda`**",
                                  description="Use esse comando para jogar cara ou coroa!\nㅤ",
                                  color=discord.Colour.blue())
            embed.set_author(name="Espero que isso te ajude!",
                             icon_url="https://cdn.discordapp.com/avatars/989409439956213830/b9336d36eb09936ca2405830600c1bc3.webp?size=1024")
            embed.add_field(name="🔀 **| Sinônimos**", value="`coin`, `coinflip`",
                            inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)

            return await ctx.reply(embed=embed)

        if escolha in ['jokenpo', 'jankenpo', 'ppt']:

            embed = discord.Embed(title="✂ **| `!ppt`**",
                                  description="Use esse comando para jogar pedra papel ou tesoura!",
                                  color=discord.Colour.blue())
            embed.set_author(name="Espero que isso te ajude!",
                             icon_url="https://cdn.discordapp.com/avatars/989409439956213830/b9336d36eb09936ca2405830600c1bc3.webp?size=1024")
            embed.add_field(name="📖 **| Exemplos**", value="`!ppt tesoura`\n`!ppt pedra`\n`!ppt papel`",
                            inline=False)
            embed.add_field(name="🔀 **| Sinônimos**", value="`jokenpo`, `jankenpo`",
                            inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name)

            return await ctx.reply(embed=embed)







def setup(client):
    client.add_cog(HelpCommands(client))
