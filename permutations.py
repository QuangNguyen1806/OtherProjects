from collections import deque

def permutations(lst):
    queue = deque([[]])  
    stack = lst[::-1]    
    while stack:
        current_element = stack.pop()
        current_size = len(queue)

        for _ in range(current_size):
            current_permutation = queue.popleft()
            for i in range(len(current_permutation) + 1):
                new_permutation = current_permutation[:i] + [current_element] + current_permutation[i:]
                queue.append(new_permutation)
    
    return list(queue)

lst = [1, 2, 3, 4]
print(permutations(lst))
