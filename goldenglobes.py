from data import GGData
from presenters import get_presenters_helper
from nominees import get_nominees_helper
from winners import get_winners_helper
from host import get_hosts_helper
from awards import get_awards_helper
from reference import AWARDS_LISTS
from reactions import gg_reactions

import argparse


def args_to_funcs(args, data):

    gg_reactions.reset()

    func_map = {
        'hosts': get_hosts_helper,
        'awards': get_awards_helper,
        'winners': get_winners_helper,
        'nominees': get_nominees_helper,
        'presenters': get_presenters_helper
    }

    return_values = dict()

    if not args:
        args = func_map.keys()

    for arg in args:
        if arg not in func_map:
            err = f'\'{arg}\' is not a valid type of information!'
            raise ValueError(err)

        func = func_map.get(arg)
        # print(func(data))

        if arg == 'presenters':
            return_values[arg] = func(data, AWARDS_LISTS)
        elif arg == 'winners':
            return_values[arg] = func(data, AWARDS_LISTS)
        elif arg == 'hosts':
            return_values[arg] = func(data)
        else:
            return_values[arg] = func(data)

        print(return_values[arg])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze tweets from the Golden Globes to find information about the '
                                                 'event.')
    parser.add_argument('-i', '--info', nargs='+', type=str, help='get specific information from the dataset')
    parser.add_argument('-f', '--file', nargs=1, type=int, help='specify tweets file to parse')
    args = parser.parse_args()

    tweets = GGData()
    args_to_funcs(args.info, tweets)

# reputable news outlets:
# Golden Globe Awards: "user":"goldenglobes","user_id":"18667907" 5 tweets
#  the rest are useless :( vague promos about red carpet styles and afterparties :(
#  "No one makes Golden Global hits like @eltonofficial, so its only right @rocketmanmovie is nominated for tonight's #GoldenGlobes! The question is... will it win? (Gif via @GIPHY) https://t.co/KWnaHM3gLe"
#
# ABC News: "user":"abcnews","user_id":"2768501", 8 tweets
#  "Golden Globes: Here's where you can find all the winners of every category https://t.co/dOME3POoDa"
#  "From Ricky Gervais's warning to Joaquin Phoenix's F-bomb: All the key moments from the Golden Globes https://t.co/Srb7G8aEO1"
#
# Deadline Hollywood: "user":"DEADLINE","user_id":"586032653", 81 tweets
#  "‘1917’ Caps Golden Globes Double With Best Film Drama Win: Sam Mendes “Optimistic” About Theatrical In Face Of Streaming &amp; Fewer Studios https://t.co/XLLW2aUaYg https://t.co/TPsxOdZ8IW"
#  "‘Once Upon A Time In Hollywood’ Wins Three Golden Globes; Producer David Heyman Calls Tarantino “Maestro” https://t.co/nQiqkG5AEU https://t.co/aEa4vW3Ffl"
#  "Golden Globe Winner Quentin Tarantino On Wrapping Up His Movie Resume: “There Is An Umbilical Cord Link Between The 10th Film &amp; ‘Reservoir Dogs'” https://t.co/OcfhXemthG https://t.co/1YeiKv74mM"
#  "Golden Globes TV Review: Ricky Gervais’ Return Flounders On Night Of Big Wins For ‘1917’, ‘Once Upon A Time In Hollywood’, ‘Succession’ &amp; ‘Fleabag’ https://t.co/yRgQSrzKwc https://t.co/KNO5bdWKBD"
#  "Renée Zellweger Wins First Golden Globe In 16 Years For ‘Judy,’ Thanking Those Who Have Reminded Her That “The Top Doesn’t Matter” https://t.co/WlQFbbd1wQ https://t.co/ehx15OzMRL"
#  "#Rocketman star Taron Egerton picked up his first-ever Golden Globes award for his portrayal of the legendary crooner Elton John #GoldenGlobes https://t.co/skwVces55C"
#  "On Sunday, Awkwafina became the first actress of Asian-American descent to win a Golden Globe in the Best Motion Picture, Musical or Comedy category #GoldenGlobes https://t.co/dowrZbHqg3"
#  "Tom Hanks delivered the goods in accepting the Cecil B. DeMille Award at Sunday’s #GoldenGlobes https://t.co/KBLCCKrG51"
#  {"_id":{"$oid":"5e1934ac174f9084edc22262"},"user_id":"586032653","text":"WINNER! 1917 | Best Motion Picture, Drama https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/unjhHispz5"
#  "WINNER! Joaquin Phoenix | Best Actor, Motion Picture, Drama https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/8VA4rA2cT7"
#  "“I had money on this not happening,” said a “completely stumped” Olivia Colman tonight as she scooped her third Golden Globe https://t.co/z1ARtJO9lr"
#  "WINNER! \"Once Upon a Time in Hollywood\" | Best Motion Picture, Musical or Comedy https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/W31B1DzZ7F"
#  "Quentin Tarantino took home his third career Golden Globe Sunday night | #GoldenGlobes https://t.co/Ikjascqf08"
#  "In one of the biggest surprises of tonight’s #GoldenGlobes ceremony, '1917' helmer Sam Mendes won the award for Best Director of a Motion Picture https://t.co/oMuLpQz2Lq"
#  "WINNER! Awkwafina | Best Actress, Motion Picture, Musical or Comedy https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/EF8qapL8LD"
#  "WINNER! Taron Egerton | Best Actor, Motion Picture, Musical or Comedy https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/ClIibux0mk"
#  "WINNER! Brad Pitt | Best Supporting Actor, Motion Picture https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/7YFX2Kj6m2"
#  "Elton John and Bernie Taupin finally share an award #GoldenGlobes https://t.co/JBAiV7zfmC"
#  "WINNER! Chernobyl | Best Limited Series or TV Movie https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/vSHVxzrdKC"
#  "WINNER! Michelle Williams | Best Actress, Limited Series or Movie https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/siuf58IgT0"
#  "WINNER! Sam Mendes | Best Director, Motion Picture https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/qMV3a5T2b9"
#  "Brian Cox landed the Best Actor in a TV Series – Drama statuette Sunday night for his performance in season 2 of HBO’s critically praised drama series #Succession https://t.co/baJBX1Hjaj
#  "WINNER! Olivia Colman | Best Actress - TV Series, Drama https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/0im4e38nOh"
#  "Phoebe Waller-Bridge was once again the belle of the ball after Fleabag scored a #GoldenGlobes double https://t.co/F1Z7uooIQQ"
#  "WINNER! Patricia Arquette | Best Supporting Actress, Limited Series or Musical https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/4cWUbpO1LX"
#  "Awards season darling #Parasite added to its haul tonight with the #GoldenGlobes for Best Foreign Language Film https://t.co/d2mrIksjbT"
#  "WINNER! \"I'm Gonna Love Me Again\" from Rocketman | Best Original Song https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/nKgiL4Grkk"
#  "WINNER! Fleabag | Best TV Series, Musical or Comedy https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/WEuJ14UBLf"
#  "WINNER! Laura Dern | Best Supporting Actress, Motion Picture https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/Jig6E1ERLn"
#  "WINNER! Missing Link | Best Animated Film https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/NqMgyZszhI"
#  "WINNER! Quentin Tarantino for \"Once Upon A Time...In Hollywood\" | Best Screenplay, Motion Picture https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/nanwfwXmjp"
#  "WINNER! Brian Cox | Best Actor, TV Series, Drama https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/JXy2KYc1CR"
#  "#Succession creator Jesse Armstrong lauded the dark HBO family drama as a “team show” after winning its first #GoldenGlobes https://t.co/EYk0cRixPf"
#  "Ramy Youssef took home the #GoldenGlobes award Sunday night in the Best Performance by an Actor in a Television Series – Musical or Comedy for his role in the Hulu series 'Ramy' https://t.co/slP7Lq7GIr"
#  "WINNER! Parasite | Best Foreign Language Film https://t.co/0MFSKkzKE8 | #GoldenGlobes https://t.co/waJkW15RQI"
#  "WINNER!  Phoebe Waller Bridge | Best Actress - TV Series, Musical or Comedy https://t.co/0MFSKkzKE8 https://t.co/s1Rz9vFaYB"
#  "A big win for Succession, which became a huge water cooler show in its second season.\" #GoldenGlobes | https://t.co/rY9x1XbQez https://t.co/RVjljHedsy"
#  "WINNER! Succession | Best TV Series, Drama https://t.co/0MFSKkzKE8 https://t.co/3j9874KrQp"
#  "WINNER! Russell Crowe | Best Actor - Limited Series or TV Movie https://t.co/0MFSKkzKE8 https://t.co/raULgU8gVU"
#  "WINNER! Ramy Youssef | Best Actor - TV series, musical or comedy https://t.co/0MFSKkzKE8 https://t.co/HxuslMEaZT"
#
# E! News: "user":"enews","user_id":"2883841", 134 tweets
#  "Alex Rodriguez's Sweet Note to Jennifer Lopez After Her Golden Globes Loss Proves He's Her No. 1 Fan https://t.co/VrlE2YkfOf"
#  "Awkwafina Has a Message For Her Dad After Historic 2020 Golden Globes Win https://t.co/yvLlXwIgJ9"
#  "Joey King's Golden Globes Dress Is a Work Of Art Worthy of a Best Actress Nominee https://t.co/ST8JdVZAQR"
#  "Awkwafina Wins Best Actress in a Comedy Film for The Farewell at Her First Golden Globes https://t.co/2YIfo0Xt5d"
#  "Olivia Colman Wins Best Actress in a Drama at the 2020 Golden Globes, Admits to Getting \"a Little Boozy\" https://t.co/MXCD9niznP"
#  "Joaquin Phoenix Tells Rooney Mara \"I Love You\" After Winning Best Actor at the 2020 Golden Globes https://t.co/u0pvtxcVzu"
#  "Once Upon a Time in Hollywood Wins Best Picture Musical or Comedy at 2020 Golden Globes https://t.co/2EipW5fppI"
#  "ICYMI: Taron Egerton took home his first #GoldenGlobe award. And ICYMI: His dedication to Elton John had us like 😭. https://t.co/CsKGZpcloK https://t.co/rGPCRoT1Bg"
#  "Succession Wins Best TV Series, Drama, at the 2020 Golden Globes https://t.co/VFaorM6GwP"
#  "1917 Wins Best Motion Picture, Drama at the 2020 Golden Globes https://t.co/WIVLgk6Q4S"
#  "Phoebe Waller-Bridge gave a special shout-out to Obama during her #GoldenGlobes speech and it was everything. https://t.co/ohlu7SCbks"
#  "Congrats to Ramy Youssef on his first-ever #GoldenGlobe win! https://t.co/tpesZoLvTn"
#  "CONGRATS to the cast &amp; crew of #1917, the Best Motion Picture, Drama at this year's #GoldenGlobes. Catch up on all the winners: https://t.co/lH21iVowYx https://t.co/8tLuTQ5bMi"
#  "Chernobyl Wins Best Limited Series at the 2020 Golden Globes https://t.co/DrMvLE5xOv"
#  "Congratulations to Brian Cox after receiving his first #GoldenGlobe award for the Successor! https://t.co/6NQHuswGbZ"
#  "The only thing greater than Stellan Skarsgård's win at the #GoldenGlobes? His praise of Colin Farrell's eyebrows during his speech.  https://t.co/VmAem0U6i0"
#  "“I'm free, and don't you know? Oh-oh-oh, I'm gonna love me again.” (I'm Gonna) Love Me Again wins Best Original Song from #Rocketman. #GoldenGlobes https://t.co/mxIxHcVEWq https://t.co/bspPFsRWBv"
#  "Welcome to the stage the creators of #Parasite, winner of Best Foreign Language Film. #GoldenGlobes https://t.co/lmi4jmsUdj https://t.co/p70DTztTt6"
#  "The only thing that could top our love of #Fleabag? Our love for Phoebe Waller-Bridge. Who just happens to be the winner of Best Actress in a TV Series, Comedy. #GoldenGlobes https://t.co/YHT4yE2cWm https://t.co/rTc2OkotSY"
#  "While we have to wait until Sunday to see if J.Lo takes home a #GoldenGlobe, take a second to revisit Jenny from the past in her first-ever Golden Globes interview with E! https://t.co/A2WFDP6buh https://t.co/DMlxJmF9vg"
#
# Entertainment Tonight: "user":"etnow","user_id":"23603092", 66 tweets
#  "Ricky Gervais is pledging that this is his LAST time hosting the #GoldenGlobes — do we believe him though?! \nhttps://t.co/xi6qnYHpAE"
#  "Awkwafina shares what it means to be the 1st Asian-American woman to win a #GoldenGlobe for Best Actress in a Motion Picture. https://t.co/kI2kxCG7o6"
#  "Joaquin Phoenix's #GoldenGlobes acceptance speech left some scratching their heads. https://t.co/hBlFqzBEem"
#  "Brad Pitt won his third Golden Globe! #GoldenGlobes https://t.co/CsSyCvMRwV"
#  "#Rocketman took it home! #GoldenGlobes https://t.co/E1w9dFLptj"
#  "From Jennifer Aniston supporting Brad Pitt during his speech, to Tom Hanks bringing everyone to tears, here's a complete #GoldenGlobes recap https://t.co/HGQJQNQ0gT"
#  "Golden Globes: #Succession takes home award for Best Drama Series #GoldenGlobes #goldenglobes2020 https://t.co/287nMDrNXv"
#
# Entertainment Weekly: "user":"EW", "user_id":"16312576", 75 tweets
#  "Taron Egerton was emotional and charmingly earnest after his #GoldenGlobes win. \nhttps://t.co/BAPVCXiZrd"
#  "Phoebe Waller-Bridge’s #GoldenGlobes win came with a very special “Thanks, Obama!”\nhttps://t.co/x3KlXKKwR0"
#  "Awkwafina's #GoldenGlobes win is a big moment for Hollywood. https://t.co/5F5VvHxW38"
#  "1917 wins Best Drama at Golden Globes https://t.co/1hbpaU6YtK"
#  "Once Upon a Time in Hollywood wins Best Picture — Comedy or Musical at Golden Globes https://t.co/qhJQVR8jeg"
#  "The Farewell star Awkwafina wins Golden Globe for Best Actress in a Comedy https://t.co/2mDuDEz46L"
#  ".@1917 wins Best Motion Picture, Drama! #GoldenGlobes \n\nSee all of tonight's #GoldenGlobes winners: https://t.co/oyrr3IVxEb https://t.co/JuSYzlvoFU"
#  "Renée Zellweger wins Best Performance by an Actress in a Motion Picture, Drama for @JudyGarlandFilm! \n\nAll of tonight's #GoldenGlobes winners: https://t.co/oyrr3IDWfB https://t.co/AJcfEsqHt8"
#  "Brad Pitt wins Golden Globe, tells Leonardo DiCaprio he would have saved him in Titanic https://t.co/JmVoltQMNR"
#  ".@OnceInHollywood wins Best Motion Picture, Musical or Comedy!\n\nYou can see all of tonight's #GoldenGlobes winners here: https://t.co/oyrr3IDWfB https://t.co/XdwsqLLdNp"
#  "Taron Egerton wins Golden Globe for Best Actor in a Musical or Comedy https://t.co/rM4tBhYNOd"
#  "Brad Pitt wins Best Performance by an Actor in a Supporting Role in any Motion Picture for @OnceInHollywood!\n\nSee all of tonight's #GoldenGlobes winners: https://t.co/oyrr3IDWfB https://t.co/XZczJciXi4",
#  "1917 director Sam Mendes wins first Golden Globe since American Beauty https://t.co/WNq1x4bt5G"
#  "Sam Mendes wins Best Director for @1917! \n\nSee all of tonight's #GoldenGlobes winners here: https://t.co/oyrr3IDWfB https://t.co/CBCsJf2gwP"
#  ".@PattyArquette wins Best Performance by an Actress in a Supporting Role in a Series, Limited Series or Motion Picture Made for Television! \n\nSee all of tonight's #GoldenGlobes winners: https://t.co/oyrr3IDWfB"
#  "Fleabag wins Best Comedy Series at Golden Globes https://t.co/H9aFtJoJ0N"
#  "‘(I’m Gonna) Love Me Again’ from @RocketmanMovie wins Best Original Song, Motion Picture!\n\nSee all of tonight's #GoldenGlobes winners: https://t.co/oyrr3IDWfB https://t.co/v0FpBm2Rfx"
#  "Succession star Brian Cox apologizes for winning Best Actor in a TV Drama at Golden Globes https://t.co/wKJdEJK4EC"
#  "Brian Cox wins Best Performance by an Actor in a Television Series, Drama for #SuccessionHBO!\n\nSee all of tonight's #GoldenGlobes winners here: https://t.co/oyrr3IDWfB https://t.co/g5d3Enb49F"
#  "Phoebe Waller-Bridge wins Best Performance by an Actress in a Television Series, Musical or Comedy for @Fleabag! \n\nSee all of tonight's #GoldenGlobes winners: https://t.co/oyrr3IDWfB https://t.co/eJvzBU5xjE"
#  "Succession wins best TV drama at Golden Globes https://t.co/0nhVjBxjQ2"
#  "Ramy Youssef wins Golden Globe for Best Actor in a TV Comedy: 'I know you guys haven't seen my show' https://t.co/9cxkmWaF6D"
#  "#SuccessionHBO wins Best Television Series, Drama!\n\nFollow along here for all of tonight's #GoldenGlobes winners: https://t.co/oyrr3IDWfB https://t.co/5kfLkMUaRP"
#  "Russell Crowe's stunning transformation into Roger Ailes lands him Best Actor in Limited Series Golden Globe https://t.co/ZfcfyEo37f",
#  ".@Ramy wins Best Performance by an Actor in a Television Series, Musical or Comedy for #Ramy! \n\nSee all the #GoldenGlobes winners here: \nhttps://t.co/oyrr3IDWfB https://t.co/XYcj45yuw1",
#
# Good Morning America: "user":"GMA","user_id":"22650211", 22 tweets
#  "Awkwafina made history at #GoldenGlobes as the first woman of Asian descent to win best actress - musical or comedy. https://t.co/d02Lt8AM7L"
#  "Brad Pitt cracked some jokes when he won the best supporting actor at the #GoldenGlobes for his role in \"Once Upon a Time in Hollywood.\" https://t.co/nJvjVPgcQy"
#  "Michelle Williams devotes #GoldenGlobes acceptance speech to a woman's right to choose. https://t.co/BczQ3NUeJW"
#  Tom Hanks was overcome with emotion talking about his family while accepting this year's Cecil B. deMille Award at the #GoldenGlobes. https://t.co/0AQ7bEsXRv"
#
# Huffington Post: "user":"HuffPost","user_id":"14511951", 41 tweets
#  "Awkwafina is the first Asian-American to win a Golden Globe Award for best actress in a musical or comedy film for her role in “The Farewell.” https://t.co/005I2QAQyq"
#  "Renée Zellweger’s star was officially reborn when she took home a Golden Globe for her portrayal of Judy Garland in the biopic “Judy.” #GoldenGlobes https://t.co/UOqsamMaUQ"
#  "This was also Awkwafina’s first Golden Globe nomination. #GoldenGlobes https://t.co/VP60WxUuk5"
#  "Tom Hanks brought the audience to its feet after receiving the Cecil B. DeMille lifetime achievement award at the 77th annual #GoldenGlobes. https://t.co/l8aJ3MaHVN"
#  "Once upon a time in Hollywood, Brad Pitt finally won a much-deserved Golden Globe. #GoldenGlobes https://t.co/X8DBMsCr9Z"
#
# IMDb: "user":"IMDb", "user_id":"17602896", 6 tweets
#  "From Pitt to #Parasite, we have the complete list of #GoldenGlobes winners here 👉 https://t.co/rjoDsWvDWH #Sponsored by @DolittleMovie https://t.co/pUvW2BNMII"
#
# MTV: "user":"MTV", "user_id":"2367911", 8 tweets
#  ".@tomhanks' #GoldenGlobes acceptance speech reminded us to always be on time: https://t.co/IKMxT32kSi 👏 https://t.co/q0lXYaIA3q"
#  "Phoebe Waller-Bridge's #GoldenGlobes acceptance speech was... FLAWLESS: https://t.co/eahDOw5n7n 😘👌 https://t.co/1qlfQigB0y"
#
# MTV News: "user":"MTVNEWS","user_id":"40076725", 33 tweets
#  ".@PattyArquette used her #GoldenGlobes speech to make an impassioned plea to Americans in 2020: \"For our kids and their kids, we have to vote in 2020\" \nhttps://t.co/ZtjFXY1q36"
#
# NBC Entertainment: "user":"nbc","id":"1214045047257067521"
# People: "user":"people","id":"1214031008242249728"
# Rotten Tomatoes: "user":"RottenTomatoes","id":"1214009260213846017"
# The Hollywood Reporter: "user":"THR","id":"1214036145115414528"
# TMZ: "user":"TMZ","id":"1213997091225128960"
# Twitter Movies: "user":"TwitterMovies","id":"1214029961264345088"
# US Weekly: "user":"usweekly","id":"1213144248016658435"
# Vanity Fair: "user":"VanityFair","id":"1214005475601203201"
# Variety: "user":"Variety","id":"1214004494540820480"
#
