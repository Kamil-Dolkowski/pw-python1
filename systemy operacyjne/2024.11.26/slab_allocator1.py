import random
class Slab:
    def __init__(self, object_size, object_per_slab = 10):
        self.slabs = []
        self.object_size = object_size
        self.object_per_slab = object_per_slab
        self._internal_alloc()

    def _internal_alloc(self):
        slab = {
            "memory": bytearray(self.object_size * self. object_per_slab),
            "available": set(range(self.object_per_slab)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        }
        self.slabs.append(slab)

    def alloc(self):
        for slab in self.slabs:
            if slab["available"]: # if len(slab["available"]) != 0
                index = slab["available"].pop()
                return (slab, index)
            print("Zabrakło pamięci, alokujemy nowy slab")
        self._internal_alloc()
        return self.alloc()
    
    def free(self, slab, index):
        slab["available"].add(index)
        
    def print(self):
        print("Wolna pamięć:")
        for i, slab in enumerate(self.slabs):
            print(f"Slab {i}: " + str(slab["available"]))




struct_size = 200 # bytes
allocated = []
allocator = Slab(struct_size)


for i in range(25):
    allocated.append(allocator.alloc())

allocator.print()

order = list(range(25))
random.shuffle(order)
order = order[0:5]

for i in order:
    slab, index = allocated[i]
    allocator.free(slab, index)

allocator.print()

allocator.alloc()

allocator.print()