

# The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of
# the sums of its parts. https://www.codewars.com/kata/sums-of-parts/train/python
def parts_sums(ls):
    tmp_sum = sum(ls)
    result = [tmp_sum]
    for i in range(len(ls)):
        tmp_sum = tmp_sum - ls[i]
        result.append(tmp_sum)
    return result
