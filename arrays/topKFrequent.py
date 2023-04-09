  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      d = {}
      for n in nums:
          if n not in d.keys():
              d[n] = 1
          else:
              d[n] += 1
      sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
      return [sorted_dict[i][0] for i in range(k)]
# O(nlogn)
