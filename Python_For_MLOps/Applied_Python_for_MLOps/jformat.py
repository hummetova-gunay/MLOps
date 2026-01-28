import os #interact with the operating system (files, folders, environment variables)
import sys # interact with how Python itself is run (command-line arguments, exit codes, etc.)
import json # work with JSON data (very common in automation)
import argparse
def formatter(string, sort_keys = True, indent = 4):
    # load incoming string into json 
    loaded_json = json.loads(string) # take a str that looks like JSON and convert it into a py dict

    return json.dumps(loaded_json, sort_keys = sort_keys, indent = indent)

def main(path, no_sort):
    if no_sort:
        sort_keys = False
    else:
        sort_keys = True
    with open(path, 'r') as _f: # underscore means this variable is not important elsewhere
        print(
            formatter(_f.read())
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is the jformat tool')
    parser.add_argument("--sort", action= "store_true", help="set the sorting")
    args = parser.parse_args()
    print(args.sort)
    # main(sys.argv[-1], no_sort = False)
