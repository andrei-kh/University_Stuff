import hashlib
from zlib import crc32
import argparse
import os
from os.path import isfile, join, exists
import pickle

BUF_SIZE = 65536
DATABASE_FILENAME = 'lab_6.pkl'


def calculate_crc_hash(filename):
    f = open(filename, 'rb')
    sha256_code = hashlib.sha256()
    crc32_code = 0
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        crc32_code = crc32(data, crc32_code)
        sha256_code.update(data)
    f.close()
    return crc32_code, sha256_code.hexdigest().upper()


def create_and_save_codes(catalogs_list):
    catalogs = {}
    for catalog in catalogs_list:
        if exists(catalog):
            files = {}
            for element in os.listdir(catalog):
                if element != DATABASE_FILENAME:
                    elpath = join(catalog, element)
                    if isfile(elpath):
                        files[element] = calculate_crc_hash(elpath)
            catalogs[catalog] = files
        else:
            print(f"{catalog} is invalid directory path")

    with open(DATABASE_FILENAME, 'wb') as dumpfile:
        pickle.dump(catalogs, dumpfile)
    print('Created Database')


def check_files():
    try:
        with open(DATABASE_FILENAME, 'rb') as f:
            database = pickle.load(f)
        for catalog in database.keys():
            if exists(catalog):
                curr_dir_files = os.listdir(catalog)
                new_files = [
                    file for file in curr_dir_files
                    if file not in database[catalog].keys()
                    if isfile(join(catalog, file))
                    if file != DATABASE_FILENAME]
                removed_files = [
                    file for file in database[catalog].keys()
                    if file not in curr_dir_files
                    if file != DATABASE_FILENAME]

                if new_files:
                    print('New files:')
                    for file in new_files:
                        print(f'\t{catalog}\\{file}')
                if removed_files:
                    print('Removed files')
                    for file in removed_files:
                        print(f'\t{catalog}\\{file}')
                for file in database[catalog].keys():
                    filepath = join(catalog, file)
                    if isfile(filepath):
                        curr_chesum = calculate_crc_hash(filepath)
                        if curr_chesum != database[catalog][file]:
                            print(f'modified {filepath}:')
                            print('\tCRC before:', database[catalog][file][0])
                            print('\tCRC    now:', curr_chesum[0])
                            print('\tSHA before:', database[catalog][file][1])
                            print('\tSHA before:', curr_chesum[1])
            else:
                print(f'Catalog \'{catalog}\' does not exist')
    except FileNotFoundError:
        print('[-]Database was not created')
        return


def arguments():
    # argv = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c',
        '--cdb',
        metavar='catalog paths',
        dest='cdb',
        nargs='*',
        default=None,
        help='Create database')
    args = parser.parse_args()
    return args.cdb


args = arguments()
if args is None:
    check_files()
elif not args:
    print('No catalog paths where given to create database')
else:
    create_and_save_codes(args)
