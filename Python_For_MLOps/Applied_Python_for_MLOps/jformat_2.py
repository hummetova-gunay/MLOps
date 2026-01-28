import sys
import json
import click


def formatter(string, sort_keys = True, indent= 4):
    loaded_json = json.loads(string)
    return  json.dumps(loaded_json, sort_keys=sort_keys, indent = indent)

@click.command()
@click.argument('path', type = click.Path(exists=True))
@click.option('--sort', '-s', is_flag = True)
def main(path, sort):
    with open(path, 'r') as _f:
        print(
            formatter(_f.read(), sort_keys=sort)
        )

if __name__ == '__main__':
    main()