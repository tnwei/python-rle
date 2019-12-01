# pyrle (Work in Progress!)

Run-length encoding [(wikipedia link)](https://en.wikipedia.org/wiki/Run-length_encoding) for data analysis in Python. 

<!-- Include installation on pip and also dependencies--> 

## Usage

<!-- Simple code example will do! Takes any iterable as input: tuples, lists, and most importantly for data people, pd Series-->

## Motivation

Base R contains a simple `rle` function that "computes the lengths and values of runs of equal values in a vector", as described by its docstring. I found it useful for calculating streaks in collected data, and is especially wonderful for compiling and summarizing categorical data that describes status over time. I wasn't able to find an implementation of this in Python, other than the myriad of code examples that use run-length encoding to demonstrate data compression. Hence this little utility.

<!--
## Reference to `rle` in R

Literally just implementing the following! Probably with more bells and whistles.

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
