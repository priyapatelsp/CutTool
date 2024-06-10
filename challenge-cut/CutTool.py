import argparse

def cut(filePath, delimiter, fields):
    with open(filePath, 'r') as file:
        for line in file:
            parts = line.strip().split(delimiter)
            output_parts = [parts[field - 1] for field in fields]
            print(delimiter.join(output_parts))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python implementation of cut command")
    parser.add_argument("file", help="Path to the file to process")
    parser.add_argument("-d", "--delimiter", default="\t", help="Field delimiter (default is tab)")
    parser.add_argument("-f", "--fields", required=True, type=lambda s: [int(field) for field in s.split(",")],
    help="Fields to cut, separated by comma (e.g., -f 1,2,3,5)")    
    arguments = parser.parse_arguments()
   

    if arguments.fields is None:
        print("Error: You must specify at least one field with -f option")
    else:
        print(arguments)
        cut(arguments.file, arguments.delimiter, arguments.fields)