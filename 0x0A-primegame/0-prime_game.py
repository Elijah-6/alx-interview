#!/usr/bin/python3
"""
This module contains the implementation of the prime game.
Functions:
    isWinner(x, nums): Determines the winner of the prime game.
isWinner(x, nums):
    Determines the winner of the prime game after x rounds.
    Parameters:
        x (int): The number of rounds.
        nums (list): A list of integers representing
        the upper limit of numbers for each round.
    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben").
        None: If there is no winner or invalid input.
"""


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_count(n):
        primes = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return sum(primes[2:])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count(n) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
