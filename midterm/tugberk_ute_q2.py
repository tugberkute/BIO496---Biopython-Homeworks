class Transcript:

    def __init__(self, ts_start, ts_end):
        self.ts_start = int(ts_start)
        self.ts_end = int(ts_end)

    def ts_length(self):
        return self.ts_end - self.ts_start + 1


ts1 = Transcript(1645454, 1646077)
print(ts1.ts_length())

print(ts1.ts_start)