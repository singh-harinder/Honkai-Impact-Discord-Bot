import discord
from discord.ext import commands, tasks
from itertools import cycle
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
import time


statuses = cycle(['Honkai Impact 3'])


playlist_ID = {
    '3rdguy': 'UUdX9K1TQwZaoCWrYkG3Rk0Q',
    'marisa': 'UU0S7OwBRuCYyeZrM6dq9Ykg',
    'wyverein': 'UURsi-eA7IzvTkU3tqKcz9nQ',
    'yukinahime': 'UUo8ig5qW9ISJP_AnrVqYOww',
    'edwinjk': 'UUbXoYQp4Njc3dnyIsBaww6A',
    'vignette': 'UU4NSYsfffEc6abYQS5afPRQ',
    'satellizerx': 'UUKhLED79UBnoJLjAAcVj5nw',
    'furyproduction': 'UUU4xhPQufy3Ar0km8514eKg',
    'furtherbeyondgaming': 'UUltBd9gGKE6-ZkSuQ0jGntw',
    'mg': 'UUHmtPsuX6f7uavugk25kRTg',
    'justkirby': 'UUa7QAdy8FmnWUFHoyg1hE_A',
    'akayuki': 'UUxgSTa2iiO6heC-EnQDaqRg',
    'keebster': 'UUbXY6vNP0JzAkCdrWgjwvag',
    'milkssv': 'UUF1k7LIejtEDvb-PmCPPXwg',
    'nubskate': 'UUjnafxo93GIMAB9mQCRY2Hg',
    'honkaiglobal': 'UUko6H6LokKM__B03i5_vBQQ',
    'honkaisea': 'UU8O6WFO_0c51EB3FqAintyg',
    'whize': 'UU87RdGR6G0OrICOGVNqCaUQ'

}

community_ID = {
    '3rdguy': 'https://www.youtube.com/channel/UCdX9K1TQwZaoCWrYkG3Rk0Q/community',
    'marisa': 'https://www.youtube.com/channel/UC0S7OwBRuCYyeZrM6dq9Ykg/community',
    'furtherbeyondgaming': 'https://www.youtube.com/channel/UUltBd9gGKE6-ZkSuQ0jGntw/community',
    'furyproduction': 'https://www.youtube.com/channel/UUU4xhPQufy3Ar0km8514eKg/community',
    'honkaiglobal': 'https://www.youtube.com/channel/UUko6H6LokKM__B03i5_vBQQ/community',
    'edwinjk': 'https://www.youtube.com/channel/UUbXoYQp4Njc3dnyIsBaww6A/community',
    'wyverein': 'https://www.youtube.com/channel/UURsi-eA7IzvTkU3tqKcz9nQ/community',
    'vignette': 'https://www.youtube.com/channel/UU4NSYsfffEc6abYQS5afPRQ/community',
    'mg': 'https://www.youtube.com/channel/UUHmtPsuX6f7uavugk25kRTg/community',
    'akayuki': 'https://www.youtube.com/channel/UUxgSTa2iiO6heC-EnQDaqRg/community',
    'keebster': 'https://www.youtube.com/channel/UUbXY6vNP0JzAkCdrWgjwvag/community',
    'milkssv': 'https://www.youtube.com/channel/UUF1k7LIejtEDvb-PmCPPXwg/community',
    'nubskate': 'https://www.youtube.com/channel/UUjnafxo93GIMAB9mQCRY2Hg/community',
    'honkaisea': 'https://www.youtube.com/channel/UU8O6WFO_0c51EB3FqAintyg/community',
    'whize': 'https://www.youtube.com/channel/UC87RdGR6G0OrICOGVNqCaUQ/community'
}


youtube = build('youtube', 'v3', developerKey='Insert your API key here')

# VIDEOS GETTER TEMPLATE
def video_parser(uploads, results):
    channel_name = youtube.playlistItems().list(playlistId=uploads, part='snippet',
                                          maxResults=results).execute()

    videos_list = []
    for item in channel_name['items']:
        videos_list.append('http://youtube.com/watch?v=' + item['snippet']['resourceId']['videoId'])

    return videos_list


# VIDEO SEARCH FUNCTION
def search_video(playlist_id, search):
    videos_title = []
    videos_link = []

    next_Page_Token = None

    while 1:
        videos_list = youtube.playlistItems().list(playlistId=playlist_id,
                                                   part='snippet', maxResults=50,
                                                   pageToken=next_Page_Token).execute()

        for item in videos_list['items']:
            videos_link.append('http://youtube.com/watch?v=' + item['snippet']['resourceId']['videoId'])
            videos_title.append(item['snippet']['title'].encode(
                'ascii', 'ignore').decode('ascii').lower())

        next_Page_Token = videos_list.get('nextPageToken')

        if next_Page_Token is None:
            break

    search_result = [i for i, item in enumerate(videos_title) if search in item]

    final_video_list = []

    for item in search_result:
        final_video_list.append(videos_link[item])

    return final_video_list


# COMMUNITY FUNCTION TEMPLATE
def community_function(url):
    source = requests.get(url).text.encode('ascii', 'ignore').decode('ascii').replace("\n", "")

    soup = BeautifulSoup(source, 'lxml')

    community_list = []

    for part in soup.find_all('div', class_='comment-renderer-text-content'):
            res = part.text
            community_list.append(res)

    image_links = soup.find_all('img', class_='comment-image')
    img_list = []

    for link in image_links:
        img_link = link['src']
        img_list.append(img_link)

    rep = soup.find_all('a', class_='yt-uix-sessionlink')

    attachment = []
    for test in rep:
        attri = test['href']
        if 'redirect' in attri:
            x = attri.find('https')
            attri = attri[x:]
            y = attri.find('&')
            if y == -1:
                attri = attri.replace("%3A%2F%2F", "://")
                attri = attri.replace("%2F", "/")
                attachment.append(attri)
            else:
                attri = attri[:y]
                attri = attri.replace("%3A%2F%2F", "://")
                attri = attri.replace("%2F", "/")
                attachment.append(attri)

    return {
        'post' : community_list,
        'links' : img_list,
        'text_links': attachment
    }


# BOT BEGINS HERE
# DISCORD.PY
client = commands.Bot(command_prefix='.', help_command=None)

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(statuses)))

@client.event
async def on_ready():
    change_status.start()
    print('Bot is Running!')

@client.command()
async def hello(ctx,*,string):
    await ctx.send(string)


# THIS COMMAND RETIRVES AND POSTS THEM IN THE DISCORD
@client.command(aliases=['community', 'comm'])
async def channel_community(ctx, channel_name, number: int):
    if channel_name in community_ID:
        list = community_function(community_ID[channel_name])
        await ctx.send('__***Here are the requested community posts:***__')
        for k in range(number):
            if not list['post']:
                pass
            else:
                if not list['post'][k]:
                    pass
                else:
                    await ctx.send(list['post'][k])

            if not list['links']:
                pass
            else:
                if not list['links'][k]:
                    pass
                else:
                    await ctx.send(list['links'][k])

            if not list['text_links']:
                pass
            else:
                if not list['text_links'][k]:
                    pass
                else:
                    await ctx.send('**Here are the links in the Post:**')
                    await ctx.send(list['text_links'][k])
            time.sleep(1)
    else:
        await ctx.send("""`Channel Not found. Please use .help to get the list of supported Channels`""")


# THIS COMMAND SEARCHES FOR THE VIDEOS IN THE WHOLE CHANNEL AND RETRIEVES THEM WHICH MATCHES THE STRING
@client.command()
async def search(ctx, channel_name, number_of_results: int,  *,search_string):
    if channel_name in playlist_ID:
        list = search_video(playlist_ID[channel_name], search_string)
        await ctx.send('__***Here are all the matching videos I found according to your preferences:***__')
        if number_of_results == 0:
            for k in range(len(list)):
                await ctx.send(list[k])
        else:
            for k in range(number_of_results):
                await ctx.send(list[k])
    else:
        await ctx.send("""`Channel Not found. Please use .help to get the list of supported Channels`""")



# THIS COMMANDS RETRIVES AND POSTS VIDEOS IN THE DISCORD
@client.command(aliases=['videos'])
async def channel_videos(ctx, channel_name, results: int):
    if channel_name in playlist_ID:
        video_list = video_parser(playlist_ID[channel_name], results)
        await ctx.send('__***Here are your requested Videos:***__')
        for vid in video_list:
            await ctx.send(vid)
            time.sleep(1)
    else:
        await ctx.send("""`Channel Not found. Please use .help to get the list of supported Channels`""")



@client.command()
async def help(ctx):
    await ctx.send("""`NOTE: All commands are prefixed/begin with dot(.)

1) .videos(command): You can search and retrieve videos from the youtube channels.

Format: (.videos) (channel_name) (the_number_of_results_to_want)

Example: .videos marisa 2 -> This command will search the Marisa Honkai Channel and return to you the first 2 latest videos in the channel.

2) .search(command): You can search and retrieve any videos from the mentioned channel.

Format: (.search) (channel_name) (the_number_of_results_you_want) (search_string)

Example: .search marisa 2 Abyss -> This command will retrieve and return the two videos that match the word "Abyss". The videos returned are sorted by uploaded date with latest one being first. If you want all the videos matching the search_string then put (the_number_of_results_you_want) = 0

3) .community(command): You can retrieve the community posts from the channel.

Format: (.community) (channel_name) (number_of_posts)

Example: .community marisa 2 -> This will retrieve and return the latest top 2 posts from the community page and return them to you. The maximum value supported for (number_of_posts) = 5

Following are the Channel_names to access them with the bot.

CHANNELS LIST WITH NAMES: {

3rdguy                
marisa                
wyverein              
yukinahime            
edwinjk              
vignette              
satellizerx           
furyproduction        
furtherbeyondgaming   
mg     
justkirby             
akayuki               
keebster              
milkssv               
nubskate              
honkaiglobal          
honkaisea            
whize               
}

NOTE 2: Some Channels don't have community list so you won't get any results back.

If you encounter any problems with the Bot please mail them to 'kinggouken611@gmail.com'`""")


@channel_videos.error
async def check_error(ctx, error):
        await ctx.send("""`Command Error. Please Check the syntax!
        Format: (.videos) (channel_name) (the_number_of_results_to_want)
        Example: .videos marisa 2 -> This command will search the Marisa Honkai Channel and return to you the first 2 latest videos in the 
        channel.`
        """)



@channel_community.error
async def community_error(ctx, error):
        await ctx.send("""`Command Error. Please Check the syntax!
        Format: (.community) (channel_name) (number_of_posts)
        Example: .community marisa 2 -> This will retrieve and return the latest top 2 posts from the community page and return them to you. 
        The maximum value supported for (number_of_posts) = 5`
        """)



@search.error
async def search_error(ctx, error):
    await ctx.send("""`Command Error. Please Check the syntax!
            Format: (.search) (channel_name) (the_number_of_results_you_want) (search_string)
            Example: .search marisa 2 Abyss -> This command will retrieve and return the two videos that match the word "Abyss". The videos 
            returned are sorted by uploaded date with latest one being first. If you want all the videos matching the search_string then put
            (the_number_of_results_you_want) = 0`
            """)

client.run('Your Bot token goes here')
