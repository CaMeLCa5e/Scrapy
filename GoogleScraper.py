#! usr/bin/python 
import GoogleScraper
import urllib.parse

GoogleScraper.setup_logger()

if __name__ == '__main__':
	
	results = GoogleScraper.scrape('Best SEO Tool', 
									num_results_per_page=50, 
									num_pages=3, 
									offset=0,
									searchtype='normal')

	for page in results:
		for link_title, link_snippet, link_url, *rest in page['results']:
			# link_url.scheme
			# link_url.netloc
			# link_url.path
			# link_url.params
			# link_url.query
			try:
				print(urllib.parse.unquote(link_url.geturl()))
			except:
				pass

# print total number or returned values on each page 
print (sum(len(page['results']) for page in results))

# print how many urls were returned on all pages
print (results[0]['num_results_per_kw'])












