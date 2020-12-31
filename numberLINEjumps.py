# def kangaroo(x1, v1, x2, v2):
#     n_jumps = 1
#     while n_jumps < 10000:
#         x1_end = x1 + (v1*n_jumps)
#         x2_end = x2 + (v2*n_jumps)

#         if x1_end == x2_end:
#             ans = 'YES'
#             break
#         else:
#             ans = 'NO'
#         n_jumps += 1
#     return ans

# print(kangaroo(0,3,4,2))

import pandas as pd
df_movie = pd.read_csv('movie_sample_dataset.csv')

df_actor = df_movie['actors']
actor = []
for a in df_actor:
    actor.append(a.split(','))

actor2 = []
for ac in actor:
    actor2 += ac

actor_series = pd.Series(data = actor2)
df_actor2 = pd.DataFrame(actor_series.unique(), columns = ['name'])
import random
rand_index = random.sample(range(1000, 2000), 209)
rand_series = pd.Series(rand_index)
df_actor2 = df_actor2.set_index(rand_series)
df_casting = df_movie[['movie_title', 'actors']]
func_split= lambda x: pd.Series([i for i in reversed(x.split(','))])
split_act = df_casting['actors'].apply(func_split)
split_act.rename(columns={2:'Leading', 1:'Supporting1', 0:'Supporting2'}, inplace=True)
df_casting2 = pd.concat([df_casting, split_act], axis=1, join='inner')
df_casting2 = df_casting2.drop('actors', axis=1)
df_actor2.reset_index(inplace = True)

for n in df_actor2['name']:
    for s in df_casting2['Supporting2']:
        if s == n:
            df_casting2['Supporting2'] = df_actor2['index']