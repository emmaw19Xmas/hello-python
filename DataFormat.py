"""为什么我们需要类方法和静态方法"""

class DateFormat:

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}/{self.month}/{self.day}"


year, month, day = 2021, 7, 1

demo = DateFormat(year, month, day)
print(demo.out_date())