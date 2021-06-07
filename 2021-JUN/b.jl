function main()
    n = parse(Int, readline())
    count = Dict()
    for _ in 1:n
        s = readline()
        count[s] = get(count, s, 0) + 1
    end
    for (k, v) in pairs(count)
        if v == 2
            return k
        end
    end
end


main() |> println
