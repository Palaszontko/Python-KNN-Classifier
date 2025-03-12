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
    def euclidianDis(A, B): 
        if len(A) != len(B):
            raise ValueError("Vectors must have the same length")
        dis = 0 
        for i in range(len(A)):
            dis +=  math.pow(A[i] - B[i], 2)
        return math.sqrt(dis)
    
    def getKClosest(self, V : list) -> dict:
        calculatedSamples = []

        for sample in self.trainData:
            dis = KNN.euclidianDis(V, sample.vector)
            calculatedSamples.append(CalculatedSample(sample.dataTag, sample.vector, dis))

        sortedSamples = sorted(calculatedSamples, key=lambda x: x.distance)

        return sortedSamples[:self.k]
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
    def start(self, getInput : bool) -> float:
        self.trainData = self.loadCsv(self.trainingDataPath)

        correctResults = 0
        totalResults = 0

        for sample in self.loadCsv(self.testDataPath):
            kClosestGroups = self.getKClosest(sample.vector)
            closestDataTags = {x.dataTag : sum(1 for item in kClosestGroups if item.dataTag == x.dataTag) for x in kClosestGroups}
            print(f"{'\033[92m'}{sample.dataTag} {'\033[95m'}{max(closestDataTags)}{'\033[0m'}")

            if sample.dataTag == max(closestDataTags):
                correctResults += 1
            totalResults += 1

        print(f"Accuracy = {round(correctResults / totalResults * 100, 3)}%")
        if getInput:
            self.getInput()

        return correctResults / totalResults * 100
    def getInput(self):
        print("Type 'exit' to exit")
        while True:
            print("Enter a sample to test: ")
            sample = input().split(';')

            if 'exit' in "".join(sample):
                break
            elif len(sample) != len(self.trainData[0].vector):
                print("Invalid sample")
                continue
            elif any(c.isalpha() for c in "".join(sample)):
                print("Invalid sample: contains letters")
                continue

            sample = Sample('', [float(x) for x in sample])
            kClosestGroups = self.getKClosest(sample.vector)
            closestDataTags = {x.dataTag : sum(1 for item in kClosestGroups if item.dataTag == x.dataTag) for x in kClosestGroups}
            print(f"{'\033[92m'}{sample.dataTag} {'\033[95m'}{max(closestDataTags)}{'\033[0m'}")

if __name__ == "__main__":
