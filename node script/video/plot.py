import matplotlib.pyplot as plt
import numpy as np

with open('trajectory.txt') as f:
    lines = f.readlines()
    i = [line.split()[0] for line in lines]
 
    x = [float(line.split()[1]) for line in lines]
      
    y = [float(line.split()[2]) for line in lines]
    
    a = [float(line.split()[3]) for line in lines]
    #print(str(x)+" "+str(y))

with open('smoothed_trajectory.txt') as f:
    lines = f.readlines()
    i1 = [line.split()[0] for line in lines]
 
    x1 = [float(line.split()[1]) for line in lines]
      
    y1 = [float(line.split()[2]) for line in lines]
    
    a1 = [float(line.split()[3]) for line in lines]
    #print(str(x)+" "+str(y))

with open('prev_to_cur_transformation.txt') as f:
    lines = f.readlines()
    i2 = [line.split()[0] for line in lines]
 
    x2 = [float(line.split()[1]) for line in lines]
      
    y2 = [float(line.split()[2]) for line in lines]
    
    a2 = [float(line.split()[3]) for line in lines]
    #print(str(x)+" "+str(y))

with open('new_prev_to_cur_transformation.txt') as f:
    lines = f.readlines()
    i3 = [line.split()[0] for line in lines]
 
    x3 = [float(line.split()[1]) for line in lines]
      
    y3 = [float(line.split()[2]) for line in lines]
    
    a3 = [float(line.split()[3]) for line in lines]
    #print(str(x)+" "+str(y))



def plot_transforms(x2,x3,y2,y3,a2,a3 ,radians=False):
 with plt.style.context('ggplot'):
        fig, (ax1, ax2) = plt.subplots(2, sharex='all')

        ax1.plot(x2, label='delta x', color='C0')
        ax1.plot(y2, label='delta y', color='C1')
        ax1.set_ylabel('Delta Pixels', fontsize=10)

        if radians:
            ax2.plot(a2, label='delta angle', color='C2')
            ax2.set_ylabel('Delta Radians', fontsize=10)
        else:
            ax2.plot(np.rad2deg(a2), label='delta angle', color='C2')
            ax2.set_ylabel('Delta Degrees', fontsize=10)

        handles1, labels1 = ax1.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        fig.legend(handles1 + handles2,
                   labels1 + labels2,
                   loc='upper right',
                   ncol=1)

        plt.xlabel('Frame Number')

        fig.suptitle('Transformations for Stabilizing', x=0.15, y=0.96, ha='left')
        fig.canvas.manager.set_window_title('Transforms')
        plt.savefig("Transformations.png", format="png", bbox_inches="tight") 

        return fig, (ax1, ax2)


def plot_trajectory(x,x1,y,y1):
  

    with plt.style.context('ggplot'):
        fig, (ax1, ax2) = plt.subplots(2, sharex='all')

        # x trajectory
        ax1.plot(x, label='Trajectory')
        ax1.plot(x1, label='Smoothed Trajectory')
        ax1.set_ylabel('dx')

        # y trajectory
        ax2.plot(y, label='Trajectory')
        ax2.plot(y1, label='Smoothed Trajectory')
        ax2.set_ylabel('dy')

        handles, labels = ax2.get_legend_handles_labels()
        fig.legend(handles, labels, loc='upper right')

        plt.xlabel('Frame Number')

        fig.suptitle('Video Trajectory', x=0.15, y=0.96, ha='left')
        fig.canvas.manager.set_window_title('Trajectory')
        plt.savefig("trajectory.png", format="png", bbox_inches="tight")       
           
        return fig, (ax1, ax2)
        

plot_trajectory(x,x1,y,y1)
plot_transforms(x2,x3,y2,y3,a2,a3)



