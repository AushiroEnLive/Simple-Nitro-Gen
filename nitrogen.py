import requests
import random
import string


print("By AushiroEnLive")
num = int(input('Nombre de nitro à gen : '))


with open("Aushiro.txt", "w", encoding='utf-8') as file:
    print("Les nitros sont en cours de genération")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"J'ai gen {num} nitro\n")

with open("Aushiro.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")