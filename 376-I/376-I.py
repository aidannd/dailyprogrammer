# https://www.reddit.com/r/dailyprogrammer/comments/b0nuoh/20190313_challenge_376_intermediate_the_revised/

# not scalable
def countLeapYears(year1, year2):
    leapYearCount = 0
    for year in range(year1, year2):
        if year % 4 == 0 and (year % 100 != 0 or year % 900 == 200 or year % 900 == 600):
            leapYearCount += 1
    return leapYearCount

assert countLeapYears(2016, 2017) == 1
assert countLeapYears(2019, 2020) == 0
assert countLeapYears(1900, 1901) == 0
assert countLeapYears(2000, 2001) == 1
assert countLeapYears(2800, 2801) == 0
assert countLeapYears(123456, 123456) == 0
assert countLeapYears(1234, 5678) == 1077
assert countLeapYears(123456, 7891011) == 1881475
# assert countLeapYears(123456789101112, 1314151617181920) == 288412747246240