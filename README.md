# GraphEmbed
Compute a 2D embedding of a data matrix given supervised class information.

Instances are materialized as nodes in a graph where edges connect the
nearest neighbors. Additional invisible nodes are placed to represent the
supervised classes and instances are linked to their respective classes.
The final embedding is obtained using the spring layout algorithm presented in:
Tomihisa Kamada, and Satoru Kawai. "An algorithm for drawing general
undirected graphs." Information processing letters 31, no. 1 (1989): 7-15.


## Usage

Standalone script usage:

```./graph_embed -i data.csv -t target.csv --fast```


## Help

```
Version: 1.0
Author: Fabrizio Costa [costa@informatik.uni-freiburg.de]

Usage:
  graph_embed -i FILE -t FILE  [-o NAME] [--fast] [--cmap_name=NAME]
              [(-m N | --min_threshold=N)] [--multi_class_threshold=N]
              [--multi_class_bias=N] [--true_class_threshold=N]
              [--true_class_bias=N] [--nearest_neighbors_threshold=N]
              [--display] [--verbose]
  graph_embed (-h | --help)
  graph_embed --version

Options:
  -i FILE                           Specify input data file.
  -t FILE                           Specify target data file.
  -o NAME                           Prefix for output files [default: draw].
  --fast                            Use fast but approximate computation.
  --display                         Display graphs.
  -m N, --min_threshold=N           Minimum number of elements [default: 5].
  --cmap_name=NAME                  String with color scheme [default: Set3].
  --nearest_neighbors_threshold=N   Number of neighbors [default: 4].
  --true_class_bias=N               Bias for clustering [default: 0.6].
  --true_class_threshold=N          Threshold for clusters [default: 0.005].
  --multi_class_bias=N              Multiclass bias [default: 0.6].
  --multi_class_threshold=N         Multiclass threshold [default: 0.001].
  -h --help                         Show this screen.
  --version                         Show version.
  --verbose                         Print more text.
  ```
