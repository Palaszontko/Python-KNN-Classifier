class Sample:
    def __init__(self, dataTag : str, vector : list):
        self.dataTag = dataTag
        self.vector = vector

    def __str__(self):
        return f"Data Tag: {self.dataTag}, Vectors: {self.vector}"

class CalculatedSample:
    def __init__(self, dataTag : str, vector : list, distance : float):
        self.dataTag = dataTag
        self.vector = vector
        self.distance = distance
    def __str__(self):
        return f"Data Tag: {self.dataTag}, Vectors: {self.vector}, Distance: {self.distance}"
    
class KNN:
    def __init__(self, k : int, trainingDataPath : str, testDataPath : str):
        self.k = k
        self.trainingDataPath = trainingDataPath
        self.testDataPath = testDataPath
    def loadCsv(self, path : str) -> list:
        samples = []
        try:
            with open(path, 'r') as f:   
                data = f.readlines()

                for line in data:
                    if line == '' or line == '\n':
                        continue
                    line = line.strip().split(';')
                    samples.append(Sample(line[-1], [float(x) for x in line[:-1]]))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        return samples

if __name__ == "__main__":
