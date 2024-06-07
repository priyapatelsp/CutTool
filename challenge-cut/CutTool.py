import sys

def cut_tool(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                fields = line.strip().split('\t')
                if len(fields) >= 2:
                    print(fields[1])
                else:
                    print("Field number exceeds available fields in line:", line.strip())
    except IOError as e:
        print("Error reading file:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python simple_cut.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    cut_tool(file_path)