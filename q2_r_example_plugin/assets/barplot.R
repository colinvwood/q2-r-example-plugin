#!/usr/bin/env Rscript

library(tidyverse)

read.input.csv <- function(input.table.fp) {
    return( read_csv(input.table.fp) )
}

visualize.sorted.samples <- function(df, visualization.fp) {
    df <- df |>
        rowwise() |>
        mutate( count = sum(c_across(where(is.numeric))) ) |>
        ungroup() |>
        mutate(id = fct(id)) |>
        mutate(id = fct_reorder(id, count, .desc = TRUE))

    plot <- df |>
        ggplot(aes(x = id, y = count)) + geom_bar(stat = "identity")

    plot + theme(axis.text.x = element_text(angle = 90, size = 8))

    ggsave(visualization.fp, device = "svg")

    return(df)
}

if (sys.nframe() == 0) {
    args <- commandArgs(trailingOnly=TRUE)
    input.table.fp <- args[1]
    visualization.fp <- args[2]

    visualize.sorted.samples(read.input.csv(input.table.fp), visualization.fp)
}
