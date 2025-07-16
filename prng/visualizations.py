
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

def plot_unit_square_and_cube(data, label):
    """
    Creates a side-by-side matplotlib plot showing:
    1. A 2D scatter of U_i vs U_{i+1} (Unit Square)
    2. A 3D scatter of U_i, U_{i+1}, U_{i+2} (Unit Cube)
    Used to visualize sequential randomness.
    """
    fig = plt.figure(figsize=(12, 5))

    # Unit Square plot
    ax1 = fig.add_subplot(1, 2, 1)
    x = data[:-1]
    y = data[1:]
    ax1.scatter(x, y, s=2)
    ax1.set_xlabel('U_i')
    ax1.set_ylabel('U_{i+1}')
    ax1.set_title(f'{label} - Unit Square')

    # Unit Cube plot
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.scatter(data[:-2], data[1:-1], data[2:], s=1)
    ax2.set_xlabel('U_i')
    ax2.set_ylabel('U_{i+1}')
    ax2.set_zlabel('U_{i+2}')
    ax2.set_title(f'{label} - Unit Cube')

    plt.tight_layout()
    return fig

def plot_benchmark_results(timings):
    """
    Creates a simple bar chart of runtime durations for each generator,
    as measured by `benchmark_generators`.
    """
    import matplotlib.pyplot as plt

    generators = list(timings.keys())
    times = list(timings.values())

    plt.figure(figsize=(8, 5))
    plt.bar(generators, times, color='skyblue')
    plt.ylabel('Time (seconds)')
    plt.title('Benchmark of PRNG Generation Times')
    plt.show()

def plot_unit_square_and_cube_interactive(data, label):
    """
    Creates interactive Plotly versions of the Unit Square and Unit Cube
    visualizations. Allows for rotation, zooming, and inspection of data patterns.
    """
    x = np.array(data[:-1])
    y = np.array(data[1:])
    z = np.array(data[2:])

    # 2D Scatter plot
    fig2d = go.Figure()
    fig2d.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(size=3)))
    fig2d.update_layout(title=f'{label} - Interactive Unit Square',
                        xaxis_title='U_i',
                        yaxis_title='U_{i+1}')

    # 3D Scatter plot
    fig3d = go.Figure()
    fig3d.add_trace(go.Scatter3d(x=x, y=y, z=z,
                                 mode='markers',
                                 marker=dict(size=2)))
    fig3d.update_layout(title=f'{label} - Interactive Unit Cube',
                        scene=dict(xaxis_title='U_i',
                                   yaxis_title='U_{i+1}',
                                   zaxis_title='U_{i+2}'))

    return fig2d, fig3d
