class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def rookcheck(a, b, c, d, e, f):
            if a == e:
                if c == a:
                    if (min(b, d) == b and max(d, f) == f) or (max(b, d) == b and min(d, f) == f):
                        rookres = 2
                        print(rookres)
                        return rookres
                    else:
                        rookres = 1
                        print(rookres)
                        return rookres
                else:
                    rookres = 1
                    print(rookres)
                    return rookres
            elif b == f:
                if d == b:
                    if (min(a, c) == a and max(c, e) == e) or (max(a, c) == a and min(c, e) == e):
                        rookres = 2
                        print(rookres)
                        return rookres
                    else:
                        rookres = 1
                        print(rookres)
                        return rookres
                else:
                    rookres = 1
                    print(rookres)
                    return rookres
            rookres = 2
            print(rookres)
            return rookres
        def bishopcheck(a, b, c, d, e, f):
            if c - d == e - f:
                if a - b == c - d:
                    if a > c and a < e or a > e and a < c:
                        bishres = 2
                        print(bishres)
                        return bishres
                    bishres = 1
                    print(bishres)
                    return bishres
                else:
                    bishres = 1
                    print(bishres)
                    return bishres
            if c + d == e + f:
                if a + b == c + d:
                    if a > c and a < e or a > e and a < c:
                        bishres = 2
                        print(bishres)
                        return bishres
                    bishres = 1
                    print(bishres)
                    return bishres
                else:
                    bishres = 1
                    print(bishres)
                    return bishres
            bishres = 2
            print(bishres)
            return bishres
        rookres = rookcheck(a, b, c, d, e, f)
        bishres = bishopcheck(a, b, c, d, e, f)
        if bishres == None:
            print(rookres)
            return rookres
        if rookres == None:
            print(bishres)
            return bishres
        if bishres < rookres:
            print(bishres)
            return bishres
        else:
            print(rookres)
            return rookres

                


    minMovesToCaptureTheQueen(1, a = 4, b = 5, c = 7, d = 8, e = 2, f = 3)