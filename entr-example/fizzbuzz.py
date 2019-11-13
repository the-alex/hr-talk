def fizzbuzz(x):
    """Take an x and -- gimme that newline delimited string -- YEAH --
    the one with the 'fizz' for mod 3 and 'buzz' for mod 5 -- UGH
    THAT'S REAL PROGRAMMING"""

    results = []
    for n in range(x):
        result = ''

        if not n % 3:
            result += 'fizz'

        if not n % 5:
            result += 'buzz'

        if not result:
            result = str(n)

        results.append(result)

    return '\n'.join(results)

print(fizzbuzz(10))

