import time
t0 = time.time()

print("Mining Trends...\n")
import miner

print("\n\nDownloading URLs...\n\n")
import url_downloader

print("\n\nDownloading News Articles...\n")
import news_parser

t1 = time.time()
tot = t1 - t0
print('Total time taken: ' + tot)
