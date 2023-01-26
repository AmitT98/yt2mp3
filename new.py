import pytube
scan = input('Enter the query')
array = pytube.Search(scan)
pytube.YouTube(array.results[0].watch_url).streams.get_by_itag('140').download()

