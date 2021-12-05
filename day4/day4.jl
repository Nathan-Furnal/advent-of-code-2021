using DelimitedFiles


numbers = parse.(Int, split(readline("numbers.txt"), ","))[:, :, :, :] # reshape as (numbers, 1, 1, 1)


boards = readdlm("boards.txt", Int)

