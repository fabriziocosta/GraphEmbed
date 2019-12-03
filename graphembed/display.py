#!/usr/bin/env python
"""Provides interactive drawing for the embedding."""

from ipywidgets import interactive, fixed
from ipywidgets import FloatSlider, IntSlider, ToggleButtons
from ipywidgets import HBox, VBox
from graph_layout_embedder import GraphEmbedder
import time
import datetime
import logging
import random
import numpy as np
from toolz import memoize
from toolz import concat

logger = logging.getLogger(__name__)


def _sample(data_matrix, frac):
    n = data_matrix.shape[0]
    ids = list(range(n))
    m = int(n * frac)
    m = max(m, 3)
    rids = np.array(sorted(random.sample(ids, m)))
    return data_matrix[rids]


@memoize(key=lambda args, kwargs:
         (np.sum(kwargs['data_matrix']),
          kwargs['frac']))
def _subsample_data(data_matrix=None, true_target=None, frac=None):
    if frac == 1:
        d = data_matrix
        t = true_target
    else:
        d = []
        t = []
        for target in set(true_target):
            dat = [x for y, x in zip(true_target, data_matrix)
                   if y == target]
            dat = np.vstack(dat)
            dat = _sample(dat, frac)
            d.append(dat)
            t.append([target] * dat.shape[0])
        d = np.vstack(d)
        t = list(concat(t))
    return d, t


def _display_graph_embedder(data_matrix,
                            target_dict,
                            true_target,
                            mode,
                            bias,
                            outliers,
                            size,
                            k,
                            shift,
                            horizon,
                            frac):
    start = time.time()
    cmap_name = 'gist_ncar'
    file_name = 'img'
    ge = GraphEmbedder(class_bias=bias,
                       k=k,
                       k_quick_shift=shift,
                       knn_horizon=horizon,
                       k_outliers=outliers,
                       metric='cosine')
    d, t = _subsample_data(data_matrix=data_matrix,
                           true_target=true_target,
                           frac=frac)
    ge.transform(d, t)
    if mode == 'default':
        ge.display(target_dict=target_dict,
                   display_outliers=True,
                   cmap=cmap_name,
                   file_name=file_name,
                   figure_size=size,
                   save_figure=False)
    elif mode == 'links':
        ge.display_links(target_dict=target_dict,
                         display_outliers=True,
                         cmap=cmap_name,
                         file_name=file_name,
                         figure_size=size,
                         save_figure=False)
    elif mode == 'hull_link':
        ge.display_hull_link(target_dict=target_dict,
                             true_target=t,
                             remove_outer_layer=False,
                             cmap=cmap_name,
                             file_name=file_name,
                             figure_size=size,
                             save_figure=False)
    elif mode == 'hull':
        ge.display_hull(target_dict=target_dict,
                        true_target=t,
                        remove_outer_layer=False,
                        cmap=cmap_name,
                        file_name=file_name,
                        figure_size=size,
                        save_figure=False)
    delta_time = datetime.timedelta(seconds=(time.time() - start))
    logger.debug('Elapsed: %s' % (str(delta_time)))


def interactive_widget(data_matrix, target_dict, true_target):
    """interactive_widget."""
    w = interactive(
        _display_graph_embedder,
        data_matrix=fixed(data_matrix),
        target_dict=fixed(target_dict), true_target=fixed(true_target),
        mode=ToggleButtons(
            options=['default', 'links', 'hull', 'hull_link'],
            description='Display:',
            disabled=False,
            button_style='',  # 'success', 'info', 'warning', 'danger' or ''
            tooltip='default'),
        bias=FloatSlider(
            min=0.0, max=40.0, step=0.1, value=1.0, continuous_update=False),
        outliers=IntSlider(
            min=0, max=20, step=1, value=0, continuous_update=False),
        size=IntSlider(
            min=7, max=20, step=1, value=12, continuous_update=False),
        k=IntSlider(
            min=1, max=10, step=1, value=5, continuous_update=False),
        shift=IntSlider(
            min=1, max=10, step=1, value=1, continuous_update=False),
        horizon=IntSlider(
            min=0, max=50, step=1, value=10, continuous_update=False),
        frac=FloatSlider(
            min=0.01, max=1.0, step=0.01, value=1.0, continuous_update=False)
    )
    int_w = VBox([HBox((w.children[0],)),
                  HBox(w.children[1:4]),
                  HBox(w.children[4:7]),
                  HBox(w.children[7:])])
    return int_w
    # return w
