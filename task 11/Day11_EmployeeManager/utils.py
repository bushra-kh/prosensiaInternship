def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()

def write_lines(filename, lines):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.strip() + "\n")