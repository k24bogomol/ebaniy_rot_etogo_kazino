init python:
    import random

    def pull_gacha(count):
        prize_list = []
        all_pools = {
            "legendary_char": legendary_char,
            "legendary_item": legendary_item,
            "epic_char": epic_char,
            "epic_item": epic_item
        }

        items = list(all_pools.keys())
        weights = [5, 5, 45, 45]

        for i in range(count):
            chosen_pool_name = random.choices(items, weights=weights, k=1)[0]
            chosen_pool = all_pools[chosen_pool_name]

            result = random.choice(chosen_pool)
            prize_list.append(result)

            with open('example.txt', 'a', encoding='utf-8') as file:
                file.write(result["name"] + '\n')

        return prize_list

