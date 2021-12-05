using Statistics

function read_file(path)
    data = readlines(path)
    n = length(data)
    k = length(first(data))
    # Reshape and transpose to get the original shape back
    return reshape(parse.(Int, Iterators.flatten(split.(data, ""))), (k, n))'
end

arr = read_file("input.txt")

# Part 1

function compute_consumption(arr)
    bits = convert.(Int, median(arr, dims=1))
    gamma = join(bits)
    eps = join(1 .- bits)

    return parse(Int, gamma, base = 2) * parse(Int, eps, base = 2)
end

sol1 = compute_consumption(arr)

# Part 2

function compute_rating(arr, start = 1, mode = "oxy")
    if size(arr)[1] == 1 || start > size(arr)[2]
        return join(arr)
    else
        bit = (mode == "oxy") ? ceil(median(arr[:, start])) : 1 - ceil(median(arr[:, start]))
        arr = arr[arr[:, start] .== bit, :]
        compute_rating(arr, start + 1, mode)
    end
end

gam = compute_rating(arr, 1, "oxy")
eps = compute_rating(arr, 1, "co2")
sol2 = parse(Int, gam, base = 2) * parse(Int, eps, base = 2)
