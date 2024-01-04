def tower_of_hanoi(n: int, start_rod: int, end_rod: int) -> None:
    if n == 1:
        print(f"Moving disk from {start_rod} to {end_rod}")
