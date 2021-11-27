import json

class Matrix:
    ''' 
        Creates an object Matrix
        :param shape:(tuple) -> specifies the shape of the matrix
        :param fillValues:(int, float) -> a number with which matrix will be filled, default is 0
        :param spiralmatrix:(bool) -> if the matrix should be spiral or not, default is False
        :param loadMatrix:(str) -> the path of json file if you want to load your own matrix
    '''
    def __init__(self, shape, fillValues=0, spiral=False, loadMatrix=None):
        
        try:
            self.x, self.y = shape
        except ValueError:
            print('Entered invalid argument for shape parametr')
            
        if (type(fillValues) != int) and (type(fillValues) != float):
            print('Invalid arguments for fillValues parametr')
        
        elif spiral and (shape[0] != shape[1]):
            print('For spiral matrix should be square')

        elif loadMatrix is not None and type(loadMatrix) != str:
            print('Invalid arguments for loadMatrix parametr')

        else:
            self.spiral = spiral
            self.fillValues = fillValues
            self.path = loadMatrix
            self.matrix = None

    def constuctMatrix(self):
        if self.path:
            self.matrix = self.loadMatrixFromFile(self.path)
        elif self.spiral:
            self.matrix = self.spiralmatrix(self.x)
        else:
            self.matrix = self.generate_matrix((self.x, self.y), self.fillValues)
        return self.matrix


    def saveMatrixToFile(self, matrix, path):
        with open(path, 'w') as f:
            json.dump(matrix, f)
            

    def loadMatrixFromFile(self, path):
        with open(path) as f:
            matrix = json.load(f)
        return matrix


    def generate_matrix(self, shape, val):
        result = []
        x, y = shape
        for i in range(x):
            result.append([])
            for j in range(y):
                result[i].append(val)
        return result


    def spiralmatrix(self, N):
    
        a = self.generate_matrix((N, N), 1)
        q = 0
        for j in range(0,N//2):
            x, y = 0, 0
            for i in range(N-2*j):
                x, y = i, y
                a[x+j][y+j] = N**2 - q
                q += 1

            for i in range(1, N-2*j):
                x,y = x, i
                a[x+j][y+j] = N**2 - q
                q += 1

            for i in range((N-1)-2*j):
                x, y = x-1, y
                a[x+j][y+j] = N**2 - q
                q += 1

            for i in range((N-2)-2*j):
                x, y = x, y-1
                a[x+j][y+j] = N**2 - q
                q += 1

        return a


    def transpose(self, m):
        if (self.shapeOfmatrix(m) == 1) or (self.shapeOfmatrix(m) == 2):
            result = self.generate_matrix((len(m[0]), len(m)), 0)
            for i in range(len(m)):
                for j in range(len(m[0])):
                    result[j][i] = m[i][j]
            return result
        return None


    def shapeOfmatrix(self, m):
        for i in range(len(m)):
            if type(m[i]) != list:
                return -1
            elif len(m[0]) != len(m[i]):
                return 0
            for j in range(len(m[i])):
                if type(m[i][j]) == list:
                    return -1
        if len(m) == len(m[0]):
            return 2
        else:
            return 1


obj = Matrix(shape=(2, 2))
obj.constuctMatrix()
print(obj.matrix)