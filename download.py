# Install the library first
# pip install icrawler

from icrawler.builtin import BingImageCrawler

sports_persons = {
    'messi': 'Lionel Messi face',
    'ronaldo': 'Cristiano Ronaldo face',
    'virat_kohli': 'Virat Kohli face',
    'ricky_ponting': 'Ricky Ponting face',
    'chris_gayle': 'Chris Gayle face'
}

for folder, keyword in sports_persons.items():
    crawler = BingImageCrawler(storage={'root_dir': f'sports_persons_dataset/{folder}'})
    crawler.crawl(keyword=keyword, max_num=20)  # Download 20 images per person
