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
    args_to_funcs(args.info, d)
