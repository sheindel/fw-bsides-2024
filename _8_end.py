import os

def main():
    url = 'https://github.com/sheindel/fw-bsides-2024/'
    os.system(f'qrencode -t ansiutf8 {url}')
