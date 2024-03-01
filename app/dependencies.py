import json

font_map = {
    'hafs': 'hafs18',
    'warsh': 'warsh10',
    'shouba': 'shouba8',
    'qaloon': 'qaloon10',
    'doori': 'doori9',
    'soosi': 'soosi9',
    'bazzi': 'bazzi7',
    'qumbul': 'qumbul7'
}

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

def parse_quran(rewayah: str, server_access: bool):
    if server_access:
        directory = '/home/quranworld/quran-world/app/quran_data/'
    else: 
        directory = '/quran_data/'
    
    with open(f'{directory}{rewayah_map[rewayah]}') as file:
        data = json.load(file)

        return data
    
def return_suras(quran: dict):
    suras = []
    
    for aya in quran:
        if aya['sura_name_en'] not in suras:
            suras.append(aya['sura_name_en'])
            
    return suras
