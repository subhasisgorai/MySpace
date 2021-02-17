'''
    Recipe for backtracking -
    
    result = []
    def backtrack(Path, Seletion List  ):
        if meet the End Conditon:
            result.add(Path)
            return
    
        for seletion in Seletion List:
            select
            backtrack(Path, Seletion List)
            deselect
'''
from copy import copy

result = list()


def _permute(selection_list, path):
    if len(selection_list) == 1:
        path.append(selection_list[0])
        result.append(''.join(path))
        
        return 
    
    for i, selection in enumerate(selection_list):
        if selection in path:
            continue
        path_copy = copy(path)
        path.append(selection)
        _permute(selection_list[:i] + selection_list[i + 1:], path)
        path = path_copy

        
def compute_permutation(number):
    del result[:]
    _permute(list(str(number)), list())
    return result


if __name__ == '__main__':
    print compute_permutation(1234)
