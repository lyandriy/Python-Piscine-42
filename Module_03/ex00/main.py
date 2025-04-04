from NumpyCreator import NumpyCreator

npc = NumpyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))
print("\n")
print(npc.from_list([[1,2,3],[6,4]]))
print("\n")
print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
print("\n")
print(npc.from_list(((1,2),(3,4))))
print("\n")
print(npc.from_tuple(("a", "b", "c")))
print("\n")
print(npc.from_tuple(["a", "b", "c"]))
print("\n")
print(npc.from_iterable(range(5)))
print("\n")
shape=(3,5)
print(npc.from_shape(shape, 4))
print("\n")
print(npc.random(shape))
print("\n")
print(npc.identity(4))
