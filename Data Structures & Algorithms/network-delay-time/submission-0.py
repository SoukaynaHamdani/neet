class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 1. Build the adjacency list from times: u -> (v, w)
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        # 2. Nodes are 1-indexed (1 to n) and list is only 0->n-1, so allocate size n + 1
        dis = [float("inf")] * (n + 1)
        dis[k] = 0

        pq = [(0, k)]

        while pq:
            cur_dist, node = heapq.heappop(pq)

            #erase
            if cur_dist > dis[node]:
                continue

            for neighbor, edge_weight in adj[node]:
                new_dist = cur_dist + edge_weight
                if new_dist < dis[neighbor]:
                    dis[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        # 4. Max time among nodes 1..n; -1 if any node is unreachable
        max_time = max(dis[1:])
        return max_time if max_time != float("inf") else -1