from controller.operators import convolver
from controller.plot import plotter

def run(args):
    X = {-2:10,-1:-1,0:4,1:2,2:-3,3:6,4:9}
    Y = {-2:2,-1:-4,0:-5} 
    z=convolver.conv(X,Y)
    plotter.plot(X=X,Y=Y,Z=z)
    