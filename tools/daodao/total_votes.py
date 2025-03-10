from typing import Optional, List


def get_total_votes(votes: dict, choices: Optional[List] = None) -> int:
    """
    Возвращает общую сумму голосов.

    Если choices присутствует (multiple choice):
      - Ожидается, что votes содержит ключ "vote_weights" с списком весов (в виде строк).
      - Функция суммирует веса.

    Если choices отсутствует (single choice):
      - votes представляет словарь, где значения – это строки с количеством голосов.
      - Функция суммирует все голоса.

    Аргументы:
      votes: словарь голосов.
      choices: список вариантов или None.

    Возвращает:
      Общая сумма голосов в виде целого числа.
    """
    if choices is not None:
        if "vote_weights" not in votes:
            raise ValueError("Для multiple choice требуется наличие ключа 'vote_weights' в votes.")
        weights = [int(w) for w in votes["vote_weights"]]
        return sum(weights)
    else:
        return sum(int(value) for value in votes.values())
