class qsequence:
    def __init__(self, in_q: list):
        self.in_q = in_q[:]

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.in_q != [1, 2]:
            out_q = self.in_q[-self.in_q[-1]] + self.in_q[-self.in_q[-2]]
            self.in_q.append(out_q)
            return out_q
        else:
            raise StopIteration

qqce = qsequence([1, 1])
for _ in range(10):
    print(next(qqce))