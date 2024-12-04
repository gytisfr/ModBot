#ModBot by ~ Gytis5089

import discord
import asyncio
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name=f"My prefix is * | ({len(client.guilds)})"))
	print('Aaaaaaaaaaaaaaaaaaaaaaaaaaaand we are online boys!')
	print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.event
async def on_guild_join(guild):
	join = discord.utils.get(guild.text_channels, name='general')
	if join:
		await join.send('Thank you for inviting me!\nUse *help to get started!')
		print(f'ModBot has joined {guild.name}')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f"Welcome {member.mention} to {member.guild.name}")

def is_dev(ctx):
	return ctx.author.id in [301014178703998987]

@client.command(aliases=['i'])
async def invite(ctx):
	embed=discord.Embed(
		title="Invites",
		description='[ModBot Server](https://discord.gg/P4GGP9b)\n[Invite to Your Server](https://discord.com/oauth2/authorize?client_id=737708280847138837&permissions=8&scope=bot)',
        colour = 0x38c3ff,
	)
	await ctx.send(embed=embed)

@client.command(aliases=['p'])
async def ping(ctx):
	embed = discord.Embed(
		title = 'Ping',
		colour = 0x38c3ff,
		description = f'The current ping of this bot is {round(client.latency * 100)}ms {ctx.author.mention}'
	)
	embed.set_thumbnail(url="https://i.ibb.co/x3XHtXY/PFP.png")
	message = await ctx.send(embed=embed)

@client.command(aliases=['purge', 'wipe'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit=amount)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(f"{ctx.author.mention} has wiped {amount} messages in {ctx.channel.mention}")
	embed = discord.Embed(
		title = 'Clear',
		colour = 0x38c3ff,
		description = f'{ctx.author.mention} has wiped {amount} messages.'
	)
	embed.set_thumbnail(url="https://i.ibb.co/x3XHtXY/PFP.png")
	message = await ctx.send(embed=embed)
	await asyncio.sleep(3)
	await message.delete()

@clear.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['w'])
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member : discord.Member = None, *, arg):
	await member.send('You have been warned for:\n' + arg + f'\nBy {ctx.author.mention}')
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(f"{ctx.author.mention} has warned {member.mention} for " + arg)
	embed = discord.Embed(
        title = 'Warn',
        colour = 0x38c3ff,
        description = f'{ctx.author.mention} has warned {member.name} for:\n' + arg + f'By {ctx.author.mention}'
	)
	embed.set_thumbnail(url="https://i.ibb.co/x3XHtXY/PFP.png")
	message = await ctx.send(embed=embed)
	await asyncio.sleep(3)
	await message.delete()

@warn.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['m'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member = None, *, arg):
	role = discord.utils.get(member.guild.roles, name='muted')
	await member.add_roles(role)
	await member.send('You have been muted for:\n' + arg + f'\nBy {ctx.author.mention}')
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(f"{ctx.author.mention} has muted {member.mention} for " + arg)
	embed = discord.Embed(
        title = 'Mute',
        colour = 0x38c3ff,
        description = f'{ctx.author.mention} has muted {member.name} for:\n' + arg + f'By {ctx.author.mention}'
	)
	embed.set_thumbnail(url="https://i.ibb.co/x3XHtXY/PFP.png")
	message = await ctx.send(embed=embed)
	await asyncio.sleep(3)
	await message.delete()

@mute.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['um'])
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member = None):
	role = discord.utils.get(member.guild.roles, name='muted')
	await member.remove_roles(role)
	await member.send(f'You have been unmuted\nBy {ctx.author.mention}')
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(f"{ctx.author.mention} has unmuted {member.mention}")

@unmute.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.send('You have been kicked' + f'\nBy {ctx.author}')
	await member.kick(reason=reason)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(f"{ctx.author.mention} has kicked <@{member.id}>")

@kick.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason='The ban hammer has spoken!'):
	await member.send('You have been banned' + f'\nBy {ctx.author}')
	await member.ban(reason=reason)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(f"{ctx.author.mention} has banned <@{member.id}>")

@ban.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			channel = discord.utils.get(ctx.guild.text_channels, name='logs')
			await channel.send(f"{ctx.author.mention} has unbanned <@{user.id}>")
			await user.send('You have been unbanned' + f'\nBy {ctx.author}')

@unban.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['suggestion'])
async def suggest(ctx, *, arg):
	if ctx.channel.id == (739539623771897937):
		gytis = ctx.guild.get_member(301014178703998987)
		await gytis.send(f'Suggestion:\n{arg}\nfrom {ctx.author}')
		await ctx.send('Your suggestion has been sent.')

@client.command()
async def question(ctx, *, arg):
	if ctx.channel.id == (739539596466978917):
		gytis = ctx.guild.get_member(301014178703998987)
		await gytis.send(f'Question:\n{arg}\nfrom {ctx.author}')
		await ctx.send('Your question has been sent.')

@client.command(aliases=['guilds', 'guild', 'server'])
@commands.check(is_dev)
async def servers(ctx):
   embed = discord.Embed(title='Servers', colour=0x000000)

   for guild in client.guilds:
       embed.add_field(name=guild.name, value=f'`ID:`{guild.id}\n`Members:`{guild.member_count}\n`Owner:` {guild.owner}', inline=False)

   await ctx.author.send(embed=embed)
   await ctx.send('Sent.')

@servers.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Haha, yeah... You won't be accessing this.")

@client.command(aliases=['dm', 'pm', 'msg'])
@commands.check(is_dev)
async def message(ctx, member : discord.Member = None, *, arg):
	await member.send(f'Message from {ctx.author};\n' + arg)
	await ctx.send(f'{member.name} has been sent your message.')

@message.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
async def quote(ctx):
	quote = ["I'll pull the trigger on him, someone load the gun and cock it.",
	"If you stand for nothing, what'll you fall for?",
	"I am not throwing away my shot.",
	"There's a million things I haven't done, but just you wait.",
	"Talk less, smile more.",
	"This is not a moment, It's the movement.",
	"Look around at how lucky we are to be alive right now.",
	"I will kill your friends and family to remind you of my love.",
	"Dying is easy, living is harder.",
	"If there's a fire you're trying to douse, you can't put it out from inside the house.",
	"I'll write under a pseudonym, you'll see what I can do to him.",
	"What are you waiting for? What do you stall for?",
	"What was it all for?",
	"We studied and we fought and we killed for the notion of a nation we now get to build.",
	"For once in your life, take a stand with pride."]
	await ctx.send(random.choice(quote))

@client.command(aliases=['number', 'random'])
async def rng(ctx):
	rng = ["0",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"10"]
	await ctx.send(random.choice(rng))

@client.command(aliases=['flip', 'flipacoin', 'coinflip'])
async def coin(ctx):
	coin = ["Heads",
	"Tails"]
	await ctx.send(random.choice(coin))

@client.command(aliases=['join', 'joined', 'created'])
async def create(ctx, member : discord.Member = None):
		await ctx.send(f'{member.name} created their account on {str(member.created_at)[0:10]}')

@client.command(aliases=['trigger', 'trig'])
async def triggered(ctx):
	await ctx.send('https://media1.tenor.com/images/204a422e378751edf2c58c07eca56685/tenor.gif?itemid=18077100')

@client.command(aliases=['stillapieceofgarbage', 'garbage'])
async def sapog(ctx):
	await ctx.send('https://gyazo.com/adb610cb45f2deee8cc88d5ab3873c0e')

@client.command(aliases=['tryitandsee'])
async def tias(ctx):
	await ctx.send('https://i.imgur.com/8w8hPaT.png')

@client.command(aliases=['sb'])
async def stickbug(ctx):
	await ctx.send('https://tenor.com/view/get-stick-bugged-lol-gif-18023988')

@client.command()
@commands.has_permissions(administrator=True)
async def leave(ctx):
	await ctx.send('ModBot is now leaving this server...\nThanks for having me!')
	await ctx.send('To re-invite me just join the support server;\nhttps://discord.gg/P4GGP9b\nAnd do the command *invite')
	await ctx.guild.leave()

@leave.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.check(is_dev)
async def forceleave(ctx):
	await ctx.guild.leave()

@forceleave.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['8ball', 'eb', '8b'])
async def eightball(ctx, *, question=None):
    if question:
        answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
                   'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy',
                   'Try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                   'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no',
                   'Outlook not so good', 'Very doubtful']
        
        await ctx.send(f'{random.choice(answers)}.')
    else:
        await ctx.send('A question is required for this command.')

@client.command(aliases=['301014178703998987'])
@commands.check(is_dev)
async def aeuyfaesuyftvuyseabtfv6iant34w76nrtv76aw3intr37wirta7wirt3aww4ar7t3w876t6a6w3tnvr97vaw3vt697(ctx):
	embed = discord.Embed(
		title = 'DEVELOPER MODULE',
        colour = 0x000000,
        description = '`*message` - This command is used to message a specific member.\n`*servers` - This command sends you the list of servers the bot is in with all info.\n`*forceleave` - This command will force the bot to leave the server you use it in. (Restricted to Gytis only.)'
    )
	await ctx.send(embed=embed)

@aeuyfaesuyftvuyseabtfv6iant34w76nrtv76aw3intr37wirta7wirt3aww4ar7t3w876t6a6w3tnvr97vaw3vt697.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Haha, yeah... You won't be accessing this.")

@client.command()
@commands.check(is_dev)
async def BHA(ctx, arg):
	await ctx.send(f'<@{arg}> has been accepted into the ModBot Bug Hunting Team')

@client.command()
@commands.check(is_dev)
async def BHD(ctx, arg):
	await ctx.send(f'<@{arg}> has been declined for joining the ModBot Bug Hunting Team')

@client.command(aliases=['mh', 'MH'])
async def modhelp(ctx):
	embed = discord.Embed(
		title = 'Mod Help',
        colour = 0x38c3ff,
        description = '`*clear` - This command removes your set amount of messages. (Make sure to add 1 to the amount you want to remove.)\n`*warn` - This command is used to warn members.\n`*mute` - This command is used to mute members.\n`*unmute` - This command is used to unmute members.\n`*kick` - This command is used to kick members.\n`*ban` - This command is used to ban members.\n`*unban` - This command is used to unban members.\n`*nuke` - This command will completely wipe the channel you type it in.\n`*leave` - This command makes ModBot leave your server.\n\nFor the mute and unnmute commands to work, you need to already have a role named muted and setup permissions yourself. The command just gives and removes the role.\nFor welcome messages to work you need to have a channel named welcome and the bot will do the rest itself.\nFor logs to work, you need a channel named logs and the bot will handle the rest.'
    )
	await ctx.send(embed=embed)

@client.command(aliases=['commands', 'command', 'cmds', 'cmd', 'h'])
async def help(ctx):
	embed = discord.Embed(
		title = 'Help',
        colour = 0x38c3ff,
        description = '`*invite` - This command allows you to invite the bot to your server.\n`*ping` - This command sends you the current ping of this bot.\n`*quote` - This command will give you a random quote from a list.\n`*coin` - This command will flip a coin for you.\n`*rng` - This command will send a random number between 0-10\n`*create` - This command shows the creation date of a users account.\n`*eightball` - This command is a magic eight ball.\n`*help` - This command brings up this help menu.\n`*modhelp` - Help section for moderators.'
    )
	await ctx.send(embed=embed)

client.run('NzM3NzA4MjgwODQ3MTM4ODM3.XyBSYA.ddVCI0AqUPVLzzshrqdu-AuA4MY')