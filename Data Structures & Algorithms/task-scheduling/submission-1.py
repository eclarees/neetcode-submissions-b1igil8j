class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter 
        from collections import deque 
        taskCounter = Counter(tasks).most_common() 
        maxHeap = [] 
        for task, count in taskCounter:
            heapq.heappush(maxHeap,-count)
        
        print(maxHeap)
        
        time =0 
        queue = deque() #pairs of [-count,idleTime]

        # while there are sitll tasks to process
        while len(maxHeap)>0 or len(queue)>0:
            time +=1 
            if maxHeap:
                # process task 
                count = heapq.heappop(maxHeap)
                # num of tasks reduce by 1 
                updated_count = count+1 

                if updated_count:
                    # Queue to hold waiting tasks , idle time = cur time + n 
                    queue.append((updated_count,time+n))
            # if time to process task in queue 
            if queue and queue[0][1]==time: 
                cnt, time = queue.popleft()
                heapq.heappush(maxHeap,cnt)
        return time
        