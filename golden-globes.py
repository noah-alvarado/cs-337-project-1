from presenters import get_presenters
from nominees import get_nominees
from winners import get_winners
from host import get_host
from awards import get_awards

if __name__ == '__main__':
    print(get_host())
    print(get_awards())
    print(get_winners())
    print(get_nominees())
    print(get_presenters())
