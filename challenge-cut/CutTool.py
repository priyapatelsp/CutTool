import argparse

def cut(file_path, delimiter, fields):
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(delimiter)
            output_parts = [parts[field - 1] for field in fields]
            print(delimiter.join(output_parts))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python implementation of the cut command")
    parser.add_argument("file", help="Path to the file to process")
    parser.add_argument("-d", "--delimiter", default="\t", help="Field delimiter (default is tab)")
    parser.add_argument("-f", "--fields", required=True, type=lambda s: [int(field) for field in s.split(",")],
    help="Fields to cut, separated by comma (e.g., -f 1,3,5)")    
    args = parser.parse_args()
   
    # fields = [int(field) for field in args.fields.replace(',', ' ').split()]


    if args.fields is None:
        print("Error: You must specify at least one field with -f option")
    else:
        print(args)
        cut(args.file, args.delimiter, args.fields)