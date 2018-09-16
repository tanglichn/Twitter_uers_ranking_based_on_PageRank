# Twitter_uers_ranking_based_on_PageRank

1. All the algorithm code are write by python 3.7 and they are in the “python file”

2. The packages the algorithm used show below:

matplotlib
networkx
os
time
pygraph-graph-core
collections
numpy

3. In the file “test dataset”, there are 6 txt documents which is for testing algorithms

4. Implementation (it is better to run in PyCharm):

1) Test PageRank: copy the file path of “network_PageRank.txt” and paste in the “pagerank.py” and  “pagerank_original.py”. Compare the two results
2) Test HITS: copy the file path of “network_HITS.txt” and paste in the “HITS.py” and  “HITS_original.py”. Compare the two results
3) Test GlobalRank: copy the four file path of “network_follow.txt”, “network_reply.txt”,  “network_retweet.txt” and “network_mention.txt” and paste in the “pagerank.py”, implement four times to get four results and sum of those results.   Additionally, copy the four file path of “network_follow.txt”, “network_reply.txt”,  “network_retweet.txt” and “network_mention.txt” and paste in the “GlobalRank.py”, implement it once .  Compare the sum.
                         
4) Test RecommendRank: just run this algorithm, and see the result, because I add the graph in the code. 

5. Compare the performance of PageRank and HITS in twitter 

Step one: The dataset can download from “https://snap.stanford.edu/data/ego-Twitter.html" the file name is “twitter_combined.txt.gz”
Step two: copy the file and run of them.
Note: the time of running would be quite long, because the dataset is very big.

6. Implement GlobalRank in Twitter
Step one: The dataset can download from “https://snap.stanford.edu/data/higgs-twitter.html" they are edgelist format, we can paste the file path in the next line code “g = nx.read_weighted_edgelist()” to read those file. 
Note: we should make the “g = G.init_graph()” become comments. 
      the time of running would be quite long, because the dataset is very big.

7. copy file path paste in the "Draw.py" and run can visulise the direated graph.
