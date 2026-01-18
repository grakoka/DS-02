import sys

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def file_reader(self, has_header=True):
        try:
            with open(self.file_path,'r') as file:
                lines = file.readlines()

            if has_header:
                lines = lines[1:]

            data = []       
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) != 2 or not all(part in {'0', '1'} for part in parts):
                    raise ValueError('Invalid data format in file')
                data.append([int(parts[0]), int(parts[1])])

            return data

        except FileNotFoundError:
            raise FileNotFoundError(f'File "{self.file_path}" not found')
        except Exception:
            raise ValueError(f'Error while reading the file: {e}')

    class Calculations:
        @staticmethod
        def counts(data):
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails

        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            if total == 0:
                return 0.0, 0.0
            head_frac = (heads / total) * 100
            tail_frac = (tails / total) * 100
            return head_frac, tail_frac

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 first_nets.py <file_path>')
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        data = research.file_reader()

        print(data)

        heads, tails = Research.Calculations.counts(data)
        print(heads, tails)

        head_frac, tail_frac = Research.Calculations.fractions(heads, tails)
        print(head_frac, tail_frac) 

    except Exception as e:
        print(f'Error: {e}')   

