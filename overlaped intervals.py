# A da B simravleebis tanakveta tolia A da B simravleebis jams minus mati gaertianeba
def overlap(a, b, c, d):
    interval1 = sorted([a, b])
    interval2 = sorted([c, d])
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return 0
    Sum = [interval1[0] + interval2[0], interval1[1] + interval2[1]]
    united = [min([a, b, c, d]), max([a, b, c, d])]
    overlaped = [Sum[0] - united[0], Sum[1] - united[1]]
    return overlaped
print(overlap(9, 7, 7, 4))  # mushaobs
