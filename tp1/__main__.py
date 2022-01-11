import library
import utils

if __name__ == '__main__':
    all_path = utils.get_all_path()
    nb = 3
    print(
        f'File  | min: Q2_3   Q3_1  | avg: Q2_3   Q3_1  | min_points Q2_3 && Q3_1  all: Q2_3 && Q3_1')
    for path in all_path :
        letter = utils.get_letter_from_path(path)
        dim, matrix = library.matrix_and_dim(path)
        #2.3 | 3.1
        all_question2_3 = []
        all_question3_1 = []
        all_points_question2_3 = []
        all_points_question3_1 = []
        for i in range(nb) :
            question2_3, points2_3 = library.total_cost(matrix, dim)
            question3_1, points3_1 = library.all_closest_point(matrix, dim)
            all_question2_3.append(question2_3)
            all_question3_1.append(question3_1)
            all_points_question2_3.append(points2_3)
            all_points_question3_1.append(points3_1)
        min_all_question2_3 = min(all_question2_3)
        min_all_question3_1 = min(all_question3_1)
        index_min_points_2_3 = all_question2_3.index(min_all_question2_3)
        index_min_points_3_1 = all_question3_1.index(min_all_question3_1)
        print(f'For {letter} | min:', min_all_question2_3, min_all_question3_1,
                            '| avg:', int(sum(all_question2_3) / len(all_question2_3)), int(sum(all_question3_1) / len(all_question3_1)),
                            '| points: ', all_points_question2_3[index_min_points_2_3], '&&', all_points_question3_1[index_min_points_3_1],
                            '| all:', all_question2_3, '&&', all_question3_1)

