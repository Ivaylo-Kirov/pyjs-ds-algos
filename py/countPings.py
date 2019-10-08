class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t):
        self.pings.append(t)
        for p in self.pings[:]:
            if p < (t - 3000):
                self.pings.remove(p)

    


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(1)
obj.ping(100)
obj.ping(3000)
obj.ping(3002)
obj.ping(3005)
obj.ping(7000)
obj.ping(7001)