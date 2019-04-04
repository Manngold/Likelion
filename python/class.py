class Service:
    def __init__(self, name):
        self.name = name

    def secret(self, name):
        print("%s's secret is nothing" % name)


pey = Service("pey")
pey.secret(pey.name)
