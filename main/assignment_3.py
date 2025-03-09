def f(t, y):
    return t - y**2

def euler_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t = t0
    y = y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

def runge_kutta(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t = t0
    y = y0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h/2, y + (h/2)*k1)
        k3 = f(t + h/2, y + (h/2)*k2)
        k4 = f(t+h, y + h*k3)
        y += (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        t += h
    return y

if __name__ == "__main__":
    t0 = 0
    y0 = 1
    t_end = 2
    iterations = 10

    euler_result = euler_method(f, t0, y0, t_end, iterations)
    rk_result = runge_kutta(f, t0, y0, t_end, iterations)
    print(euler_result)
    print(rk_result)
