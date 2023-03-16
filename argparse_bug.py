import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--foobar", type=str)
args = parser.parse_args()

print(f'temp_args.foobar: {args.foobar}')
