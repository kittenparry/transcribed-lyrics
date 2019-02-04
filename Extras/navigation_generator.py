import os

path_bands = '../Bands'
path_subs = []
files = []

#get band names
n_bands = [f for f in os.listdir(path_bands) if not f == 'Navigation.md']
n_albums = []
#get album paths
for band in n_bands:
  path_sub = f'{path_bands}/{band}/'
  #this assumes one album per band should be changed
  album = ''.join(os.listdir(path_sub))
  path_sub = path_sub + album
  n_albums.append(album)
  path_subs.append(path_sub)
#get song names
for i in range(len(path_subs)):
  files.append([f for f in os.listdir(path_subs[i]) if not f == 'README.md'])
#remove the .md ending for links
for file in files:
  for i in range(len(file)):
    # file[i] = file[i].rstrip('.md')
    file[i] = file[i].replace('.md', '')
#this also assumes one album per band
#get paths for md file
paths = []
for i in range(len(n_bands)):
  paths.append([])
  paths[i] = [f for f in files[i]]
  for x in range(len(paths[i])):
    paths[i][x] = f'{n_bands[i]}/{n_albums[i]}/{paths[i][x]}'
    paths[i][x] = paths[i][x].replace(' ', '%20')
#non-numbered song names
n_songs = [f for f in files]
for file in n_songs:
  for i in range(len(file)):
    file[i] = file[i][4:]

#navigation.md creation
temp = ''
temp += '# Navigation\n'
temp += '## Contents\n'
for i in range(len(n_bands)):
  p = f'{n_bands[i]} - {n_albums[i]}'
  temp += f'{i+1}. [{p}](#{p.lower().replace(" ", "-")})\n'
temp += '\n---\n\n'
#this also assumes one album per band
for i in range(len(n_bands)):
  temp += f'### {n_bands[i]} - {n_albums[i]}\n'
  x = 1
  for song in n_songs[i]:
    temp += f'{x}. [{song}]({paths[i][x-1]})\n'
    x += 1
  temp += '\n'

with open('../Bands/Navigation.md', 'w') as f:
  f.write(temp)
