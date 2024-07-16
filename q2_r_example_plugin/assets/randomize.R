#!/usr/bin/env Rscript

library(tidyverse)

read.input.csv <- function(input.table.fp) {
    return( read_csv(input.table.fp) )
}

write.output.csv <- function(df, output.table.fp) {
    write_csv(df, output.table.fp)
}

randomize <- function(df) {
    for (col in names(df)) {
        if ( !is.character(df[[col]]) ) {
            df[[col]] <- sample(1:1000, nrow(df), replace=TRUE)
        }
    }

    return(df)
}

if (sys.nframe() == 0) {
    args <- commandArgs(trailingOnly=TRUE)
    input.table.fp <- args[1]
    output.table.fp <- args[2]

    randomized.df <- randomize(read.input.csv(input.table.fp))
    write.output.csv(randomized.df, output.table.fp)
}
