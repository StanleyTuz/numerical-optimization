
"""
Generate a population of m design points (chromosomes, individuals, ...)
from within the hyperrectangle with lower-bound vector a and upper-bound
vector b.
"""
function rand_population_uniform(m, a, b)
    d = length(a);
    return [a+rand(d).*(b-a) for i in 1:m]
end


##
using Distributions

function rand_population_normal(m, μ, Σ)
    D = MvNormal(μ, Σ) # distribution
    return [rand(D) for i in 1:m]
end

## 
using Distributions 
function rand_population_cauchy(m, μ, σ)
    n = length(μ)
    return [[rand(Cauchy(μ[j], σ[j])) for j in 1:n] for i in 1:m]
end


##
using Plots
m = 100
X = rand_population_normal(100, [-2., -2.], [[1.5, 0.] [0., 3.]]);
# X = rand_population_uniform(m, [-2.,-2.], [2.,2.]);
x = [x[1] for x in X];
y = [x[2] for x in X];
for j in 1:m
    display(scatter(x, y));
end


##
function genetic_algorithm(f, population, k_max, S, C, M)

end
