import library

if __name__ == '__main__':
    path = library.get_path()
    dim, matrix = library.matrix_and_dim(path)
    n = library.get_nb()
    all_total_cost = library.many_total_coast(n, matrix, dim)
    print(f'all (with {n} repeats) :', all_total_cost)
    print('max :', max(all_total_cost))
    print('min :', min(all_total_cost))
