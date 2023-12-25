import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Золотой ключик')
        collector.add_new_book('12 стульев')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('title', ['Понедельник начинается в субботу', 'Золотой теленок'])
    def test_add_new_book_add_books(self, title):
        collector = BooksCollector()
        collector.add_new_book(title)
        assert title in collector.get_books_genre()

    @pytest.mark.parametrize("invalid_title, expected_result",
                             [('', False), ('Странная история доктора Джекила и мистера Хайда', False)])
    def test_add_new_book_boundary_values_of_the_input_data(self, invalid_title, expected_result):
        collector = BooksCollector()
        collector.add_new_book(invalid_title)
        assert (invalid_title in collector.get_books_genre()) == expected_result

    '''Метод изменен. Замена на проверку отсутствия жанра у добавленной книги, если его нет в списке жанров'''
    def test_set_book_genre_add_genre_not_list(self):
        collector = BooksCollector()
        collector.add_new_book('Tintin')
        collector.add_new_book('Под куполом')
        collector.set_book_genre('Tintin', 'Мультфильмы')
        collector.set_book_genre('Под куполом', 'Научная фантастика')
        assert '' == collector.get_book_genre('Под куполом')

    '''Метод оставлен без изменений'''
    def test_get_book_genre_output_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        assert collector.get_book_genre('Убийство в Восточном экспрессе') == 'Детективы'

    def test_get_books_with_specific_genre_output_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.add_new_book('Под куполом')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.set_book_genre('Под куполом', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Под куполом', 'Сияние']

    def test_get_books_genre_current_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        assert collector.get_books_genre() == {'Убийство в Восточном экспрессе': 'Детективы'}

    '''Метод изменен. Проверка, что возвращаются книги жанров, подходящих для детей'''
    def test_get_books_for_children_books_for_children_genre(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_new_book('Тайна отца Брауна')
        collector.set_book_genre('Тайна отца Брауна', 'Детективы')
        assert collector.get_books_for_children() == ['12 стульев']

    def test_add_book_in_favorites_add_this_book_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Tintin')
        collector.add_book_in_favorites('Tintin')
        assert 'Tintin' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_del_this_book_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Tintin')
        collector.add_book_in_favorites('Tintin')
        collector.delete_book_from_favorites('Tintin')
        assert 'Tintin' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_get_one_favorite_book(self):
        collector = BooksCollector()
        collector.add_new_book('Tintin')
        collector.add_new_book('Понедельник начинается в субботу')
        collector.add_book_in_favorites('Tintin')
        collector.add_book_in_favorites('Понедельник начинается в субботу')
        assert collector.get_list_of_favorites_books() == ['Tintin', 'Понедельник начинается в субботу']
