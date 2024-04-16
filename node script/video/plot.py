import matplotlib.pyplot as plt
import numpy as np
import sys, getopt, os
from pathlib import Path

def plot_transforms(dx,dy,a,folder,title,radians=False):
 with plt.style.context('ggplot'):
        fig, (ax1, ax2) = plt.subplots(2, sharex='all')

        ax1.plot(dx, label='delta x', color='C0')
        ax1.plot(dy, label='delta y', color='C1')
        ax1.set_ylabel('Delta Pixels', fontsize=10)

        if radians:
            ax2.plot(a, label='delta angle', color='C2')
            ax2.set_ylabel('Delta Radians', fontsize=10)
        else:
            ax2.plot(np.rad2deg(a), label='delta angle', color='C2')
            ax2.set_ylabel('Delta Degrees', fontsize=10)

        handles1, labels1 = ax1.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        fig.legend(handles1 + handles2,
                   labels1 + labels2,
                   loc='upper right',
                   ncol=1)

        plt.xlabel('Frame Number')

        fig.suptitle('Transformations for Stabilizing '+title, x=0.15, y=0.96, ha='left')
        fig.canvas.manager.set_window_title('Transforms')
        plt.savefig(folder+"/transforms.png", format="png", bbox_inches="tight") 

        return fig, (ax1, ax2)


def plot_trajectory(x,y,avg_x,avg_y,folder,title):
    with plt.style.context('ggplot'):
        fig, (ax1, ax2) = plt.subplots(2, sharex='all')

        # x trajectory
        ax1.plot(x, label='Trajectory')
        ax1.plot(avg_x, label='Smoothed Trajectory')
        ax1.set_ylabel('dx')

        # y trajectory
        ax2.plot(y, label='Trajectory')
        ax2.plot(avg_y, label='Smoothed Trajectory')
        ax2.set_ylabel('dy')

        handles, labels = ax2.get_legend_handles_labels()
        fig.legend(handles, labels, loc='upper right')

        plt.xlabel('Frame Number')

        fig.suptitle('Video Trajectory '+title, x=0.15, y=0.96, ha='left')
        fig.canvas.manager.set_window_title('Trajectory')
        plt.savefig(folder+"/trajectory.png", format="png", bbox_inches="tight")       
           
        return fig, (ax1, ax2)
        
def main(argv):
	folder=argv[0]
	folder=os.path.split(os.path.abspath(folder))
	algorithm=argv[1]
	print("folder= "+folder[0])
	print("Algoritmo= "+algorithm)
	title=""
	if algorithm == '1':
	   title=" -Videostab"
	elif algorithm == '2':
	   title=" -Kalman"
	print(title)
	folder=folder[0]
	try:
		opts, args = getopt.getopt(argv,"hi:o:")
		   
		with open(folder+'/trajectory.txt') as f:
		    lines = f.readlines()
		    i = [line.split()[0] for line in lines]
		 
		    x = [float(line.split()[1]) for line in lines]
		      
		    y = [float(line.split()[2]) for line in lines]
		    
		    a = [float(line.split()[3]) for line in lines]
		    #print(str(x)+" "+str(y))

		with open(folder+'/smoothed_trajectory.txt') as f:
		    lines = f.readlines()
		    i1 = [line.split()[0] for line in lines]
		 
		    avg_x = [float(line.split()[1]) for line in lines]
		      
		    avg_y = [float(line.split()[2]) for line in lines]
		    
		    avg_a = [float(line.split()[3]) for line in lines]
		    #print(str(x)+" "+str(y))

		with open(folder+'/prev_to_cur_transformation.txt') as f:
		    lines = f.readlines()
		    k = [line.split()[0] for line in lines]
		 
		    dx = [float(line.split()[1]) for line in lines]
		      
		    dy = [float(line.split()[2]) for line in lines]
		    
		    a = [float(line.split()[3]) for line in lines]
		    #print(str(x)+" "+str(y))

		with open(folder+'/new_prev_to_cur_transformation.txt') as f:
		    lines = f.readlines()
		    i2 = [line.split()[0] for line in lines]
		 
		    dx1 = [float(line.split()[1]) for line in lines]
		      
		    dy1 = [float(line.split()[2]) for line in lines]
		    
		    da1 = [float(line.split()[3]) for line in lines]
		    #print(str(x)+" "+str(y))
		    plot_trajectory(x,y,avg_x,avg_y,folder,title)
		    plot_transforms(dx,dy,a,folder,title)



	except getopt.GetoptError:
		sys.exit(2)
if __name__ == "__main__":
   main(sys.argv[1:])





        




