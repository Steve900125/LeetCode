class a:
    def b(self):
        print("b")
        return 1
    def c(self):
        return self.b()

item = a()
item.c()