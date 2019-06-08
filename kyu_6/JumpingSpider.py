import math
import string


# https://www.codewars.com/kata/the-spider-and-the-fly-jumping-spider/python
def spider_to_fly(spider, fly):
    a = float(spider[1])
    b = float(fly[1])
    angC = (string.ascii_lowercase.index(spider[0].lower()) - string.ascii_lowercase.index(fly[0].lower())) * 45
    return math.sqrt((a * a + b * b) - 2 * a * b * math.cos(math.radians(angC)))
