import random


def how_many_before_collision(buckets, loops=1):
    '''
    Roll random has indexes into buckets and print
     how many rolls before a hash collision

     run loops number of times
    '''

    for i in range(loops):
        # keep track of tries
        tries = 0
        # make a set of tried indecies
        tried = set()
        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                # add index to list of tried
                tried.add(hash_index)
                # Update count of number of tries
                tries += 1

            else:
                # We found a collision
                break
        print(
            f"{buckets} buskets, {tries} hashes before collision. ({tries / buckets * 100:.1f}%)")


# how_many_before_collision(32, 10)


def longest_linked_list_chain(keys, buckets, loops=10):
    '''
    Rolls keys number of random keys into buckets
    and count the collisions

    run loops times 
    '''

    for i in range(loops):
        key_counts = {}

        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]

        print(
            f"Longest linked list chain for {keys} keys in {buckets} buckets Load Factor: {keys/buckets:2f}: {largest_n})")


longest_linked_list_chain(16, 16, 10)
