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

**Requeriments**
- numpy
- matplotlib
