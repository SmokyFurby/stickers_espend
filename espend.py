GEN_INFO = {
    '1': (0.25, 23, 5),
    '2': (0.6, 56, 5),
    '3': (0.8, 32, 4),
    '4': (0.99, 40, 2),
    '5': (0.7, 32, 10),
    '6': (0.7, 46, 10),
    '7': (0.8, 60, 10),
    '8': (0.8, 47, 4),
    '9': (0.9, 32, 3),
    '12': (3.3, 23, 2),
    'hedgehog': (2.5, 10, 1)
    }

print('''
This program can estimate the spend for
getting a particular ticket from buying
standard packs from its generation.
''')

print(
    'Available generations: ' + ','.join(GEN_INFO.keys()) + '\n'
)

gen = str(
    input(
        'Pick a generation...'
        )
    )

pack_cost, num_stickers, pack_size = GEN_INFO[gen]

q = ((num_stickers - 1) / num_stickers) ** pack_size
p = 1 - q

expected_packs: float = 1 / p
spend = expected_packs * pack_cost

print('£' + str(round(spend, 2)) + 'i')
