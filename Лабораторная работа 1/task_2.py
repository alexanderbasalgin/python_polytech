# TODO Найдите количество книг, которое можно разместить на дискете
inf_v = 1.44 * 1024 * 1024
num_p = 100
num_st = 50
num_sym = 25
one_sym = 4
one_book_weight = num_p * num_st * num_sym * one_sym
print("Количество книг, помещающихся на дискету:", int(inf_v // one_book_weight))
