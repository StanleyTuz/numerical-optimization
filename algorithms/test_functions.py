import torch

torch.pi = torch.acos(torch.zeros(1)).item() * 2


"""
2-dim quadratic function
global minimum at [1,3], optimal value of 0
"""
def booth(x: torch.tensor):
    return (x[0] + 2*x[1] -7)**2 + (2*x[0] + x[1] - 5)**2

"""
2-dim function with four global minima
"""
def branin(x: torch.tensor, a=1, b=5.1/(4*torch.pi**2), c=5/torch.pi, r=6, s=10, t=1/(8*torch.pi)):
    return a*(x[1] - b*x[0]**2 + c*x[0] - r)**2 + s*(1-t)*torch.cos(x[0]) + s


"""
2-dim function with no global minimum thanks to atan being undefined at origin
"""
def flower(x: torch.tensor, a=1, b=1, c=4):
    return a*torch.norm(x) + b*torch.sin( c*torch.atan2(x[1], x[0]))



"""
Rosenbrock banana function
The global minimum at [a,a^2], inside a long narrow valley, 
is tough to reach.
"""
def rosenbrock(x: torch.tensor, a=1, b=5):
    return (a - x[0])**2 + b*(x[1] - x[0]**2)**2