[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.59227.svg)](http://dx.doi.org/10.5281/zenodo.59227)

# GraphEmbed
Compute a 2D embedding of a data matrix given supervised class information.

A discrete label for each instance is expected.
A graph is built where nodes are instances and there exist two types
of edges: the 'knn' edges and the 'k_shift' edges.
A knn edge is an edge to the k-th nearest instance that has the same
label.
A k_shift edge is an edge to the k-th nearest instance that is denser
and has a different label.
The density is defined as the sum of the pairwise cosine similarity between
an instance and all the other instances.
The desired edge length is the euclidean distance between the instances.
If the endpoints of an edge have the same label then the desired distance
is divided by 1 + class_bias.
A k-shift edge is deleted if at least one of the endpoints of is an
outlier.
Outlier nodes are defined as those instances that have no mutual
k=knn_outlier neighbors.

Finally the embedding is computed as the 2D coordinates of the
corresponding graph embedding using the force layout algorithm from
Tomihisa Kamada, and Satoru Kawai. "An algorithm for drawing general
undirected graphs.", Information processing letters 31, no. 1 (1989): 7-15.

<p align="center"><img src="img/img.png"></p>

## Installation

GraphEmbed can be installed via [conda](http://conda.pydata.org/miniconda.html):

```bash
conda install graph_embed -c bioconda
```

## Usage

You can execute the program by typing:

```./graph_embed -i example/prot_expression.csv -t example/target.csv --correlation_transformation```

You can change the strength of the belief in the supervised information. Values higher than 0 indicate a stronger belief and will result in more compact layouts for instances of the same class. Values of 0.5-1 are suitable for clean data where clusters are naturally well separated, values of 5-30 are suitable for noisy data where it is necessary to force a strong separation in the 2D representation. 

To set a desired separation strength:
```./graph_embed -i example/prot_expression.csv -t example/target.csv --correlation_transformation --class_bias 1 ```


## Output

The following files are produced:

```
fname_2D_coords.txt      The 2D coordinates, one line per instance
fname_target.txt         The target identifier (given or predicted), one line per instance 
fname_probs.txt          The probability of each instance to belong to one of the targets, one line per instance.

fname_1_clean.pdf        The image of the 2D embedding.
fname_2_clean_hull.pdf   The image of the 2D embedding with convex hulls.
fname_3.pdf              The image of the 2D embedding with convex hulls and target info.
fname_4_target.pdf       The image of the 2D embedding of the targets.
```

## Help

```
Version: 1.0
Author: Fabrizio Costa [costa@informatik.uni-freiburg.de]

Usage:
  graph_embed -i FILE (-t FILE | -n N)  [-o NAME] [--cmap_name=NAME]
              [(-m N | --min_threshold=N)] [--multi_class_threshold=N]
              [--multi_class_bias=N] [--true_class_threshold=N]
              [--true_class_bias=N] [--nearest_neighbors_threshold=N]
              [--correlation_transformation]
              [--display] [--verbose]
  graph_embed (-h | --help)
  graph_embed --version

Options:
  -i FILE                           Specify input data file.
  -t FILE                           Specify target data file.
  -n N                              Specify the num of classes [default: 1].
  -o NAME                           Prefix for output files [default: out].
  --display                         Display graphs.
  -m N, --min_threshold=N           Min num of elements per class [default: 5].
  --cmap_name=NAME                  Color scheme [default: gist_ncar].
  --correlation_transformation      Convert data matrix to corr coeff matrix.
  --nearest_neighbors_threshold=N   Number of neighbors [default: 5].
  --true_class_bias=N               Bias for clustering [default: 0.9].
  --true_class_threshold=N          Threshold for clusters [default: 3].
  --multi_class_bias=N              Multiclass bias [default: 0].
  --multi_class_threshold=N         Multiclass threshold [default: 3].
  -h --help                         Show this screen.
  --version                         Show version.
  --verbose                         Print more text.

  ```
  
## Sample output pdf files

The image of the 2D embedding.
<p align="center"><img src="img/img_1_clean.png"></p>

The image of the 2D embedding with convex hulls.
<p align="center"><img src="img/img_2_clean_hull.png"></p>

The image of the 2D embedding with convex hulls and target info.
<p align="center"><img src="img/img_3.png"></p>

The image of the 2D embedding of the targets.
<p align="center"><img src="img/img_4_target.png"></p>

