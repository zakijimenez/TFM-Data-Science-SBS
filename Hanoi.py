def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Mover disco 1 de", source, "a", destination)
        return 1

    count1 = hanoi(n - 1, source, auxiliary, destination)
    print("Mover disco", n, "de", source, "a", destination)
    count2 = 1
    count3 = hanoi(n - 1, auxiliary, destination, source)

    return count1 + count2 + count3

def count_hanoi(n, source, destination, auxiliary):
    print("Movimientos de torre:")
    total_moves = hanoi(n, source, destination, auxiliary)
    print("Total de movimientos:", total_moves)

n = 4
count_hanoi(n, 'A', 'B', 'C')