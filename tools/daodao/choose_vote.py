import random
from typing import List, Optional


def choose_vote(votes: dict, choices: Optional[List] = None) -> str | int:
    """
    Выбирает голос с вероятностью, пропорциональной количеству голосов.

    Если choices присутствует (multiple choice):
      - Ожидается, что votes содержит ключ "vote_weights" с списком весов (в виде строк).
      - Функция выбирает случайный вариант на основе весов и возвращает индекс выбранного варианта в виде строки.

    Если choices отсутствует (single choice):
      - votes представляет словарь, где ключи – это названия опций (например, "yes", "no", "abstain"),
        а значения – строки с количеством голосов.
      - Функция возвращает название выбранной опции (с наиболее вероятным выбором на основе весов).

    Аргументы:
      votes: словарь голосов.
      choices: список вариантов (например, объектов Choice) или None.

    Возвращает:
      Выбранный голос: если choices существует – индекс выбранного варианта (в виде строки),
      иначе – название опции ("yes", "no" и т.д.).
    """
    if choices is not None:
        if "vote_weights" not in votes:
            raise ValueError("Для multiple choice требуется наличие ключа 'vote_weights' в votes.")
        weights = [int(w) for w in votes["vote_weights"]]
        total_votes = sum(weights)
        if total_votes == 0:
            raise ValueError("Нет голосов для выбора.")
        indices = list(range(len(weights)))
        chosen_index = random.choices(indices, weights=weights, k=1)[0]
        return chosen_index

    votes_int = {key: int(value) for key, value in votes.items()}
    total_votes = sum(votes_int.values())
    if total_votes == 0:
        raise ValueError("Нет голосов для выбора.")
    vote_options = list(votes_int.keys())
    weights = [votes_int[option] for option in vote_options]
    chosen_option = random.choices(vote_options, weights=weights, k=1)[0]
    return chosen_option
