import sys
from random import randint

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self, has_header=True):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()

            if has_header:
                lines = lines[1:]

            data = []
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) != 2 or not all(part in {'0', '1'} for part in parts):
                    raise ValueError(f'Invalid data format in file')
                data.append([int(parts[0]), int(parts[1])])

            return data

        except FileNotFoundError:
            raise FileNotFoundError(f'File "{self.file_path}" not found')
        except Exception as e:
            raise ValueError(f'Error while reading the file: {e}')

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            if total == 0:
                return 0.0, 0.0
            head_frac = (heads / total) * 100
            tail_frac = (tails / total) * 100
            return head_frac, tail_frac

    class Analytics(Calculations):
        def predict_random(self, steps):
            predictions = []
            for _ in range(steps):
                if randint(0, 1) == 0:
                    predictions.append([0, 1])
                else:
                    predictions.append([1, 0])
            return predictions

        def predict_last(self):
            if not self.data:
                return None
            return self.data[-1]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 first_child.py <file_path>')
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        data = research.file_reader()

        print(data)

        analytics = Research.Analytics(data)
        heads, tails = analytics.counts()
        print(heads, tails)

        head_frac, tail_frac = analytics.fractions(heads, tails)
        print(head_frac, tail_frac)

        random_predictions = analytics.predict_random(3)
        print(random_predictions)

        last_prediction = analytics.predict_last()
        print(last_prediction)

    except Exception as e:
        print(f'Error: {e}')  
 




                       
