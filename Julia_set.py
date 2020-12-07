import numpy as np
import imageio
import matplotlib.pyplot as plt



def generate_julia(m, s, n):
    """[summary]

    Args:
        m ([integer]): [image width]
        s ([integer]): [image height]
        n ([integer]): [image scale]
    """
    # Fill llinspace (-m/s x m/s) with m.
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))
    Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
    
    # Computation
    C = np.full((n, m), -0.143 + 0.65j)
    M = np.full((n, m), True, dtype=bool)
    N = np.zeros((n, m))
    for i in range(256):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        N[M] = i
    return N
    
def draw_img(m, n, N, img_path):
    # Save with Matplotlib using a colormap.
    fig = plt.figure()
    fig.set_size_inches(m / 100, n / 100)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(np.flipud(N), cmap='Blues')
    plt.savefig(img_path)
    plt.close()

m = 480
n = 320
s = 300

N = generate_julia(m, s, n)
img_path = 'julia-plt.png'
draw_img(m, n, N, img_path)