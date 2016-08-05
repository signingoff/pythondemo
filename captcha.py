from captcha_solver import CaptchaSolver

def decode():
    solver = CaptchaSolver('browser')
    with open('test.jpg', 'rb') as inp:
        raw_data = inp.read()
    print(solver.solve_captcha(raw_data))

if __name__=='main':
    decode()