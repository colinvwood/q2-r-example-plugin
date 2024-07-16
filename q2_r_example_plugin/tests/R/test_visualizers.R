library(testthat)

test_that('visualize sorted samples works', {
    source('../../assets/barplot.R')

    testdir <- tempdir()
    visualization.fp <- file.path(testdir, 'figure.svg')

    df <- tibble(
        id = c("s1", "s2", "s3"),
        feat1 = c(10, 0, 9),
        feat2 = c(100, 3, 4)
    )
    processed.df <- visualize.sorted.samples(df, visualization.fp)
    unlink(testdir)

    expect_true(is.numeric(processed.df$count))
    expect_true(is.factor(processed.df$id))

    max.count <- max(processed.df$count)
    max.frequency <- processed.df |> select(!c(id, count)) |> max()
    expect_true(max.count >= max.frequency)
})
