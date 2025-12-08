class Solution:
    def p1(self, points):
        pass

if __name__ == "__main__":
    sol = Solution()
    points = [
    (162, 817, 812),
    (57, 618, 57),
    (906, 360, 560),
    (592, 479, 940),
    (352, 342, 300),
    (466, 668, 158),
    (542, 29, 236),
    (431, 825, 988),
    (739, 650, 466),
    (52, 470, 668),
    (216, 146, 977),
    (819, 987, 18),
    (117, 168, 530),
    (805, 96, 715),
    (346, 949, 466),
    (970, 615, 88),
    (941, 993, 340),
    (862, 61, 35),
    (984, 92, 344),
    (425, 690, 689),
    ]
    # with open("input.txt", 'r') as file:
    #     for line in file:
    #         line = line.strip()
    #         if not line:
    #             continue
    #         x, y, z = map(int, line.split(','))
    #         points.append((x, y, z))
    result = sol.p1(points)