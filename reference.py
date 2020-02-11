REACTIONS = ['mad', 'upset', 'happy', 'sad', 'good', 'bad', 'funny', 'cool', 'awful', 'terrible']

PRESENTER_NOISE = [
    'annual',
    'golden',
    'globes',
    'globe',
    'awards',
    'award',
    'tv',
    'television',
    'series'
    'motion',
    'picture',
    'when',
    'fashion',
    'dressed',
    'best',
    'fitness'
]

WINNER_NOISE = [
    'annual',
    'golden',
    'globes',
    'globe',
    'awards',
    'award',
    # 'tv',
    # 'television',
    # 'motion',
    # 'picture',
    'when'
]


# { award : [
#       [words in the tweet],
#       [words not in the tweet],
#       [at least one word in the tweet]
#   ]}
AWARDS_LISTS = {
    'carol burnett award for lifetime achievement in television': [
        ['award'],
        [],
        ['carol', 'burnett']
    ],
    'cecil b. demille award': [
        ['award'],
        [],
        ['cecil', 'demille']],
    'best motion picture - drama': [ #
        ['best', 'drama'],
        ['actor', 'actress', 'television', 'tv', 'series'],
        ['picture', 'film', 'feature']],
    'best performance by an actress in a motion picture - drama': [ #
        ['best', 'actress', 'drama'],
        ['television', 'tv', 'series', 'supporting', 'comedy', 'musical'],
        ['picture', 'film', 'feature']],
    'best performance by an actor in a motion picture - drama': [ #
        ['best', 'actor', 'drama'],
        ['television', 'tv', 'series', 'supporting', 'comedy', 'musical'],
        ['picture', 'film', 'feature']],
    'best motion picture - comedy or musical': [ #
        ['best', 'comedy', 'musical'],
        ['actor', 'actress', 'television', 'tv', 'series'],
        ['picture', 'film', 'feature']],
    'best performance by an actress in a motion picture - comedy or musical': [ #
        ['best', 'actress', 'comedy', 'musical'],
        ['actor', 'television', 'drama', 'supporting', 'tv', 'series'],
        ['picture', 'film', 'feature']],
    'best performance by an actor in a motion picture - comedy or musical': [ #
        ['best', 'actor', 'comedy', 'musical'],
        ['actress', 'television', 'drama', 'supporting', 'tv', 'series'],
        ['picture', 'film', 'feature']],
    'best animated feature film': [ #
        ['best', 'animated'],
        ['tv', 'television', 'series', 'actor', 'actress'],
        ['picture', 'film', 'feature']],
    'best foreign language film': [ #
        ['best', 'foreign', 'language'],
        ['tv', 'television', 'series', 'actor', 'actress'],
        ['picture', 'film', 'feature']],
    'best performance by an actress in a supporting role in a motion picture': [ #
        ['best', 'actress', 'supporting'],
        ['tv', 'television', 'series', 'actor'],
        ['picture', 'film', 'feature']],
    'best performance by an actor in a supporting role in a motion picture': [ #
        ['best', 'actor', 'supporting'],
        ['tv', 'television', 'series', 'actress'],
        ['picture', 'film', 'feature']],
    'best director - motion picture': [ #
        ['best', 'director'],
        ['tv', 'television', 'series', 'actor', 'actress'],
        ['picture', 'film', 'feature']],
    'best screenplay - motion picture': [ #
        ['best', 'screenplay'],
        ['tv', 'television', 'series', 'actor', 'actress'],
        ['picture', 'film', 'feature']],
    'best original score - motion picture': [ #
        ['best', 'score'],
        ['tv', 'television', 'series', 'actor', 'actress'],
        ['picture', 'film', 'feature']],
    'best original song - motion picture': [ #
        ['best', 'song'],
        ['tv', 'television', 'series', 'actor', 'actress'],
        ['picture', 'film', 'feature']],
    'best television series - drama': [ #
        ['best', 'drama'],
        ['actor', 'actress', 'film', 'feature', 'comedy', 'musical'],
        ['television', 'tv', 'series']],
    'best performance by an actress in a television series - drama': [ #
        ['best', 'actress', 'drama'],
        ['actor', 'picture', 'film', 'comedy', 'musical', 'supporting'],
        ['television', 'tv', 'series']],
    'best performance by an actor in a television series - drama': [ #
        ['best', 'actor', 'drama'],
        ['actress', 'picture', 'film', 'comedy', 'musical', 'supporting'],
        ['television', 'tv', 'series']],
    'best television series - comedy or musical': [ #
        ['best', 'comedy', 'musical'],
        ['actor', 'actress', 'picture', 'film', 'drama'],
        ['television', 'tv', 'series']],
    'best performance by an actress in a television series - comedy or musical': [ #
        ['best', 'actress', 'comedy', 'musical'],
        ['actor', 'picture', 'film', 'drama', 'supporting'],
        ['television', 'tv', 'series']],
    'best performance by an actor in a television series - comedy or musical': [ #
        ['best', 'actor', 'comedy', 'musical'],
        ['actress', 'picture', 'film', 'drama', 'supporting'],
        ['television', 'tv', 'series']],
    'best mini-series or motion picture made for television': [ #
        ['best'],
        ['actor', 'actress'],
        ['mini', 'mini-series', 'limited']],
    'best performance by an actress in a mini-series or motion picture made for television': [ #
        ['best', 'actress'],
        ['supporting', 'actor'],
        ['mini', 'mini-series', 'limited']],
    'best performance by an actor in a mini-series or motion picture made for television': [ #
        ['best', 'actor'],
        ['supporting', 'actress'],
        ['mini', 'mini-series', 'limited']],
    'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television': [
        ['best', 'actress', 'supporting'],
        ['actor', 'film', 'feature'],
        ['mini', 'mini-series', 'limited', 'television', 'tv', 'series']],
    'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television': [
        ['best', 'actor', 'supporting'],
        ['actress', 'film', 'feature'],
        ['mini', 'mini-series', 'limited', 'television', 'tv', 'series']
    ]}