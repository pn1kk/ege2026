from math import dist

def dbscan(dots):
    eps = 0.5
    all_clusters = []

    while len(dots) > 0:
        X = dots.pop()
        new_cluster = [X]
        i = 0
        while i < len(new_cluster):
            d = new_cluster[i]
            neighbours = []

            for d2 in dots[:]:
                if dist(d, d2) <= eps and d2 not in new_cluster:
                    neighbours += [d2]
        
            new_cluster += neighbours

            for d2 in neighbours:
                dots.remove(d2)

            i += 1

        all_clusters += [new_cluster]

    return all_clusters

def center(cluster):
    m_sums = []
    m_dots = []
    for p in cluster:
        s = 0
        for p1 in cluster:
            s += dist(p, p1)
        m_sums.append(s)
        m_dots.append(p)
    return m_dots[m_sums.index(min(m_sums))]

dots = []
f = open('27_A.txt')

for s in f:
    x, y = [float(d) for d in s.replace(',', '.').split()]
    dots.append([x, y])

clusters = dbscan(dots)
centers = [center(cl) for cl in clusters]

sumx = 0
sumy = 0

for i in centers:
    sumx += centers[0]
    sumy += centers[1]

print([len(i) for i in clusters])
print(sumx/len(centers) * 1000, sumy/len(centers) * 1000)
