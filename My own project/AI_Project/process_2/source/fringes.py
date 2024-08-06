import heapq
class PriorityQueue:
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        MAX_PRIORITY = 2**31 - 1  # Điều chỉnh hằng số để đảm bảo số ưu tiên không vượt quá phạm vi
        entry = (MAX_PRIORITY - priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0
    
    def qSize(self):
        return len(self.heap)
    
    def clear(self):
        self.heap=[]
        self.count=0
        
    def get(self, i):
        (_,_,item)=self.heap[i]
        return item
    