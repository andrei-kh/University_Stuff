import numpy as np
import warnings

warnings.filterwarnings('ignore')


class Simplex:
    def __init__(self, A, b, c, signs, simplexType, M=100):
        self.simplexType = simplexType
        self.c_num = len(A)
        self.v_num = len(A[0])
        self.count = self.v_num
        self.basicVars = []
        self.artaficialVars = []
        self.X = None
        self.z_optimal = None
        self.M = M
        self.c = c
        self.tableau = self.__buildTableau(A, b, c, signs)

    def __buildTableau(self, A, b, c, signs):
        R = np.eye(self.c_num)
        P = b

        for i in range(self.c_num):
            if signs[i] == '<=':
                self.c = np.vstack((self.c, [[0]]))
                self.count += 1
                self.basicVars.append(self.count - 1)
                self.artaficialVars = [self.artaficialVars, 0]
            elif signs[i] == '==':
                if self.simplexType == 'min':
                    self.c = np.vstack((self.c, [[self.M]]))
                else:
                    self.c = np.vstack((self.c, [[self.M]]))

                self.count += 1
                self.basicVars.append(self.count - 1)
                self.artaficialVars = [self.artaficialVars, 1]
            elif signs[i] == '>=':
                if self.simplexType == 'min':
                    self.c = np.vstack((self.c, [[0], [self.M]]))
                else:
                    self.c = np.vstack((self.c, [[0], [-self.M]]))

                c_s = R.shape[1]
                R = np.hstack((R[:, 0:self.count - self.v_num], -R[:, [self.count - self.v_num]],
                               R[:, self.count - self.v_num:c_s]))
                k = np.size(P)
                P = np.vstack((P[0:self.count - self.v_num, [0]], np.array([[0]]), P[self.count - self.v_num:k, [0]]))

                self.count += 2
                self.basicVars.append(self.count - 1)
                self.artaficialVars = [self.artaficialVars, 0, 1]
            else:
                ValueError("Invalid Sign")

        self.X = np.vstack((np.zeros((self.v_num, 1)), P))
        A = np.hstack((A, R))

        tablaeu = np.vstack((np.hstack((-np.transpose(self.c), np.array([[0]]))), np.hstack((A, b))))
        self.z_optimal = np.matmul(np.transpose(self.c), self.X)

        if self.z_optimal != 0:
            for i in range(self.c_num):
                if signs[i] == '==' or signs[i] == '>=':
                    if self.simplexType == 'min':
                        tablaeu[0, :] = tablaeu[0, :] + self.M * tablaeu[1 + i, :]
                    else:
                        tablaeu[0, :] = tablaeu[0, :] - self.M * tablaeu[1 + i, :]

        return tablaeu

    def __getPivotIndexes(self):
        i, j = None, None
        rows, cols = self.tableau.shape
        if self.simplexType == 'min':
            i = np.amax(self.tableau[0, 0:cols - 1])
            if i <= 0:
                return None
            j = np.argmax(self.tableau[0, 0:cols - 1])
        else:
            i = np.amin(self.tableau[0, 0:cols - 1])
            if i >= 0:
                return None
            j = np.argmin(self.tableau[0, 0:cols - 1])

        return i, j

    def __pivot(self, pivot_indexes):
        pi, pj = pivot_indexes
        rows, cols = self.tableau.shape
        T = self.tableau[1:rows, cols - 1] / self.tableau[1: rows, pj]
        R = np.logical_and(T != np.inf, T > 0)
        maskedT = [T[i] for i in range(np.size(T)) if R[i] == 1]
        mIndx = list(T).index(min(maskedT))

        currentZ = self.tableau[[0], :]
        pivotElement = self.tableau[mIndx + 1, pj]
        pivotRowDivided = self.tableau[mIndx + 1, :] / pivotElement
        self.tableau = self.tableau - self.tableau[:, [pj]] * pivotRowDivided
        self.tableau[mIndx + 1, :] = pivotRowDivided

        self.basicVars[mIndx] = pj
        basic = self.tableau[:, cols - 1]
        self.X = np.zeros((self.count, 1))
        for i in range(np.size(self.basicVars)):
            self.X[self.basicVars[i]] = basic[i + 1]

        self.c = -np.transpose(currentZ[[0], 0:self.count])
        self.z_optimal = currentZ[0, cols - 1] + np.matmul(np.transpose(self.c), self.X)
        self.tableau[0, cols - 1] = self.z_optimal

    def solve(self):
        i = 0
        while True and i < 500:
            pivot_indexes = self.__getPivotIndexes()
            if pivot_indexes is None:
                break
            self.__pivot(pivot_indexes)
            i += 1

        aSize = np.size(self.artaficialVars)
        for i in range(aSize):
            if self.artaficialVars[i] == 1:
                if self.X[self.v_num + i] > 0:
                    print("Infeasible solution")
                    break

        return self.z_optimal[0][0], self.X


def parse_equations(equations):
    firstString = equations[0].split()
    sType = firstString[0]
    c = list(map(float, firstString[1:]))
    c = [[cc] for cc in c]

    A = []
    b = []
    signs = []

    for eq in equations[1:]:
        eq = eq.split()
        signs.append([eq[-2]])
        A.append(list(map(float, eq[:-2])))
        b.append([float(eq[-1])])

    return np.array(A), np.array(b), np.array(c), np.array(signs), sType


def print_system(equations):
    firstLine = equations[0].split()
    v_num = len(firstLine) - 1
    if firstLine[0] == 'max':
        print('Maximize F(x) = ', end='')
    else:
        print('Minimize F(x) = ', end='')

    for p in enumerate(firstLine[1:]):
        if p[0] != 0:
            if p[1][0] == '-':
                print('- ', end='')
                p = (p[0], p[1][1:])
            else:
                print('+ ', end='')
        print(f'{p[1]}*x{p[0] + 1} ', end='')
    print()

    print("subject to")
    for line in equations[1:]:
        print('                ', end='')
        eq = line.split()
        for i in range(v_num):
            if i != 0:
                if eq[i][0] == '-':
                    print('- ', end='')
                    eq[i] = eq[i][1:]
                else:
                    print('+ ', end='')
            print(f'{eq[i]}*x{i + 1} ', end='')
        print(eq[-2], eq[-1])
    print()


if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    print("-----------------------Simplex solver-----------------------")
    print("First input min/max, then coefficents, separated by space,")
    print("of the equation that needs to be minimized/maximized.")
    print("For example: max 10 20")
    print()
    print("Then one by one input constraints in the form:")
    print("coeficents separated by space, equality sign, some number")
    print("For example: 2 7 <= 21")
    print()
    print("At the end input blank line.")
    print()
    equations = []
    while True:
        inp = input()
        if inp == '':
            break
        equations.append(inp)
    print("You inputed:")
    print_system(equations)
    args = parse_equations(equations)
    s = Simplex(*args)
    ans, ans_vals = s.solve()
    print("Answer is:", format(ans, '.6f'))
