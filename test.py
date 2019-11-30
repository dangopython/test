class Point(object):
    def __init__(self, x = 0.0, y = 0.0):
        self.m_x = x
        self.m_y = y
    def print(self):
        print(self.m_x, self.m_y)

if __name__ == "__main__":
    import tkinter
    tkinter._test()
    P1 = Point(45,78)
    P1.print()

