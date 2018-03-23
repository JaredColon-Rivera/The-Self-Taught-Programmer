

def bottles_of_beer(bob):
    """Prints 99 Bottles of Beer on the wall lyrics.
    :param bob: must be a positive integer."""

    if bob < 1:
        print("No more bottles of beer on the wall. no more bottles of beer.")
        return
    tmp = bob
    bob -= 1
    print("""%s bottles of beer on the wall. %s bottles of beer.
    Take one down, pass it around, %s bottles of beer on the wall.""" % (tmp, tmp, bob))

    bottles_of_beer(bob)


bottles_of_beer(99)