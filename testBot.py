import asyncio
import discord
from discord.ext import commands
import asyncio
#import youtube_dl

client =commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('Bot is ready!')
    

@client.event
async def on_member_join(member):
    print(f'{member} has joined server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left server.')
@client.command()
async def botPing(ctx):
    await ctx.send(f'Ping! {round(client.latency *1000)}ms')
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)
@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
@client.command()
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
@client.command()
async def stop(ctx):
    await client.logout()

    
    


client.run('NjI2NjIzNTMzNDgwNTQyMjI4.XY1BEA.GOdBkq7HLoKakUERU2ipYfie89c')
#NjI2NjIzNTMzNDgwNTQyMjI4.XY1BEA.GOdBkq7HLoKakUERU2ipYfie89c

