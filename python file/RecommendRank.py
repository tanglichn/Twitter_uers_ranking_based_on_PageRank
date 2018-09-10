def RecommendRank(G, alpha, root, max_step):
    rank = dict()
    rank = {x: 0 for x in G.keys()}
    rank[root] = 1
    # Start iteration
    for k in range(max_step):
        tmp = {x: 0 for x in G.keys()}
        # Take node i and its out-side tail nodes set ri
        for i, ri in G.items():
            # Take the tail node j of the outgoing edge of node i and the weight wij of
            # edge E(i,j), the weight of each edge is 1, which does not work here.
            for j, wij in ri.items():
                # i is the first node of one of the edges of j, so need to traverse the
                # graph to find the first node of the incoming edge of j.
                # This traversal process is the 2 layer for loop here.
                tmp[j] += alpha * rank[i] / (1.0 * len(ri))
        # Every time to walk, we start from the root node,
        # so the weight of the root node needs to be added (1 - alpha).
        tmp[root] += (1 - alpha)
        rank = tmp

        # Output the weight of each node after each iteration
        print('iter: ' + str(k) + "\t"),
        for key, value in rank.items():
            print("%s:%.3f, \t" % (key, value)),
        print()

    return rank


if __name__ == '__main__':
    G = {'A': {'a': 1, 'c': 1},
         'B': {'a': 1, 'b': 1, 'c': 1, 'd': 1},
         'C': {'c': 1, 'd': 1},
         'a': {'A': 1, 'B': 1},
         'b': {'B': 1},
         'c': {'A': 1, 'B': 1, 'C': 1},
         'd': {'B': 1, 'C': 1}}
    items_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

    rank = RecommendRank(G, 0.85, 'A', 100)
    for k in items_dict.keys():
        if k in rank:
            items_dict[k] = rank[k]
        # sort:
    result = sorted(items_dict.items(), key=lambda d: d[1], reverse=True)
    print("\nThe result:")
    for k in result:
        print("%s:%.3f \t" % (k[0], k[1])),
    print()

