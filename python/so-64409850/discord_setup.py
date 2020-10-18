@bot.command()
async def load(ctx, extension):
    id = str(ctx.author.id)
    if id == '721029142602056328':
        bot.load_extension(f'cogs.{extension}')
        print(f'Specified cog {extension} loaded!')
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 237, 76)
        )

        embed.add_field(name='Cog Loaded', value=f"Specified cog {extension} loaded by {author}.", inline=False)

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 237, 76)
        )

        embed.add_field(name="You can't do this!", value=f"You can't load the {extension} cog.", inline=False)

        await ctx.send(embed=embed)

@bot.command()
async def unload(ctx, extension):
    id = str(ctx.author.id)
    if id == '721029142602056328':
        bot.unload_extension(f'cogs.{extension}')
        print(f'Specified cog {extension} unloaded!')
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 237, 76)
        )

        embed.add_field(name='Cog Unloaded', value=f"Specified cog {extension} unloaded by {author}.", inline=False)

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 237, 76)
        )

        embed.add_field(name="You can't do this!", value=f"You can't unload the {extension} cog.", inline=False)

        await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
