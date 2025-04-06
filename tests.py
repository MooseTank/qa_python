import pytest

class TestBooksCollector:
    # Тест 1 на добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тест 2 на возможность добавления книги
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Новая книга')
        assert collector.get_book_genre('Новая книга') == ''

    # Тест 3 на возможность присвоения книге существующего жанра
    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.books_genre['Оно'] == 'Ужасы'

    # Тест 4 на установление жанра недобавленной книги
    def test_set_book_genre_for_non_existing_book(self, collector):
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_book_genre('Сияние') is None

    # Тест 5 на установление несуществующего жанра
    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Мистика')
        assert collector.get_book_genre('Сияние') == ''

    # Тест 6 на добавление книг с длиной названия > 0 и <= 40
    @pytest.mark.parametrize("name", ["Мой Рагнарёк", "X" * 40])
    def test_add_new_book_valid_name_length(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # Тест 7 на недобавление книг с длиной названия 0 и 41 символ
    @pytest.mark.parametrize("name", ["", "x" * 41])
    def test_add_new_book_invalid_name_length(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    # Тест 8 на добавление двух книг с одниковым названием
    def test_add_new_book_twice(self, collector):
        collector.add_new_book('Чужак')
        collector.add_new_book('Чужак')
        assert len(collector.get_books_genre()) == 1

    # Тест 9 на получение жанра книги по её имени
    def test_get_book_genre(self, collector):
        collector.add_new_book('Мёртвый ноль')
        collector.set_book_genre('Мёртвый ноль', 'Фантастика')
        assert collector.get_book_genre('Мёртвый ноль') == 'Фантастика'

    # Тест 10 на получения списка книг с определенным жанром
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Чуб земли')
        collector.set_book_genre('Чуб земли', 'Фантастика')
        collector.add_new_book('Чужак')
        collector.set_book_genre('Чужак', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Чуб земли', 'Чужак']

    # Тест 11 на получение книг несуществующего жанра
    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        assert collector.get_books_with_specific_genre('Мистика') == []

    # Тест 12 на получение словаря book_genre
    def test_get_book_genre_dict(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.books_genre == {'Оно': 'Ужасы'}

    # Тест 13 на получение книг, подходящих для детей
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Мумий Тролль')
        collector.set_book_genre('Мумий Тролль', 'Фантастика')
        assert collector.get_books_for_children() == ['Мумий Тролль']

    # Тест 14 на добавление книги в избранное
    def test_add_book_in_favorites_one_book(self, collector):
        collector.add_new_book('Настоящий детектив')
        collector.add_book_in_favorites('Настоящий детектив')
        assert 'Настоящий детектив' in collector.favorites

    # Тест 15 на добавление двух одинаковых книг в избранное
    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book('Война и Мир')
        collector.add_book_in_favorites('Война и Мир')
        collector.add_book_in_favorites('Война и Мир')
        assert collector.get_list_of_favorites_books().count('Война и Мир') == 1

    # Тест 16 на удаление книг из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.favorites

    # Тест 17 на получение списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Оно']