# qa_python
1.Метод проверяет, что словарь с добавленными книгами возвращает ожидаемое количество книг
test_add_new_book_add_two_books
2.С использованием параметризации добавлено несколько названий книг, метод проверяет, что все названия содержатся в коллекции
test_add_new_book_add_book
3.Добавлен невалидный набор данных. Если добавляется книга с пустым названием или со слишком длинным названием, метод возвращает ожидаемый результат
4.Добавлены книги с присвоением жанров. Проверка на соответствие жанра заданному названию книги
test_set_book_genre_add_genre
5.Добавленной книге верно присваивается указанный жанр
test_get_book_genre_output_genre
6.Метод возвращает весь список книг, соответствующих заданному жанру
test_get_books_with_specific_genre_output_specific_genre
7.Словарь содержит верное значение жанра добавленной книги
test_get_books_genre_current_dictionary
8.Запрещенные жанры книг не содержатся в списке детских книг
test_get_books_for_children_rating_book_kids
9.Добавленная книга содержится в избранном
test_add_book_in_favorites_add_this_book_favorite
10.Удаленная из избранного книга не содержится в списке favorites
test_delete_book_from_favorites_del_this_book_favorite
11.Метод возвращает весь список книг, добавленных в избранное
test_get_list_of_favorites_books_get_one_favorite_book
