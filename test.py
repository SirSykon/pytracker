import numpy as np
from pytracker.tracker import Tracker
import random
import matplotlib.pyplot as plt


def plot_trace(positions, color, ax):
    ax.scatter(positions[:,0], positions[:,1], color=color)

def plot_tracker(tracker, colors, preffix = "img"):

    fig, ax = plt.subplots(1)
    
    for trace in tracker.get_active_traces():
        trace_id = trace.get_id()
        if not trace_id in colors:
            colors[trace_id] =[random.randint(0,255)/255., random.randint(0,255)/255., random.randint(0,255)/255.]
        color = colors[trace_id]
        
        trace_positions = trace.get_not_None_positions()
        trace_positions = np.array(trace_positions.copy())
        
        plot_trace(trace_positions, color, ax)
        
    plt.savefig(f"./imgs/{preffix}.png")

random.seed = 45


# First simple test. Onlye One short trace.
colors = {}

tracker = Tracker(50,5,1000)

positions = [[0,0], [0,1], [0,2]]

for index, pos in enumerate(positions):

    trace_ids = tracker.assign_incomming_positions(np.array([pos]))
    
    for trace_id in trace_ids:
        if not trace_id in colors:
            colors[trace_id] = (random.randint(0,255)/255., random.randint(0,255)/255., random.randint(0,255)/255.)
    
    plot_tracker(tracker, colors, preffix=f"1_{index}")
    
# Second simple test. Two traces.

tracker = Tracker(50,5,1000)

positions = [[0,0], [0,51], [0,2]]

for index, pos in enumerate(positions):

    trace_ids = tracker.assign_incomming_positions(np.array([pos]))
    
    for trace_id in trace_ids:
        if not trace_id in colors:
            colors[trace_id] = (random.randint(0,255)/255., random.randint(0,255)/255., random.randint(0,255)/255.)
    
    plot_tracker(tracker, colors, preffix=f"2_{index}")
    
    
# Third simple test.

tracker = Tracker(50,5,1000)

positions = [[[0,0], [0,51]],
            [[2,-7], [4,60]],
            [[7,6], [-1,65]],
            [[0,70]],
            [[7,10]],
            [],
            [[15,10], [-5,75]],
            [[-45,-20], [-76,39]],
            [],
            [],
            [],
            [[-50,-20], [-80,39]],
            []
            ]

for index, pos in enumerate(positions):

    trace_ids = tracker.assign_incomming_positions(np.array(pos))
    
    for trace_id in trace_ids:
        if not trace_id in colors:
            colors[trace_id] = (random.randint(0,255)/255., random.randint(0,255)/255., random.randint(0,255)/255.)
    
    plot_tracker(tracker, colors, preffix=f"3_{index}")
