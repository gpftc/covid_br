from googlesearch import search
import requests as rq
import wget

num_page = 10


def download_search(query:str,num_page:int) -> list:
	search_results = search(query,num_page)
	size_search = len(search_results)

	for i,result in enumerate(search_results):
		url = result.title().lower()
		print('=+='*10,f'[{i}/{size_search}]site: {url.split("/")[0]}',10*'=+=')

		file_name = f"{url.split('/')[-1]}"
		content_url = rq.get(url).content
		size_content = len(content_url)/(1024**2)

		print(f'[file name: {file_name}] [size file: {size_content}MB]')
		with open('files/'+file_name,'wb') as file:
			
			file.write(content_url)
			print(f'{file_name} salvo!')

		return search_results


'''
with open(file_name,'wb') as file:
		file.write(rq.get(url).content)
		print(f'{file_name} salvo!')

'''