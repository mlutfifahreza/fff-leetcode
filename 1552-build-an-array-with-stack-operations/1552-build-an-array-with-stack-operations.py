class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_idx = 0
        target_count = 0
        target_len = len(target)
        i = 1
        actions = []
        while i <= n:
            if target[target_idx] == i:
                actions.append("Push")
                target_idx += 1
                target_count += 1
                if target_count == target_len:
                    return actions
            else:
                actions.extend(["Push", "Pop"])
            # print(f"i={i}, actions={actions}")
            i += 1
            
        return actions