from presenters import get_presenters
from nominees import get_nominees
from winners import get_winners
from host import get_hosts
from awards import get_awards
from data import GGData

import argparse


def args_to_funcs(arguments, data):
    func_map = {
        'hosts': get_hosts,
        'awards': get_awards,
        'winners': get_winners,
        'nominees': get_nominees,
        'presenters': get_presenters
    }

    if not arguments:
        arguments = func_map.keys()

    for arg in arguments:
        if arg not in func_map:
            err = f'\'{arg}\' is not a valid type of information!'
            raise ValueError(err)

        func = func_map.get(arg)
        print(func(data))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze tweets from the Golden Globes to find information about the '
                                                 'event.')
    parser.add_argument('-i', '--info', nargs='+', type=str, help='get specific information from the dataset')
    parser.add_argument('-f', '--file', nargs=1, type=str, help='specify location of the json file containing tweets')
    args = parser.parse_args()

    d = GGData(args.file)
    args_to_funcs(args.info, d)\

# reputable news outlets:
# Golden Globe Awards: "user":"goldenglobes","id":"1214036660305817600"
# ABC News: "user":"abcnews","id":"1214011891925733376"
# Deadline Hollywood: "user":"DEADLINE","id":"1214005309259169793"
# E! News: "user":"enews","id":"1214010782956040192"
# Entertainment Tonight: "user":"etnow","id":"1213164371217723392"
# Entertainment Weekly: "user":"EW","id":"1213996984937459712"
# Good Morning America: "user":"GMA","id":"1213077705706680320"
# Huffington Post: "user":"HuffPost","id":"1213174711791820800"
# IMDb: "user":"IMDb","id":"1213565772020305920"
# MTV: "user":"MTV","id":"1214041643579531265"
# MTV News: "user":"MTVNEWS","id":"1214029399760285697"
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
