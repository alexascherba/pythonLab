def sort(x, y, z):
    if x > y:
        x, y = y, x
    if y > z:
        y, z = z, y
    if x > y:
        x, y = y, x
    return x, y, z

x1, y1, z1 = 35.2, 11.4, 21.1
x1, y1, z1 = sort(x1, y1, z1)
print(f"По возрастанию (x1, y1, z1): ({x1}, {y1}, {z1})")

x2, y2, z2 = 54, 73, 42
x2, y2, z2 = sort(x2, y2, z2)
print(f"По возрастанию (x2, y2, z2): ({x2}, {y2}, {z2})")





