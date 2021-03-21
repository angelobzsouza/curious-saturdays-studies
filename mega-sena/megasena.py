from base import get_games


def remove_duplicated(games):
    numbers = [game["numbers"] for game in games]

    no_dupes = [games[n] for n, x in enumerate(numbers) if x not in numbers[:n]]

    return no_dupes


# Print duplicated
def print_duplicated(games):
    numbers = [game["numbers"] for game in games]

    no_dupes = [x for n, x in enumerate(numbers) if x not in numbers[:n]]
    dupes = [x for n, x in enumerate(numbers) if x in numbers[:n]]
    for dupe in no_dupes:
        for game in games:
            if dupe == game["numbers"] and game["id"] == "1537":
                print(game)


def mount_bet_with_less_reps(games):
    alg_repetitions = [{"ix": i, "rep": 0} for i in range(1, 61)]
    for game in games:
        for number in game["numbers"]:
            alg_repetitions[number - 1]["rep"] += 1

    sorted_alg_repetitions = sorted(alg_repetitions, key=lambda k: k["rep"])

    new_game = sorted(
        [
            sorted_alg_repetitions[0]["ix"],
            sorted_alg_repetitions[1]["ix"],
            sorted_alg_repetitions[2]["ix"],
            sorted_alg_repetitions[3]["ix"],
            sorted_alg_repetitions[4]["ix"],
            sorted_alg_repetitions[5]["ix"],
            sorted_alg_repetitions[6]["ix"],
            sorted_alg_repetitions[7]["ix"],
            sorted_alg_repetitions[8]["ix"],
            sorted_alg_repetitions[9]["ix"],
            sorted_alg_repetitions[10]["ix"],
            sorted_alg_repetitions[11]["ix"],
        ]
    )

    return sorted(new_game)


def mount_bet_with_more_reps(games):
    alg_repetitions = [{"ix": i, "rep": 0} for i in range(1, 61)]
    for game in games:
        for number in game["numbers"]:
            alg_repetitions[number - 1]["rep"] += 1

    sorted_alg_repetitions = sorted(alg_repetitions, key=lambda k: k["rep"])

    new_game = [
        sorted_alg_repetitions[59]["ix"],
        sorted_alg_repetitions[58]["ix"],
        sorted_alg_repetitions[57]["ix"],
        sorted_alg_repetitions[56]["ix"],
        sorted_alg_repetitions[55]["ix"],
        sorted_alg_repetitions[54]["ix"],
        sorted_alg_repetitions[53]["ix"],
        sorted_alg_repetitions[52]["ix"],
        sorted_alg_repetitions[51]["ix"],
        sorted_alg_repetitions[50]["ix"],
        sorted_alg_repetitions[49]["ix"],
        sorted_alg_repetitions[48]["ix"],
    ]

    return sorted(new_game)


def mount_bet_with_more_reps_in_quaters(games):
    alg_repetitions = [{"ix": i, "rep": 0} for i in range(1, 61)]
    for game in games:
        for number in game["numbers"]:
            alg_repetitions[number - 1]["rep"] += 1

    first_quarter = sorted(
        alg_repetitions[0:4] + alg_repetitions[10:14] + alg_repetitions[20:24],
        key=lambda k: k["rep"],
    )
    sec_quarter = sorted(
        alg_repetitions[5:9] + alg_repetitions[15:19] + alg_repetitions[25:29],
        key=lambda k: k["rep"],
    )
    third_quarter = sorted(
        alg_repetitions[30:34] + alg_repetitions[40:44] + alg_repetitions[50:54],
        key=lambda k: k["rep"],
    )
    fourth_quarter = sorted(
        alg_repetitions[35:39] + alg_repetitions[45:49] + alg_repetitions[55:59],
        key=lambda k: k["rep"],
    )

    return sorted(
        [
            first_quarter[11]["ix"],
            sec_quarter[11]["ix"],
            third_quarter[11]["ix"],
            fourth_quarter[11]["ix"],
            first_quarter[10]["ix"],
            sec_quarter[10]["ix"],
            third_quarter[10]["ix"],
            fourth_quarter[10]["ix"],
            first_quarter[9]["ix"],
            sec_quarter[9]["ix"],
            third_quarter[9]["ix"],
            fourth_quarter[9]["ix"],
            first_quarter[8]["ix"],
            sec_quarter[8]["ix"],
            third_quarter[8]["ix"],
            fourth_quarter[8]["ix"],
        ]
    )


def main():
    games = remove_duplicated(get_games())

    bet = [1, 2, 3, 4, 5, 6]

    for game in games:
        match = 0

        for num in bet:
            if num in game["numbers"]:
                match += 1

        if match >= 5:
            print(bet)
            print(game)
            print(match)

    count = 0
    for num, game in enumerate(games):
        match = 0
        new_game = mount_bet_with_more_reps_in_quaters(games[:num])
        for num in new_game:
            if num in game["numbers"]:
                match += 1

        if match >= 5:
            count += 1
            print(new_game)
            print(game)
            print(match)

    print(count)


main()
