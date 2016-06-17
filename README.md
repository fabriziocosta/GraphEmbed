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
