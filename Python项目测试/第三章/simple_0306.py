Worlds = []
Worlds.append('usa')
Worlds.append('india')
Worlds.append('england')
Worlds.append('singapore')
Worlds.append('ireland')
Worlds.append('china')
print(Worlds)
print("-------------------------")
print("-------------------------")
print(f"正向临时排序：{sorted(Worlds)}")
print(f"检查:::{Worlds}")
print("-------------------------")
print("-------------------------")
print(f"反向临时排序：{sorted(Worlds,reverse=True)}")
print(f"检查:::{Worlds}")
print("-------------------------")
print("-------------------------")
Worlds.reverse()
print(f"反转列表元素的排列顺序:{Worlds}")
Worlds.reverse()
print(f"再次反转列表元素的排列顺序，即恢复原状:{Worlds}")
print("-------------------------")
print("-------------------------")
Worlds.sort()
print(f"永久性地修改排列顺序:{Worlds}")
Worlds.sort(reverse=True)
print(f"永久性地修改排列顺序:{Worlds}")
print(f"\t一共有{len(Worlds)}个国家")
