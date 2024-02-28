import json

def parse_quran(rewayah: str):
    rewayah_map = {
        'bazzi': 'Bazzi.json',
        'doori': 'Doori.json',
        'hafs': 'Hafs.json',
        'qaloon': 'Qaloon.json',
        'qumbul': 'Qumbul.json',
        'shouba': 'Shouba.json',
        'soosi': 'Soosi.json',
        'warsh': 'Warsh.json'
    }

    with open(f'quran_data/{rewayah_map[rewayah]}') as file:
        data = json.load(file)

        return data
