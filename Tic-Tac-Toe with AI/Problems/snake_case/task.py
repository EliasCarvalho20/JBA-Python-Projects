for t in input():
    print(t.replace(t, f"_{t.lower()}") if t.isupper() else t, end='')
