import sys 

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()

            header = lines[0].strip()
            if header != 'head,tail':
                raise ValueError('Invalid header format')

            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) != 2 or not all (part in {'0', '1'} for part in parts):
                    raise ValueError('Invalid data fornmat in file')

            return ''.join(lines)

        except FileNotFoundError:
            raise FileNotFoundError(f'File "{self.file_path}" not found')
        except Exception as e:
            raise ValueError(f'Error while reading the file: {e}')

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python3 first_constructor.py <file_path>')
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        print(research.file_reader())
    except Exception as e:
        print(f'Error {e}')        



    



