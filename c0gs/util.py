import discord
import requests
from discord.ext import commands
import random
import json
from pprint import pprint
import asyncio

class Comandos(commands.Cog):

    def __init__(self, client):
        self.client = client

    # _______________________________________________________________________________________
    # Say command, makes the bot type something


    @commands.command(aliases=['say'], brief='Faz com que eu fale algo.',
                      description='This is the full description')  # Say Command
    async def falar(self, ctx, *, fala):
        await ctx.send(f'{fala}')

    # _______________________________________________________________________________________
    # @commands.command(aliases=['help']) #Help Command
    # async def ajuda(self, ctx):
    # await ctx.send('```LISTA DE COMANDOS:\nPrefixo| Diz qual o prefixo do servidor\nAlternar| Liga e desliga algum dos meus comandos.\nLimpar| Deleta mensagens do canal(Padrão=10 Você pode escolher)\nFalar| Você faz eu dizer alguma coisa.```')
    # _______________________________________________________________________________________
    # Sayd command, makes the bot type something and the deletes your message

    @commands.command(aliases=['sayd'], brief='Faz com que eu fale algo, apagando seu comando.',
                      description='This is the full description')  # SayD Command
    async def falard(self, ctx, *, fala):

        await ctx.channel.purge(limit=1)
        await ctx.send(f'{fala}')

    # _______________________________________________________________________________________
    # Avatar command, shows the profile image of someone you mention

    @commands.command(brief='Mostra a imagem de perfil de alguém.',
                      description='This is the full description')  # Avatar Command
    async def avatar(self, ctx, *, member: discord.Member = None):

        if member == None:

            avatarUrl = ctx.author.avatar_url
            embed = discord.Embed(color=discord.Colour.blue())
            embed.add_field(name=f'🖼 {ctx.author.name}\n ⠀',value=f'**Clique [aqui]({avatarUrl}) para baixar a imagem.**', inline=False)
            embed.set_image(url=avatarUrl)
            await ctx.reply(embed=embed)

        else:

            avatarUrl = member.avatar_url
            embed = discord.Embed(color=discord.Colour.blue())
            embed.add_field(name=f'🖼 {ctx.author.name}\n ⠀',
                            value=f'**Clique [aqui]({avatarUrl}) para baixar a imagem.**', inline=False)
            embed.set_image(url=avatarUrl)
            await ctx.reply(embed=embed)



    # _______________________________________________________________________________________
    # Coinflip command, flip a coin to heads or tails

    @commands.command(aliases=['coinflip', 'coin'], brief='Cara ou Coroa.',
                      description='This is the full description')  # Coinflip command
    async def moeda(self, ctx):

        coin = random.randrange(0, 2)

        if coin == 0:

            await ctx.reply('<:cara:990479504365473822> **| Cara!**',mention_author=False)

        else:

            await ctx.reply('<:coroa:990479536430907433> **| Coroa!**',mention_author=False)

    # _______________________________________________________________________________________
    # Rock, paper, scissors command
    @commands.command(aliases=['jankenpon', 'ppt', 'rps'], brief='Pedra Papel ou Tesoura.',
                      description='This is the full description')  # Jankenpon command
    async def jokenpo(self, ctx, escolha):
        escolha = escolha.lower()
        escolhabot = random.randrange(0, 3)
        if escolhabot == 0 and escolha == 'pedra':
            await ctx.reply('Você escolheu 🪨 e eu escolhi 🪨... Deu EMPATE!!',mention_author=False)

        elif escolhabot == 1 and escolha == 'pedra':
            await ctx.reply('Você escolheu 🪨 e eu escolhi 📰... Você PERDEU!!',mention_author=False)

        elif escolhabot == 2 and escolha == 'pedra':
            await ctx.reply('Você escolheu 🪨 e eu escolhi ✂... Você VENCEU!!',mention_author=False)

        elif escolhabot == 0 and escolha == 'papel':
            await ctx.reply('Você escolheu 📰 e eu escolhi 🪨... Você VENCEU!!',mention_author=False)

        elif escolhabot == 1 and escolha == 'papel':
            await ctx.reply('Você escolheu 📰 e eu escolhi 📰... Deu EMPATE!!',mention_author=False)

        elif escolhabot == 2 and escolha == 'papel':
            await ctx.reply('Você escolheu 📰 e eu escolhi ✂... Você PERDEU!!',mention_author=False)

        elif escolhabot == 0 and escolha == 'tesoura':
            await ctx.reply('Você escolheu ✂ e eu escolhi 🪨... Você PERDEU!!',mention_author=False)

        elif escolhabot == 1 and escolha == 'tesoura':
            await ctx.reply('Você escolheu ✂ e eu escolhi 📰... Você VENCEU!!',mention_author=False)

        elif escolhabot == 2 and escolha == 'tesoura':
            await ctx.reply('Você escolheu ✂ e eu escolhi ✂... Deu EMPATE!!',mention_author=False)

        else:
            await ctx.reply('Você escolheu 💩 e eu escolhi DEUS 🙏 Você PERDEU!!',mention_author=False)

    # _______________________________________________________________________________________
    # Dice command, rolls a dice of your choice

    @commands.command(aliases=['roll', 'dice'], brief='Vou rolar um dado da sua escolha.',
                      description='This is the full description')  # Roll command
    async def dado(self, ctx, *, escolha=None):
        if escolha != None:
            escolha = escolha.lower().replace(' ', '')

        if escolha == None:

            rolar = random.randrange(1, 7)
            return await ctx.reply(f'{ctx.author.mention} rolou 6 e conseguiu: {rolar}')

        elif escolha.isnumeric():

            rolar = random.randrange(1, int(escolha) + 1)
            return await ctx.reply(f'{ctx.author.mention} rolou {escolha} e conseguiu: {rolar}')

        else:

            try:

                y, z = escolha.split('d')
                nlist = [random.randrange(1, int(z) + 1) for x in range(int(y))]
                soma = sum(k for k in nlist)
                return await ctx.reply(f'{ctx.author.mention} rolou {z} e tirou `{soma}`! Seus numeros foram `{[k for k in nlist]}`')

            except:
                await ctx.reply('Este comando precisa que você use algo tipo `1d1`')

    # _______________________________________________________________________________________
    # Is this a meme? edit this meme image to your liking

    @commands.command()
    async def issoeh(self, ctx, *, frase):

        pessoa, frase2 = frase.split('-')
        frase2 = frase2.replace(' ', '_')
        link = str(ctx.message.attachments[0].url)
        final = 'https://api.memegen.link/images/pigeon/{}/_/{}~q.png?style={}'.format(pessoa, frase2, link)
        await ctx.reply(final)

    # _______________________________________________________________________________________
    # Hug command, use it to send a img/gif of a hug to someone

    @commands.command(aliases=['abraço', 'abraco','abracar','abraçar'])
    async def hug(self, ctx, *, member: discord.Member = None):
        r = requests.get('https://api.waifu.pics/sfw/hug')
        content = r.text[8:-3]
        if member == None:

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

        if member:
            embed = discord.Embed(title=f'❤ **| {ctx.author.name} abraçou {member.name}!**', color=discord.Colour.blue())
            embed.set_image(url=content)

            return await ctx.reply(member.mention,embed=embed)

    @commands.command()
    async def anime(self, ctx, *, procura):
        page = 0
        r = requests.get(f'http://staging.jikan.moe/v4/anime?q={procura}&sfw')
        anime_data = r.json()
        url = anime_data['data'][page]['url']
        mal='https://cdn.discordapp.com/attachments/989374831487229952/993011826109448223/unknown.png'
        title = anime_data['data'][page]['title']
        score = anime_data['data'][page]['score']
        if score == None:
            score = '??'
        image = anime_data['data'][page]['images']['jpg']['image_url']
        episodes = str(anime_data['data'][page]['episodes'])
        duration = anime_data['data'][page]['duration']
        aired = anime_data['data'][page]['aired']['string']
        source = anime_data['data'][page]['source']
        try:
            studio = anime_data['data'][page]['studios'][0]['name']
        except IndexError as index_error:
            print(index_error)
            studio = 'Não expecificado'
        genres = [anime_data['data'][page]['genres'][generos]['name'] for generos in range(len(anime_data['data'][page]['genres']))]
        if len(genres) == 0:
            genres.append('Não expecificado')
        synopsis = anime_data['data'][page]['synopsis'][:-25]
        rank = anime_data['data'][page]['rank']
        synonyms = anime_data['data'][page]['title_synonyms']
        english_title = anime_data['data'][page]['title_english']
        if english_title != None:
            synonyms.insert(0, english_title)
        else:
            english_title = ' '
        japanese_title = anime_data['data'][page]['title_japanese']
        if japanese_title != None:
            synonyms.append(japanese_title)
        else:
            pass
        status = anime_data['data'][page]['status']
        type = anime_data['data'][page]['type']



        embed = discord.Embed(title=f"{title} ({english_title})", url=url, description=synopsis,color=discord.Colour.blue())

        embed.set_author(name=f"Tipo: {type} • Status: {status} • Nota: {score} • Rank: {rank}",
                         icon_url=mal)
        embed.set_thumbnail(
            url=image)
        embed.add_field(name="**Episódios**", value=f'`{episodes}`', inline=True)
        embed.add_field(name="**Duração**", value=f'`{duration}`', inline=True)
        embed.add_field(name="**Data de lançamento**", value=f'`{aired}`', inline=False)
        embed.add_field(name="**Fonteㅤ**", value=f'`{source}`', inline=True)
        embed.add_field(name="**Estúdio**", value=f'`{studio}`', inline=True)
        embed.add_field(name="**Gêneros**", value=' • '.join(f'`{x}`' for x in genres), inline=False)
        embed.add_field(name="**Nomes alternativos**", value=' • '.join(f'`{x}`' for x in synonyms), inline=False)
        embed.add_field(name="**Saiba mais**", value=f"[Myanimelist Page]({url})", inline=False)
        embed.set_footer(icon_url='https://cdn.discordapp.com/avatars/989409439956213830/b9336d36eb09936ca2405830600c1bc3.webp?size=1024', text="De: myanimelist.com")
        mensagem = await ctx.send(embed=embed)

        return


def setup(client):
    client.add_cog(Comandos(client))

