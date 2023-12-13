from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Tintin')
        collector.add_new_book('Под куполом')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в Восточном экспрессе')
        assert 'Убийство в Восточном экспрессе' in collector.books_genre

    def test_set_book_genre_add_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Tintin', 'Мультфильмы')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.set_book_genre('Под куполом', 'Ужасы')
        assert {'Tintin': 'Мультфильмы'}

    def test_get_book_genre_output_genre(self):
        collector = BooksCollector()
        collector.get_book_genre('Убийство в Восточном экспрессе')
        assert {'Убийство в Восточном экспрессе': 'Детективы'}

    def test_get_books_with_specific_genre_output_specific_genre(self):
        collector = BooksCollector()
        collector.get_books_with_specific_genre('Детективы')
        assert 'Детективы' in collector.genre_age_rating

    def test_get_books_genre_current_dictionary(self):
        collector = BooksCollector()
        assert collector.get_books_genre

    def test_get_books_for_children_rating_book_kids(self):
        collector = BooksCollector()
        collector.get_books_for_children()
        assert collector.get_books_for_children() != ['Ужасы', 'Детективы']

    def test_add_book_in_favorites_add_this_book_favorite(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Убийство в Восточном экспрессе')
        assert collector.add_book_in_favorites('Убийство в Восточном экспрессе') != ['Tintin']

    def test_delete_book_from_favorites_del_this_book_favorite(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Девушка в поезде')
        assert (collector.delete_book_from_favorites('Девушка в поезде'), 'Этой книги нет в списке')

    def test_get_list_of_favorites_books_get_one_favorite_book(self):
        collector = BooksCollector()
        collector.get_list_of_favorites_books()
        assert 'Убийство в Восточном экспрессе'
