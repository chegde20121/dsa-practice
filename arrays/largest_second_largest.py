def solve():
    a = [5, 2, 9, 7, 9]

    first = float("-inf")
    second = float("-inf")

    for x in a:
      if x > first:
        second= first
        first = x
      elif x !=first and x > second:
        second = x
    print("Largest:", first)
    print("Second largest:", second)
    print("Sum:", first + second)


if __name__ == "__main__":
    solve()