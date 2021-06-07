function count(s::String, cns=1)::Dict{Char, Int}
    counts = Dict()
    for c in s
        counts[c] = get(counts, c, 0) + cns
    end
    counts
end

function main()
    n = parse(Int, readline())
    s = readline()
    l = length(s)

    res = 0

    obj_c = count(s)

    base_c = count(s[1:end÷2], 2)
    for i in 1:l
        if base_c == obj_c
            res += 1
        end
        base_c[s[i]] -= 2
        base_c[s[mod1(i + l ÷ 2, l)]] = get(base_c, s[mod1(i + l ÷ 2, l)], 0) + 2
    end
    res
end

main() |> println