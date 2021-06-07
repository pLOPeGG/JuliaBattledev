function main()
    n, a, c = parse.(Ref(Int), readline() |> split)
    grid = parse.(Ref(Int), readline() |> split) |> collect
    append!(grid, zeros(Int, a+c+1))

    fast_range = vcat([0], cumsum(grid))
    dp = Dict(i => 0 for i in 0:(n+a+c+1))

    for i in 0:n+1
        dp[i+1] = max(dp[i+1], dp[i])
        dp[i+a+c] = dp[i] + fast_range[i+a+1] - fast_range[i+1]
    end
    sum(grid) - maximum(values(dp))
end

main() |> println