class HighScoreTable:
    def __init__(self, limit):
        self._limit = limit
        self.scores = []

    def update(self, n):
        self.scores.append(n)
        self.scores = sorted(self.scores, reverse=True)[:self._limit]

    def reset(self):
        self.scores = []


# ======================
# Example usage
# ======================
if __name__ == '__main__':
    high_score_table = HighScoreTable(5)

    print(high_score_table.scores)

    scores = [34, 30, 66, 28, 17, 97, 75, 24, 24, 81, 19, 38, 57, 45, 52, 67, 13, 32, 86, 99, 21, 18, 13, 70, 88, 84, 54,
              15, 71, 33, 75, 36, 56, 85, 59, 88, 57, 24, 34, 51, 29, 54, 92, 22, 70, 49, 86, 77, 10, 40, 77, 28, 50, 44,
              73, 28, 16, 90, 94, 17, 65, 93, 68, 77, 84, 18, 12, 86, 74, 29, 38, 12, 28, 24, 41, 54, 53, 35, 11, 80, 95,
              10, 93, 42, 23, 57, 81, 20, 78, 73, 51, 19, 55, 71, 45, 62, 54, 42, 39, 54]

    for score in scores:
        high_score_table.update(score)

    print(high_score_table.scores)
