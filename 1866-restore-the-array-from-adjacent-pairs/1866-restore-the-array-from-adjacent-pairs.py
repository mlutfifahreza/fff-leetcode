class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:        
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]

        edge = {}

        for x,y in adjacentPairs:
            if x in edge:
                del edge[x]
            else:
                edge[x] = True
            
            if y in edge:
                del edge[y]
            else:
                edge[y] = True
        
        adj_list = {}
        for x,y in adjacentPairs:
            if x in adj_list:
                adj_list[x].append(y)
            else:
                adj_list[x] = [y]
            
            if y in adj_list:
                adj_list[y].append(x)
            else:
                adj_list[y] = [x]
        
        # print(f"adj_list={adj_list}")

        total_num = len(adjacentPairs) + 1
        result = []
        
        left, right = edge.keys()
        prev_num = left
        curr_num = left
        while curr_num != right:
            result.append(curr_num)
            ajd = adj_list[curr_num]
            for i in range(2):
                # print(ajd)
                if ajd[i] != prev_num:
                    prev_num = curr_num
                    curr_num = ajd[i]
                    # print(f"prev_num, curr_num = {prev_num}, {curr_num}")
                    break
        
        result.append(right)
        return result