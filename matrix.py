class Matrix:
    ''' 
        Creates an object Matrix
        :param shape:(tuple) -> specifies the shape of the matrix
        :param fillValues:(int, float) -> a number with which matrix will be filled, default is 0
        :param spiralmatrix:(bool) -> if the matrix should be spiral or not, default is False
        :param loadMatrix:(str) -> the path of json file if you want to load your own matrix
        '''
    def __init__(self, shape, fillValues = 0, spiralmatrix = False, loadMatrix = None):
        
        try:
            self.x, self.y = shape
        except ValueError:
            print('Entered invalid argument for shape parametr')
            
        if (type(fillValues) != int) and (type(fillValues) != float):
            print('Invalid arguments for fillValues parametr')
            return None
        
        elif spiralmatrix and (shape[0] != shape[1]):
            print('For spiral matrix should be square')
            return None
        elif loadMatrix != None and type(loadMatrix) != str:
                print('Invalid arguments for loadMatrix parametr')
                return None
        else:
            self.spiralmatrix = spiralmatrix
            self.fillValues = fillValues
            self.path = loadMatrix
            self.matrix = None
            
        
    def constuctMatrix(self):
        if self.path:
            self.matrix = loadMatrixFromFile(self.path)
            
        elif self.spiralmatrix:
            self.matrix = spiralmatrix(self.x)
        else:
            self.matrix = generate_matrix((self.x, self.y), self.fillValues)
        
        return self.matrix
    
    
    def saveMatrixToFile(self, matrix, path):
        with open(path, 'w') as f:
            json.dump(matrix, f)
            
            
    def loadMatrixFromFile(path):
        with open(path) as f:
            matrix = json.load(f)
    
        return matrix
        
        
    def spiralmatrix(N):
    
        a = generate_matrix((N, N), 1)
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

    def generate_matrix(shape, val):
        result = []
        x, y = shape
        for i in range(x):
            result.append([])
            for j in range(y):
                result[i].append(val)
        return result
    
    
    def transpose(m):
        if (shapeOfmatrix(m) == 1) or (shapeOfmatrix(m) == 2):
            result = generate_matrix((len(m[0]), len(m)), 0)
            for i in range(len(m)):
                for j in range(len(m[0])):
                    result[j][i] = m[i][j]

            return result

        return None  
