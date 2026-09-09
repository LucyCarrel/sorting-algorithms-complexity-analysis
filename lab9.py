from trees import TreeNode


class LessThan:

    def __init__(self):
        self.history = []

    def __call__(self, value1, value2):
    
        if value2 < value1:
            value1, value2 = value2, value1
            ls = (value1, value2)
            self.history.append(ls)
            return False
        else:
            ls = (value1, value2)
            self.history.append(ls)
            return True
            
    def report(self):
        result = [tuple(sorted([v1, v2])) for (v1, v2) in self.history]
        self.history = []
        return result

""" 
Oscar's custom-made comparison function. 

Do not delete or change! You'll need this.

"""
lessthan = LessThan()


def bubble_sort(ls):
    """Adapt this code for Question Two ("Adept")."""
    for goal in range(len(ls), 0, -1):
        for baton in range(0, goal - 1):
            # if ls[baton + 1] < ls[baton]:
            if lessthan(ls[baton+1], ls[baton]):
                ls[baton], ls[baton + 1] = ls[baton + 1], ls[baton]


def pivot_sort(ls, choose_pivot = lambda ls: 0):

    less = []
    great = []
    new = []

    if len(ls) <= 1:
        return ls
    
    index = choose_pivot(ls)
    pivot = ls[index]

    for i in range(0,len(ls)):
        if ls[i] != pivot:

            if lessthan(ls[i], pivot) == True:
                less.append(ls[i])
            else:
                great.append(ls[i])

    less = pivot_sort(less, choose_pivot)
    great = pivot_sort(great, choose_pivot)
    new = less + [pivot] + great 
    
    return new 

def quick_sort(ls):
    """This won't work until you implement pivot_sort!"""
    from random import randint

    return pivot_sort(ls, lambda ls: randint(0, len(ls) - 1))


def build_tree(ls):
    if len(ls) == 1:
        return TreeNode(None, ls[0], None)

    else:
        mid = len(ls)//2
        left = ls[:mid]
        right = ls[mid:]
        return TreeNode(build_tree(left),None, build_tree(right))


def merge(ls1, ls2):
    sum = []
    in1 = 0
    in2 = 0

    while (in1 < len(ls1)) and (in2 < len(ls2)):
        if lessthan(ls1[in1],ls2[in2]):
            sum.append(ls1[in1])
            in1 += 1
        else:
            sum.append(ls2[in2])
            in2 += 1

    return sum + ls1[in1:] + ls2[in2:]


def bottom_up_merge(tree):
    if tree.is_leaf():
        return [tree.label]

    else:
        left = bottom_up_merge(tree.left)
        right = bottom_up_merge(tree.right)
        return merge(left, right)

def merge_sort(ls):
    """This won't work until you implement build_tree and bottom_up_merge!"""
    tree = build_tree(ls)
    return bottom_up_merge(tree)


def count_comparisons(sorter, ls):
    lessthan.report()
    sorter(ls)
    return len(lessthan.report())


def plot_efficiency_curve(sorters, max_length, adversarial=False):
    """Oscar and Skeeter's software for measuring efficiency."""
    from random import shuffle
    from matplotlib.pyplot import plot
    from matplotlib import pyplot

    pyplot.clf()
    for sorter in sorters:
        x_coords = list(range(1, max_length + 1))
        y_coords = []
        for x in x_coords:
            ls = list(range(x))
            if not adversarial:
                shuffle(ls)
            y = count_comparisons(sorter, ls)
            y_coords = y_coords + [y]
        plot(x_coords, y_coords, label=sorter.__name__)
    pyplot.legend()
    pyplot.title("Efficiency Curve")
    pyplot.xlabel("Length of list")
    pyplot.ylabel("Number of comparisons")
    pyplot.show()
