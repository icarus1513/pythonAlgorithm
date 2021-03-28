import heapq

heap = [] # heap 생성하기
heapq.heappush(heap,1) #원소 추기하기

heap_ex = [3,2,1]
heapq.heapify(heap_ex) ## 리스트 heap처럼 만들기
print(heap_ex[0]) ## 1출력
heap_min = heapq.heappop(heap_ex) # 1 pop 최솟값 얻기

