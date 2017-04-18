from itertools import cycle
from matplotlib import colors as mcolors
from matplotlib import pyplot as plt
from numpy import size
import pickle
from scipy.io import loadmat

# fig_contents = loadmat('1-roc.fig', squeeze_me=True, struct_as_record=False)
# matfig = fig_contents['hgS_070000']
# childs = matfig.children

def plot_mat_roc_curve(file_name):
    # Setup plot details
    color_dict = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    color_names = [name for name, color in color_dict.items()]
    colors = cycle(color_names)
    lw = 2

    mat_file = loadmat(file_name, squeeze_me=True, struct_as_record=False)
    plot_data = mat_file['hgS_070000'].children
    if size(plot_data) > 1:
        legs = plot_data[1]
        leg_entries = tuple(legs.properties.String)
        plot_data = plot_data[0]
    else:
        return

    prs = []
    plt.clf()
    counter = 0
    for color,line in zip(colors, plot_data.children):
        if line.type == 'graph2d.lineseries':
            if hasattr(line.properties,'LineStyle'):
                linestyle = "%s" % line.properties.LineStyle
            else:
                linestyle = '--'
                marker_size = 1 
            x = line.properties.XData
            y = line.properties.YData

            plt.plot(x, y, linestyle=linestyle)
            prs.append((x,y))
            counter += 1
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(leg_entries, loc="lower right")
    plt.grid()
    plt.savefig('./' + file_name + '.png')

    with open('./' + file_name + '.file', 'w') as outfile:
        pickle.dump([prs,], outfile)


def main():
    file_name='1-roc.fig'
    plot_mat_roc_curve(file_name),

if __name__ == "__main__":
    main()