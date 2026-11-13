class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1
        
        for i in map.keys():
            heapq.heappush(pq, (-map[i], i))

        res = []
        while k > 0:
            res.append(heapq.heappop(pq)[1])
            k-=1

        return res