# python-rle

Run-length encoding [(wikipedia link)](https://en.wikipedia.org/wiki/Run-length_encoding) for data analysis in Python. Install with `pip install python-rle`. No dependencies required other than `tqdm` for visualizing a progress bar. 

## Usage

Encode any iterable (tuples, lists, pd.Series etc.) with `rle.encode`.

```
# rle.encode(iterable) returns (values, counts)
>>> import rle 
>>> rle.encode((10, 10, 10, 20, 20, 20, 30, 30, 30))
([10, 20, 30], [3, 3, 3])
```

Decode (values, counts) back into a sequence with `rle.decode`.
```
>>> rle.decode([10, 20, 30], [3, 3, 3])
[10, 10, 10, 20, 20, 20, 30, 30, 30]
```

Set `progress_bar` == `True` for long sequences :

![progress_bar_anim](progress_bar.svg)

## Motivation

Base R contains a simple `rle` function that "computes the lengths and values of runs of equal values in a vector", as described by its docstring. I found it useful for calculating streaks in collected data, and is especially wonderful for compiling and summarizing categorical data that describes status over time. Hence this little utility.

<!--
## Reference to `rle` in R

``` r
> rle
function (x) 
{
    if (!is.vector(x) && !is.list(x)) 
        stop("'x' must be a vector of an atomic type")
    n <- length(x)
    if (n == 0L) 
        return(structure(list(lengths = integer(), values = x), 
            class = "rle"))
    y <- x[-1L] != x[-n]
    i <- c(which(y | is.na(y)), n)
    structure(list(lengths = diff(c(0L, i)), values = x[i]), 
        class = "rle")
} 
```

-->
