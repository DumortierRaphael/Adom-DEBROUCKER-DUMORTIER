import library
import utils

if __name__ == '__main__':
    nb_repeat = utils.get_nb()
    all_path = utils.get_all_path()
    for path in all_path :
        letter = utils.get_letter_from_path(path)
        dim, matrix = library.matrix_and_dim(path)
        all_total_cost = library.many_total_coast(nb_repeat, matrix, dim)
        print(f'for {letter}, with {nb_repeat} repeats |', 'max :', max(all_total_cost), '| min :', min(all_total_cost))
