# DWITE '07 R3 #3 - Playlist
# DMOJ: https://dmoj.ca/problem/dwite07c3p3

def max_playlist_rating(player_space, songs):
    knapsack_values = [0] * (player_space + 1)

    for song in songs:
        song_space, song_rating = song
        for current_space in range(player_space, song_space - 1, -1):
            knapsack_values[current_space] = max(knapsack_values[current_space - song_space] + song_rating, knapsack_values[current_space])

    return max(knapsack_values)

for _ in range(5):  # for each data set
    player_space = int(input())
    num_songs = int(input())
    songs = []
    for _ in range(num_songs):
        _, song_rating, song_space = input().split()
        songs.append((int(song_space), int(song_rating)))  # append song as a tuple (space, rating)
    print(max_playlist_rating(player_space, songs))
