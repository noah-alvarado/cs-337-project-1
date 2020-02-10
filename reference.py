PRESENTER_NOISE = [
    'annual',
    'golden',
    'globes',
    'globe',
    'awards',
    'award',
    'tv',
    'television',
    'motion',
    'picture',
    'when',

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
    'best motion picture - drama': [
        ['best', 'drama'],
        ['actor', 'actress', 'television'],
        ['motion', 'picture']],
    'best performance by an actress in a motion picture - drama': [
        ['best', 'actress', 'drama'],
        ['television'],
        []],
    'best performance by an actor in a motion picture - drama': [
        ['best', 'actor', 'drama'],
        ['television'],
        []],
    'best motion picture - comedy or musical': [
        ['best', 'comedy', 'musical'],
        ['actor', 'actress', 'television'],
        ['motion', 'picture']],
    'best performance by an actress in a motion picture - comedy or musical': [
        ['best', 'actress', 'comedy', 'musical'],
        [],
        []],
    'best performance by an actor in a motion picture - comedy or musical': [
        ['best', 'actor', 'comedy', 'musical'],
        [],
        []],
    'best animated feature film': [
        ['best', 'animated'],
        [],
        []],
    'best foreign language film': [
        ['best', 'foreign'],
        [],
        []],
    'best performance by an actress in a supporting role in a motion picture': [
        ['best', 'actress', 'supporting'],
        ['television', 'tv'],
        []],
    'best performance by an actor in a supporting role in a motion picture': [
        ['best', 'actor', 'supporting'],
        ['television', 'tv'],
        []],
    'best director - motion picture': [
        ['best', 'director'],
        [],
        []],
    'best screenplay - motion picture': [
        ['best', 'screenplay'],
        [],
        []],
    'best original score - motion picture': [
        ['best', 'score'],
        [],
        []],
    'best original song - motion picture': [
        ['best', 'song'],
        [],
        []],
    'best television series - drama': [
        ['best', 'drama'],
        ['actor', 'actress'],
        []],
    'best performance by an actress in a television series - drama': [
        ['best', 'actress', 'drama'],
        [],
        ['television', 'tv', 'series']],
    'best performance by an actor in a television series - drama': [
        ['best', 'actor', 'drama'],
        [],
        ['television', 'tv', 'series']],
    'best television series - comedy or musical': [
        ['best', 'comedy', 'musical'],
        ['actor', 'actress'],
        ['television', 'tv', 'series']],
    'best performance by an actress in a television series - comedy or musical': [
        ['best', 'actress', 'comedy', 'musical'],
        [],
        ['television', 'tv', 'series']],
    'best performance by an actor in a television series - comedy or musical': [
        ['best', 'actor', 'comedy', 'musical'],
        [],
        ['television', 'tv', 'series']],
    'best mini-series or motion picture made for television': [
        ['best'],
        ['actor', 'actress'],
        ['mini', 'series', 'mini-series', 'television', 'tv']],
    'best performance by an actress in a mini-series or motion picture made for television': [
        ['best', 'actress'],
        [],
        ['mini', 'series', 'mini-series', 'television', 'tv']],
    'best performance by an actor in a mini-series or motion picture made for television': [
        ['best', 'actor'],
        [],
        ['mini', 'series', 'mini-series', 'television', 'tv']],
    'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television': [
        ['best', 'actress', 'supporting'],
        [],
        ['television', 'tv']],
    'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television': [
        ['best', 'actor', 'supporting'],
        [],
        ['television', 'tv']
    ]}
