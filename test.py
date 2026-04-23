111111111111111111111
data = {
    "nominal": ["male","female","male"],
    "ordinal": ["A","B","A"],
    "discrete": [2,4,6],
    "continuous": [160.5,165.2,170.1],
    "interval": [36.5,37.0,38.2],
    "ratio": [18,19,20]
}

# Functions
def mean(d): return sum(d)/len(d)

def median(d):
    d = sorted(d)
    n = len(d)
    m = n // 2
    return d[m] if n%2 else (d[m] + d[m-1]) / 2

def mode(d):
    return max(set(d), key=d.count)

def var(d):
    m = mean(d)
    return sum((x-m)**2 for x in d) / len(d)   # simpler

def sd(d):
    return var(d) ** 0.5

# Processing
for k, v in data.items():
    print("\n", k.upper())

    if k == "nominal":
        print("Mode:", mode(v))

    elif k == "ordinal":
        print("Median:", median(v))
        print("Mode:", mode(v))

    else:
        print("Mean:", mean(v))
        print("Median:", median(v))
        print("Mode:", mode(v))
        print("Variance:", var(v))
        print("Std Dev:", sd(v))

2222222222222222222
# Training data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Step 1: Initialize most specific hypothesis
h = ['0'] * (len(data[0]) - 1)

# Step 2: Apply Find-S
for example in data:
    if example[-1] == 'Yes':   # consider only positive examples
        for i in range(len(h)):
            if h[i] == '0':
                h[i] = example[i]
            elif h[i] != example[i]:
                h[i] = '?'

# Final hypothesis
print("Final Hypothesis:", h)

3333333333333
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initialize
S = ['0'] * (len(data[0]) - 1)
G = [['?'] * (len(data[0]) - 1)]

for example in data:
    if example[-1] == 'Yes':   # Positive
        # Update S
        for i in range(len(S)):
            if S[i] == '0':
                S[i] = example[i]
            elif S[i] != example[i]:
                S[i] = '?'
        
        # Remove inconsistent G
        G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(len(S)))]

    else:   # Negative
        new_G = []
        for g in G:
            for i in range(len(S)):
                if g[i] == '?':
                    if S[i] != example[i]:
                        temp = g.copy()
                        temp[i] = S[i]
                        new_G.append(temp)
        
        # Remove duplicates
        G = []
        for g in new_G:
            if g not in G:
                G.append(g)

print("S:", S)
print("G:", G)

444444444444444444444
import numpy as np

# Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# Data (XOR)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(0)

# Weights
w1 = np.random.rand(2,2)
w2 = np.random.rand(2,1)

lr = 0.5   # slightly higher learning rate

# Training
for _ in range(50000):   # increase iterations
    # Forward
    h = sigmoid(np.dot(X, w1))
    o = sigmoid(np.dot(h, w2))
    
    # Error
    error = y - o
    
    # Backprop
    d2 = error * sigmoid_deriv(o)
    d1 = d2.dot(w2.T) * sigmoid_deriv(h)
    
    # Update
    w2 += h.T.dot(d2) * lr
    w1 += X.T.dot(d1) * lr

# Output
print("Final Output:\n", o)

55555555555555555555555
import random
import math

# 2D data points
data = [(1,2), (2,3), (3,3), (6,5), (7,7), (8,6)]

k = 2  # number of clusters

# Step 1: Initialize centroids randomly
centroids = random.sample(data, k)

for _ in range(5):  # iterations
    clusters = [[] for _ in range(k)]
    
    # Step 2: Assign points to nearest centroid
    for point in data:
        distances = []
        for c in centroids:
            d = math.sqrt((point[0]-c[0])**2 + (point[1]-c[1])**2)
            distances.append(d)
        
        index = distances.index(min(distances))
        clusters[index].append(point)
    
    # Step 3: Update centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            x_mean = sum(p[0] for p in cluster) / len(cluster)
            y_mean = sum(p[1] for p in cluster) / len(cluster)
            new_centroids.append((x_mean, y_mean))
    
    centroids = new_centroids

# Output
print("Clusters:", clusters)
print("Centroids:", centroids)
666666666666666666666
import math

# Training data: (x, y, class)
data = [
    (1,2,'A'),
    (2,3,'A'),
    (3,3,'A'),
    (6,5,'B'),
    (7,7,'B'),
    (8,6,'B')
]

# Test point
test = (4,4)
k = 3

# Step 1: Calculate distance
distances = []
for point in data:
    d = math.sqrt((point[0]-test[0])**2 + (point[1]-test[1])**2)
    distances.append((d, point[2]))

# Step 2: Sort
distances.sort()

# Step 3: Take k nearest
neighbors = distances[:k]

# Step 4: Majority vote
count = {}
for n in neighbors:
    label = n[1]
    count[label] = count.get(label, 0) + 1

result = max(count, key=count.get)

# Output
print("Neighbors:", neighbors)
print("Classified as:", result)


777777777777777777777
import math

# Dataset
data = [
    ["Sunny","Hot","High","Weak","No"],
    ["Sunny","Hot","High","Strong","No"],
    ["Overcast","Hot","High","Weak","Yes"],
    ["Rain","Mild","High","Weak","Yes"]
]

attributes = ["Outlook","Temperature","Humidity","Wind"]

# Entropy function
def entropy(dataset):
    total = len(dataset)
    yes = sum(1 for row in dataset if row[-1] == "Yes")
    no = total - yes
    
    def calc(p):
        return 0 if p == 0 else -p * math.log2(p)
    
    return calc(yes/total) + calc(no/total)

# Information Gain
def info_gain(dataset, index):
    total_entropy = entropy(dataset)
    total = len(dataset)
    
    values = set(row[index] for row in dataset)
    weighted_entropy = 0
    
    for v in values:
        subset = [row for row in dataset if row[index] == v]
        weighted_entropy += (len(subset)/total) * entropy(subset)
    
    return total_entropy - weighted_entropy

# Calculate entropy
print("Total Entropy:", entropy(data))

# Calculate info gain for each attribute
gains = []
for i in range(len(attributes)):
    g = info_gain(data, i)
    gains.append(g)
    print("Info Gain(", attributes[i], ") =", g)

# Best attribute
best = gains.index(max(gains))
print("\nBest Attribute (Root Node):", attributes[best])
or 
import math

data = [
    ["Sunny","Hot","High","Weak","No"],
    ["Sunny","Hot","High","Strong","Yes"],
    ["Sunny","Mild","High","Weak","Yes"],
    ["Rain","Mild","High","Weak","No"],
    ["Rain","Cool","Normal","Weak","Yes"],
    ["Overcast","Hot","High","Weak","Yes"]
]
attributes = ["Outlook","Temperature","Humidity","Wind"]

# Entropy
def entropy(dataset):
    total = len(dataset)
    yes = sum(1 for r in dataset if r[-1]=="Yes")
    no = total - yes
    def f(p): return 0 if p==0 else -p*math.log2(p)
    return f(yes/total) + f(no/total)

# Info Gain
def info_gain(dataset, i):
    total = len(dataset)
    vals = set(r[i] for r in dataset)
    we = 0
    for v in vals:
        sub = [r for r in dataset if r[i]==v]
        we += (len(sub)/total) * entropy(sub)
    return entropy(dataset) - we

# Build Tree (recursive)
def build(dataset, attrs):
    labels = [r[-1] for r in dataset]
    
    # If all same → leaf
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    # If no attributes → majority
    if not attrs:
        return max(set(labels), key=labels.count)
    
    # Choose best attribute
    gains = [info_gain(dataset, i) for i in attrs]
    best = attrs[gains.index(max(gains))]
    
    tree = {attributes[best]: {}}
    
    values = set(r[best] for r in dataset)
    for v in values:
        subset = [r for r in dataset if r[best]==v]
        new_attrs = [i for i in attrs if i != best]
        tree[attributes[best]][v] = build(subset, new_attrs)
    
    return tree

# Build and print tree
tree = build(data, list(range(len(attributes))))
print(tree)
