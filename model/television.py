class Television:
    def __init__(self):
        self.on = False
        self.channel = 0

    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def up_channel(self):
        self.channel += 1

    def low_channel(self):
        self.channel -= 1


if __name__ == '__main__':
    television = Television()
    print(television.on)
    television.power()
    print(television.on)
    print(television.channel)
    television.up_channel()
    television.up_channel()
    print(television.channel)
    television.low_channel()
    print(television.channel)
