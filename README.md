# Discrete-Convolution
__
Helper Module  to apply convolution over discrete sequences.
### Usage:

```bash
python -m controller <command> <signals>*
``` 
### Options:
- convolution (conv)  convolve two discrete signals:
                        < signalA -> collections.OrderedDict > 
                        < signalB -> collections.OrderedDict >
                        and outputs the convolved signal
    
- plot (plt, p)       plot a set of discrete signals <signal0> <signal1> ... <signaln> represented as python dictionaries


### Examples

- Convolve two signals and plot them
````bash
python -m controller conv "{-2:10,-1:-1,0:4,1:2,2:-3,3:6,4:9}" "{-2:2,-1:-4,0:-5}" -p True
````
- Plot two signal
````bash
python -m controller plot "{-2:10,-1:-1,0:4,1:2,2:-3,3:6,4:9}" "{-2:2,-1:-4,0:-5}" 
````
**Requeriments**
- numpy
- matplotlib
