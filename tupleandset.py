players=("virat kohli", "rohit sharma", "mohammed siraj", "shreyas iyer", "tilak varma")
print(players[2])
x,y=(10,20)
print(x,y)

games={"hide n seek", "tag", "lock in key", "basketball", "football", "tag"}
print(games)

games.add("Tennis")
print(games)

games.remove("hide n seek")
print(games)
print(games.pop())

rcb={"Virat kohli", "mohammed siraj ", "tilak varma", "venky"," bhuvi"}
gt={"gill", "mohammed siraj ", "tilak varma", "sharma", "samson"}
csk={"mohammed siraj ", "tilak varma", "Abishek", "Shami"}
print(rcb.intersection(gt))
print(rcb.union(gt))
print(gt.difference(rcb))
print(rcb.difference(gt))
print(rcb.intersection(gt.intersection(csk)))