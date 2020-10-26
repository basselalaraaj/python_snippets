def subnetworks(nets, crushes):
  runningNets = [[y for y in x if y not in crushes] for x in nets]
  newNets = []
  for net in runningNets:
    if len(net) == 0: continue
    for newNet in newNets.copy():
      links = set(newNet)-set(net)
      if len(links) != len(newNet):
        newNets.remove(newNet)
    newNets.append(net)
  return len(newNets)

print(subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']), "should be equal to 2")
print(subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']), "should be equal to 3")
print(subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']), "should be equal to 1" )

print(subnetworks([["A","B"],["A","C"],["A","D"],["D","F"],["B","C"]],["A"]), "should be equal to 2")
