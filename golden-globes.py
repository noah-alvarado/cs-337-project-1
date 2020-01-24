from presenters import get_presenters
from nominees import get_nominees
from winners import get_winners
from host import get_hosts
from awards import get_awards

import argparse


def args_to_funcs(args):
    func_map = {
        'hosts': get_hosts,
        'awards': get_awards,
        'winners': get_winners,
        'nominees': get_nominees,
        'presenters': get_presenters
    }

    if not args:
        args = func_map.keys()

    for arg in args:
        if arg not in func_map:
            err = f'\'{arg}\' is not a valid type of information!'
            raise ValueError(err)

        func = func_map.get(arg)
        print(func())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze tweets from the Golden Globes to find information about the '
                                                 'event.')
    parser.add_argument('-i', '--info', nargs='+', type=str, help='get specific information from the dataset')
    parser.add_argument('-y', '--year', nargs=1, type=int, help='use the dataset of a previous year')
    args = parser.parse_args()

    args_to_funcs(args.info)
