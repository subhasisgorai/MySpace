def alienOrder(words):
        from collections import defaultdict, Counter
        indegree = Counter()
        graph = defaultdict(set)
        letter_set = {letter for word in words for letter in word}
        for index in range(len(words) - 1):
            cur_word = words[index]
            next_word = words[index + 1]
            for cur_letter, next_letter in zip(cur_word, next_word):
                if cur_letter != next_letter:
                    if next_letter not in graph[cur_letter]:
                        graph[cur_letter].add(next_letter)
                        indegree[next_letter] += 1
                    break
            else:
                if len(cur_word) > len(next_word):
                    return ""
        topo_sort = ''
        bfs_list = [node for node in letter_set if indegree[node] == 0]
        while bfs_list:
            node = bfs_list.pop()
            topo_sort += node
            for adj_node in graph[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    bfs_list.append(adj_node)
        return topo_sort if len(topo_sort) == len(letter_set) else ""

    
if __name__ == '__main__':

    def print_result(sample):
        print 'Output for {}:[{}]'.format(sample, alienOrder(sample))
    
    print_result(["wrt", "wrf", "er", "ett", "rftt"])
    print_result(["z", "x"])
    print_result(["z", "x", "z"])
    print_result(["z", "z"])
    print_result(["ab", "adc"])
    print_result(["a", "b", "ca", "cc"])
    print_result(["abc", "ab"])
    print_result(["wrt", "wrtkj"])
    print_result(["ac", "ab", "zc", "zb"])
