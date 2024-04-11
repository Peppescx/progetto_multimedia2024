from vidstab import VidStab
import matplotlib.pyplot as plt

import sys, getopt, os
from pathlib import Path
def main(argv):
	folder=argv[0]
	folder=os.path.split(os.path.abspath(folder))
	print("folder= "+folder[0])
	folder=folder[0]
	try:
		opts, args = getopt.getopt(argv,"hi:o:")
		
		stabilizer = VidStab()
		stabilizer.stabilize(input_path=folder+"/input.mp4", output_path=folder+'/outcpp.avi',border_type='reflect')
		
	
		stabilizer.plot_trajectory()
		
		plt.savefig(folder+"/trajectory.png", format="png", bbox_inches="tight") 
		
		stabilizer.plot_transforms()
		plt.savefig(folder+"/transforms.png", format="png", bbox_inches="tight") 
		#plt.show()

	except getopt.GetoptError:
		sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])
   

