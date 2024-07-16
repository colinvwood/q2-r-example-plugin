library(testthat)

test_that('randomize works', {
    source('../../assets/randomize.R')

    df <- tibble(
        id = c("s1", "s2", "s3"),
        feat1 = c(10, 0, 9),
        feat2 = c(100, 3, 4)
    )

    randomized.df <- randomize(df)

    expect_true(identical(df$id, randomized.df$id))
    expect_false(identical(df$feat1, randomized.df$feat1))
    expect_false(identical(df$feat2, randomized.df$feat2))
})
