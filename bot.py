import discord
import crawling

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("League of Legends")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("ㅇㅇ")
    if message.content.startswith("순위"):
        rank_list = crawling.SearchRank()
        embed = discord.Embed(title="LCK순위", color=0x00ff56)
        for i in range(len(rank_list)):
            embed.add_field(name=str(i + 1) + "등", value=rank_list[i], inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 DRX"):
        team_info = crawling.SearchMatching("DRX")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 DWG"):
        team_info = crawling.SearchMatching("DWG")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 GEN"):
        team_info = crawling.SearchMatching("GEN")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 T1"):
        team_info = crawling.SearchMatching("T1")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 AF"):
        team_info = crawling.SearchMatching("AF")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 KT"):
        team_info = crawling.SearchMatching("KT")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 SB"):
        team_info = crawling.SearchMatching("SB")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 DYN"):
        team_info = crawling.SearchMatching("DYN")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 HLE"):
        team_info = crawling.SearchMatching("HLE")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("전적 SP"):
        team_info = crawling.SearchMatching("SP")
        embed = discord.Embed(title="최근 전적", color=0x00ff56)
        embed.add_field(name=team_info[0] + " VS " + team_info[3], value=team_info[1] + ":" + team_info[2],
                        inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("전적"):
        embed = discord.Embed(title="전적", color=0x00ff56)
        embed.add_field(name="검색 방법", value="전적 '팀이름'", inline=False)
        embed.set_footer(text="관련 명령어: 팀 목록")
        await message.channel.send(embed=embed)

    if message.content.startswith("팀 목록"):
        embed = discord.Embed(title="전적 확인방법", color=0x00ff56)
        embed.add_field(name="DRX", value="전적 DRX", inline=True)
        embed.add_field(name="DWG", value="전적 DWG", inline=True)
        embed.add_field(name="GEN", value="전적 GEN", inline=True)
        embed.add_field(name="T1", value="전적 T1", inline=True)
        embed.add_field(name="AF", value="전적 AF", inline=True)
        embed.add_field(name="KT", value="전적 KT", inline=True)
        embed.add_field(name="SB", value="전적 SB", inline=True)
        embed.add_field(name="DYN", value="전적 DYN", inline=True)
        embed.add_field(name="HLE", value="전적 HLE", inline=True)
        embed.add_field(name="SP", value="전적 SP", inline=True)
        await message.channel.send(embed=embed)


client.run("NzM4MjQ3NDA0OTY0MjgyNDI4.XyJIeQ.mo6xmPs9Lmo_1EwRi1koqY1wMio")
