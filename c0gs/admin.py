import discord
import json
from discord.ext import commands


class AdminC(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events_________________________________________________________________________________
    @commands.Cog.listener()  # Set prefix on joining the server
    async def on_guild_join(self, guild):

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '!'

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f)

    @commands.Cog.listener()  # Remove prefix on leaving the server
    async def on_guild_remove(self, guild):

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

    # Commands_______________________________________________________________________________

    # Prefix Command, change it and store in a json file

    @commands.command(aliases=['prefix', 'fix'], brief='Muda o prefixo do servidor!',
                      description='Muda o prefixo do servidor! [Usos alternativos: `prefix` / `fix`')
    @commands.has_permissions(administrator=True)
    async def prefixo(self, ctx, fix):

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = fix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f)

        return await ctx.send('O prefixo foi mudado para `{}`'.format(fix))

    # _______________________________________________________________________________________

    # Toggle command to deactivate/activate a command

    @commands.command(aliases=['toggle', 'ativar', 'desativar'], brief='Ativa ou Desativa algum comando!',
                      description='Ativa ou Desativa algum comando!')
    @commands.has_permissions(administrator=True)
    async def alternar(self, ctx, command):
        command_ = self.client.get_command(command)

        if command_ == None:

            await ctx.send('Este comando não existe')

        elif command_ == ctx.command:

            await ctx.send('Você não pode alterar esse comando.')

        elif str(command_) == 'prefixo':

            await ctx.send('Você não pode alterar esse comando.')

        elif str(command_) in ['load', 'unload', 'reload']:

            await ctx.send('Este comando não existe')

        else:

            command_.enabled = not command_.enabled
            situation = 'ativado' if command_.enabled else 'desativado'

            await ctx.send(f'O comando `{command}` foi **{situation}**!')

    # _______________________________________________________________________________________

    # Clear command, delete messages from the chat

    @commands.command(aliases=['clear'], brief='Apaga quantas mensagens do chat você quiser.',
                      description='This is the full description')
    @commands.has_permissions(manage_messages=True)
    async def limpar(self, ctx, amount=2):

        await ctx.channel.purge(limit=amount)

    # _______________________________________________________________________________________
    # Kick command

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):

        await user.kick(reason=f'Usuario punido por: {ctx.author} com o Motivo: {reason}')
        await ctx.message.add_reaction('✅')
        await ctx.send(f'✅ | {ctx.author.mention} Usuário punido!')

    # _______________________________________________________________________________________
    # Ban command

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):

        await user.ban(reason=f'Usuario punido por: {ctx.author} com o Motivo: {reason}')
        await ctx.message.add_reaction('✅')
        await ctx.send(f'✅ | {ctx.author.mention} Usuário punido!')

    # _______________________________________________________________________________________
    # Unban command

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user, *, reason=None):

        user = discord.Object(id=user)

        await ctx.guild.unban(user, reason=f'Usuario perdoado por: {ctx.author} com o Motivo: {reason}')
        await ctx.message.add_reaction('✅')
        await ctx.send(f'✅ | {ctx.author.mention} Usuário desbanido!')


def setup(client):
    client.add_cog(AdminC(client))

















