import time
t0 = time.time()

print("Mining Trends...\n")
import miner

t1 = time.time()
print(t1-t0)

print("\n\nDownloading URLs...\n\n")
import url_downloader

t2 = time.time()
print(t2 - t1)

print("\n\nDownloading News Articles...\n")
import news_parser

t3 = time.time()
print(t3 - t2)

print("\n\nGenerating Articles...\n")
import summarizer

t4 = time.time()
print(t4 - t3)

print("\n\nRetrieving tweets...\n")
import tweet_retriever

t5 = time.time()
print(t5 - t4)

print("\n\nCategorizing Articles\n\n")
import skclassifier

t6 = time.time()
print(t6 - t5)


print("\n\nGenerating webpages...\n")
import webpage_generator
import mainpage_generator

t7 = time.time()
print(t7-t6)


tot = t7 - t0
print('Total time taken: ')
print(tot)
