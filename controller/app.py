import sys
import ast
import argparse
from collections import OrderedDict
from controller.operators import convolver
from controller.plot import plotter

def convolve(options):
    signalA=OrderedDict(ast.literal_eval(options.signalA))
    signalB=OrderedDict(ast.literal_eval(options.signalB))
    z=convolver.conv(signalA,signalB)
    print(z)
    if options.plot:
        plotter.plot(SignalA=signalA,SignalB=signalB,ResultSignal=z)
def plot(options):
    kwargs={f'Signal{i}':OrderedDict(ast.literal_eval(options.signals[i])) 
            for i in range(len(options.signals))}
    plotter.plot(**kwargs)

def run(args):
    #X = {-2:10,-1:-1,0:4,1:2,2:-3,3:6,4:9}
    #X = dict(enumerate(np.sin(range(-10,10))))
    #Y = {-2:2,-1:-4,0:-5} 
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    # Create a convolution subcommand 
    parser_convolution = subparsers.add_parser('convolution',aliases=["conv"], 
                                               help='convolve two discrete signals < signalA -> collections.OrderedDict > < signalB -> collections.OrderedDict >and outputs the convolved signal')
    parser_convolution.add_argument('signalA',help="A Discrete signal to be convolved represented as collections.OrderedDict")
    parser_convolution.add_argument('signalB',help="A Discrete signal to be convolved represented as collections.OrderedDict")
    parser_convolution.add_argument('-plot', '-p', help="plot the input and output signals",default=False)
    parser_convolution.set_defaults(func=convolve)
    
    #create a downloa subcommand
    parser_plot = subparsers.add_parser('plot',aliases=["plt","p"],
                                            help='plot a set of discrete signals')
    parser_plot.add_argument('signals',nargs='+',help='Signals to be plotted requiers >=1')
    parser_plot.set_defaults(func=plot)


    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)
    