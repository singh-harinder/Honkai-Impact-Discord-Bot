# Honkai-Impact-Discord-Bot

Depracated: This no longer works due to the updations in the youtube API

Link: https://discord.com/api/oauth2/authorize?client_id=712388775841366056&permissions=522304&scope=bot

This is a bot created in discord.py related to the game Honkai Impact 3. 
The Bot has following commands and features....

NOTE: All commands are prefixed/begin with dot(.)

1))      **.help(command)**: The help command. Will tell you the syntax and info about all the commands available.

Format: .help



2))      **.videos(command)**: You can search and retrieve videos from the youtube channels.

Format:           (*.videos*)    (*channel_name*)     (*the_number_of_results_to_want*)

Example:      **.videos marisa 2** -> This command will search the Marisa Honkai Channel and return to you the first 2 latest videos in the channel.





3))     **.search(command)**: You can search and retrieve any videos from the mentioned channel.

Format:          (*.search*)     (*channel_name*)      (*the_number_of_results_you_want*) (*search_string*)

Example:        **.search marisa 2 Abyss** -> This command will retrieve and return the two videos that match the word "Abyss". The videos returned are sorted by uploaded date with latest one being first.
If you want all the videos matching the search_string then put (*the_number_of_results_you_want*) = 0




4))      **.community(command)**: You can retrieve the community posts from the channel. 

Format:            (*.community*)     (*channel_name*)        (*number_of_posts*)

Example:           **.community marisa 2** -> This will retrieve and return the latest top 2 posts from the community page and return them to you.
The maximum value supported for (*number_of_posts*) = 5

You can also use .comm alias for this. Like , 	.comm marisa 1

NOTE 2: Community posts are returned in the following format. 
			
			{ Post text }
			{ Images in the Post }
			{ Any links Embedded into the Post }





Following are the Channel_name to access them with the bot. 


CHANNELS LIST WITH NAMES: {

3rdguy ->                  https://www.youtube.com/channel/UCdX9K1TQwZaoCWrYkG3Rk0Q

marisa ->                  https://www.youtube.com/channel/UC0S7OwBRuCYyeZrM6dq9Ykg

wyverein ->                https://www.youtube.com/channel/UURsi-eA7IzvTkU3tqKcz9nQ

yukinahime ->              https://www.youtube.com/channel/UCo8ig5qW9ISJP_AnrVqYOww

edwinjk ->                 https://www.youtube.com/channel/UUbXoYQp4Njc3dnyIsBaww6A

vignette ->                https://www.youtube.com/channel/UU4NSYsfffEc6abYQS5afPRQ

satellizerx ->             https://www.youtube.com/channel/UCKhLED79UBnoJLjAAcVj5nw

furyproduction ->          https://www.youtube.com/channel/UUU4xhPQufy3Ar0km8514eKg

furtherbeyondgaming ->     https://www.youtube.com/channel/UUltBd9gGKE6-ZkSuQ0jGntw

mg ->                      https://www.youtube.com/channel/UUHmtPsuX6f7uavugk25kRTg

justkirby ->               https://www.youtube.com/user/kkcomicproduction

akayuki ->                 https://www.youtube.com/channel/UUxgSTa2iiO6heC-EnQDaqRg

keebster ->                https://www.youtube.com/channel/UUbXY6vNP0JzAkCdrWgjwvag

milkssv ->                 https://www.youtube.com/channel/UUF1k7LIejtEDvb-PmCPPXwg

nubskate ->                https://www.youtube.com/channel/UUjnafxo93GIMAB9mQCRY2Hg

honkaiglobal ->            https://www.youtube.com/channel/UUko6H6LokKM__B03i5_vBQQ

honkaisea ->               https://www.youtube.com/channel/UU8O6WFO_0c51EB3FqAintyg

whize ->                   https://www.youtube.com/channel/UC87RdGR6G0OrICOGVNqCaUQ

}

NOTE 3: Some Channels don't have community list so you won't get any results back.

If you encounter any problems with the Bot please mail them to 'kinggouken611@gmail.com'
