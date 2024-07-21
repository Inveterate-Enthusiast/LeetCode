# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size,
# and the sign represents its direction
# (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.


def asteroidCollision1(asteroids: list[int]) -> list[int]:
    OurAsteroids, newIndex = [], -1
    for index in range(len(asteroids)):
        if len(OurAsteroids) == 0:
            OurAsteroids.append(asteroids[index])
            newIndex += 1
            continue
        if (OurAsteroids[newIndex] * asteroids[index]) == abs(OurAsteroids[newIndex] * asteroids[index]) or ((OurAsteroids[newIndex] != abs(OurAsteroids[newIndex])) and (asteroids[index] == abs(asteroids[index]))):
            OurAsteroids.append(asteroids[index]); newIndex += 1
        else:
            while len(OurAsteroids) != 0 and (OurAsteroids[newIndex] * asteroids[index]) != abs(OurAsteroids[newIndex] * asteroids[index]):
                if abs(OurAsteroids[newIndex]) > abs(asteroids[index]):
                    break
                else:
                    ExplodedAsteroid = OurAsteroids.pop(); newIndex -= 1
                    if abs(ExplodedAsteroid) == abs(asteroids[index]):
                        break
            else:
                if abs(ExplodedAsteroid) != abs(asteroids[index]):
                    OurAsteroids.append(asteroids[index]); newIndex += 1
    return OurAsteroids


def asteroidCollision2(asteroids: list[int]) -> list[int]:
    OurAsteroids = []

    for asteroid in asteroids:
        OurFlag = True

        while OurAsteroids and OurAsteroids[-1] > 0 and asteroid < 0:
            if abs(OurAsteroids[-1]) <= abs(asteroid):
                ExplodedAsteroid = OurAsteroids.pop()
                if abs(ExplodedAsteroid) != abs(asteroid):
                    continue
            OurFlag = False
            break

        if OurFlag:
            OurAsteroids.append(asteroid)

    return OurAsteroids

asteroids = [8,-8]
print(asteroidCollision2(asteroids))


