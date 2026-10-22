"""Replacement clustering helpers; historical helper was not included."""
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import calinski_harabasz_score, davies_bouldin_score

def _tune(data, k, factory, score_function):
    ks = list(k)
    scores = []
    for n in ks:
        labels = factory(n).fit_predict(data)
        score = score_function(data, labels)
        scores.append(-score if score_function is davies_bouldin_score else score)
    plt.figure()
    plt.plot(ks, scores, marker='o')
    best = max(range(len(scores)), key=scores.__getitem__)
    return {'best_k': ks[best], 'k': ks, 'scores': scores}

def tune_k_means(data, k, n_init=10, score_function=calinski_harabasz_score):
    return _tune(data, k, lambda n: KMeans(n_clusters=n, n_init=n_init, random_state=42), score_function)

def tune_agglomerative_clustering(data, k, score_function=calinski_harabasz_score):
    return _tune(data, k, lambda n: AgglomerativeClustering(n_clusters=n, linkage='ward'), score_function)

def plot_dendrogram(data, **kwargs):
    return dendrogram(linkage(data, method='ward'), **kwargs)
