import pytest

from main import BooksCollector
class TestBooksCollector:
    # Тест на добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тест на возможность добавления книги
    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        assert collector.get_book_genre('Новая книга') == ''

    # Тест на возможность присвоения книге существующего жанра
    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    # Тест на установление жанра недобавленной книги
    def test_set_book_genre_for_non_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_book_genre('Сияние') is None

        # Тест на установление несуществующего жанра
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Мистика')
        assert collector.get_book_genre('Сияние') == ''

    # Тест на недобавление книг с длиной названия 0 и 41 символ
    @pytest.mark.parametrize("name", ["", "x" * 41])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    # Тест на добавление двух книг с одниковым названием
    def test_add_new_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Чужак')
        collector.add_new_book('Чужак')
        assert len(collector.get_books_genre()) == 1

    # Тест на получения списка книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Чуб земли')
        collector.set_book_genre('Чуб земли', 'Фантастика')
        collector.add_new_book('Чужак')
        collector.set_book_genre('Чужак', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Чуб земли', 'Чужак']

    # Тест на получение книг несуществующего жанра
    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Мистика') == []

    # Тест на получение словаря book_genre
    @pytest.mark.parametrize('books_genre', [{'Оно': 'Ужасы', 'Настоящий детектив': 'Детективы', 'Мумий Тролль': 'Фантастика'}])
    def test_get_book_genre_dict(self, books_genre):
        collector = BooksCollector()
        collector.books_genre = books_genre
        assert collector.books_genre == {'Оно': 'Ужасы', 'Настоящий детектив': 'Детективы', 'Мумий Тролль': 'Фантастика'}

    # Тест на получение книг, подходящих для детей
    @pytest.mark.parametrize('books_genre', [{'Оно': 'Ужасы', 'Настоящий детектив': 'Детективы', 'Мумий Тролль': 'Фантастика'}])
    def test_get_books_for_children(self, books_genre):
        collector = BooksCollector()
        collector.books_genre = books_genre
        assert collector.get_books_for_children() == ['Мумий Тролль']

    # Тест на добавление книги в избранное
    @pytest.mark.parametrize('name', ['Оно', 'Настоящий детектив', 'Мумий Тролль'])
    def test_add_book_in_favorites_one_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    # Тест на добавление двух одинаковых книг в избранное
    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Война и Мир')
        collector.add_book_in_favorites('Война и Мир')
        collector.add_book_in_favorites('Война и Мир')
        assert collector.get_list_of_favorites_books().count('Война и Мир') == 1

    # Тест на удаление книг из избранного
    @pytest.mark.parametrize('name', ['Оно', 'Настоящий детектив', 'Мумий Тролль'])
    def test_delete_book_from_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    # Тест на получение списка избранных книг
    @pytest.mark.parametrize("name", ['Оно', 'Настоящий детектив', 'Мумий Тролль'])
    def test_get_list_of_favorites_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == [name]