import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from circle import Circle
from container import Container
from placement import Placement

def visualise_solution(container, radii, weights, solution, title="Solution", save_path=None):

    # Create circles and place them
    circles = [Circle(r,w) for r,w in zip(radii,weights)]
    placement = Placement(circles, container)
    placement.place_from_chromosome(solution)

    # Create figure
    fig, ax = plt.subplots(figsize = (10,10))
    ax.set_facecolor('#01364C')
    fig.patch.set_facecolor('#01364C')

    # Draw container boundary
    container_rect = mpatches.Rectangle(
        (0,0), container.width, container.height,
        fill=False, edgecolor = '#F4BA02', linewidth=3, linestyle= '--'
    )
    ax.add_patch(container_rect)

#
    com_rect = mpatches.Rectangle(
        (0.2 * container.width, 0.2 * container.height),
        0.6 * container.width, 0.6 * container.height,
        fill=False, edgecolor = '#F4BA02', linewidth=2, linestyle= ':', alpha = 0.5
    )
    ax.add_patch(com_rect)

# Draw circles 

    for i, circle in enumerate(circles):
        if circle.placed:
            circle_patch = mpatches.Circle(
            (circle.x, circle.y), circle.radius,
            facecolor = '#99D9DD', edgecolor= '#F7F8F9', linewidth=2, alpha=0.7
            )
            ax.add_patch(circle_patch)

            ax.text(circle.x, circle.y, str(i),
                    ha='center', va='center', color='#01364C',
                    fontsize=10, fontweight = 'bold')
            
        
    placed = [c for c in circles if c.placed]
    if placed:
        total_weight = sum(c.weight for c in placed)
        com_x = sum(c.x * c.weight for c in placed) / total_weight
        com_y = sum(c.y * c.weight for c in placed) / total_weight

        ax.plot(com_x, com_y, 'x', color = '#F4BA02', markersize=15,
                markeredgewidth=3, label='Center of Mass')
    
    # Set limits and labels 
    margin = max(container.width, container.height) * 0.1
    ax.set_xlim(-margin, container.width + margin)
    ax.set_ylim(-margin, container.height + margin)
    ax.set_aspect('equal')
    ax.set_xlabel('Width (m)', color = '#F7F8F9', fontsize=12)
    ax.set_ylabel('Width (m)', color = '#F7F8F9', fontsize=12)
    ax.set_title(title, color = '#F7F8F9', fontsize=14, fontweight= 'bold', pad=20)

    # Style Axis
    ax.tick_params(colors='#F7F8F9')
    for spine in ax.spines.values():
        spine.set_edgecolor('#F7F8F9')
    
    # Add legend
    ax.legend(loc='upper right', facecolor = '#01364C', edgecolor= '#F7F8F9',
    labelcolor = '#F7F8F9', framealpha=0.9)
    
    # Grid
    ax.grid(True, alpha=0.2, color='#F7F8F9')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, facecolor= '#01364C', dpi=150)
        print(f"saved visualisation to {save_path}")
    else: plt.show()

    plt.close()

if __name__ == "__main__":
    from container_instances import create_basic_instances

    inst = create_basic_instances()[0]
    container = Container(inst.container.width, inst.container.depth, inst.container.max_weight)
    radii = [c.diameter / 2 for c in inst.cylinders]
    weights = [c.weight for c in inst.cylinders]
    solution = [0,2,1]

    visualise_solution(container, radii, weights, solution,
                       title = "Instance 1: Three Identical Cylinders",
                       save_path = "Instance_1.png")
                        



